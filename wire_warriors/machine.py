from enum import Enum
import logging
import sys

from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

import requests
from starlette.responses import JSONResponse

# Replace with your actual endpoint URL
url = "https://example.com/api/data"

_logger = logging.getLogger(__name__)
logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO)

router = APIRouter(
    prefix="/machine",
    tags=["Machine"],
    responses={404: {"description": "Not found"}},
    dependencies=[],
)

class Direction(Enum):
    IN="in"
    OUT="out"

class RotorPosition(BaseModel):
    """Model for rotor position."""

    rotor_index: int = Field(..., description="Index of the rotor (0-based).")
    position: str = Field(..., description="Letter that represents the current rotor position.")


class RotationInstruction(BaseModel):
    rotor_index: int = Field(..., description="Index of the rotor to use for rotating.")
    position_count: int = Field(1, description="Number of positions to rotate.")


class RotationResult(BaseModel):
    rotor_index: int = Field(..., description="Index of the rotor to use for rotating.")
    trigger_next: bool = Field(..., description="Whether the rotation also triggers the next rotor.")
    position: str = Field(..., description="The new position indicator of after rotating.")

class EncoderData(BaseModel):
    """Input model for encoding a character with the rotor."""

    rotor_index: int = Field(..., description="Index of the rotor to use for encoding (0-based).")
    character: str = Field(..., description="Character to encode using the rotor.")
    direction: Direction = Field(Direction.IN, description="Direction to encode the character.")

    def to_url(self) -> str:
        return "http://127.0.0.1:8000/rotor/encode/?rotor_index={}&character={}&direction={}".format(
            self.rotor_index,
            self.character,
            self.direction.value
        )

class Enigma(BaseModel):
    reflector: list[str] = Field(..., description="Reflector wiring, consisting of 13 unique letter pairs.")
    plugs: list[str] = Field([], description="Plugs setting. At most 13 unique letter pairs.")

    def _reflect(self, character: str) -> str:
        """Reflects the character using the reflector wiring."""
        for pair in self.reflector:
            if character in pair:
                return pair[1] if pair[0] == character else pair[0]
        raise ValueError(f"Character {character} not found in reflector wiring.")

    def get_key(self):
        result = ""
        for n in range(3):
            path = f"http://127.0.0.1:8000/rotor/position/{n}"
            response = http_get_json(path)
            rotor_position = RotorPosition.model_validate(response)
            result = f"{result}{rotor_position.position}"
        return result

    def set_key(self, key: str):
        path = f"http://127.0.0.1:8000/rotor/position"
        for n in range(3):
            data = RotorPosition(rotor_index=n, position=key[n]).model_dump_json()
            _logger.info(f"Setting rotor position {n} to {key[n]}")
            http_post_json(path, data)
        return key

    def _rotate_rotors(self):
        path = f"http://127.0.0.1:8000/rotor/rotate"
        n = 0
        while n < 3:
            data = RotationInstruction(rotor_index=n, position_count=1).model_dump_json()
            _logger.info(f"Rotating rotor {n}...")
            response = http_post_json(path, data)
            rotation_result = RotationResult.model_validate(response)
            if not rotation_result.trigger_next:
                break
            n += 1

    def add_plug(self, plug: str):
        if len(plug) != 2 or not plug.isalpha() or plug[0] == plug[1]:
            raise ValueError("Plug must consist of two different alphabetic characters.")
        for p in self.plugs:
            if plug[0] in p or plug[1] in p:
                raise IndexError(f"Plug {plug} conflicts with existing plug {p}.")
        self.plugs.append(plug)

    def clear_plugs(self):
        self.plugs = []

    @staticmethod
    def _rotor_encode(rotor_index: int, char: str, direction: Direction):
        to_encode = EncoderData(
            rotor_index=rotor_index,
            character=char,
            direction=direction,
        )
        response = http_get_json(to_encode.to_url())
        validated = EncoderData.model_validate(response)
        return validated.character

    def _plug(self, char:str):
        for plug in self.plugs:
            if char in plug:
                return plug[1] if plug[0] == char else plug[0]
        return char

    def _encode(self, char: str) -> str:
        encoded_char = self._plug(char)
        for n in range(3):
            encoded_char = self._rotor_encode(n, encoded_char, Direction.IN)
        encoded_char = self._reflect(encoded_char)
        for n in range(2, -1, -1):
            encoded_char = self._rotor_encode(n, encoded_char, Direction.OUT)
        self._rotate_rotors()
        return self._plug(encoded_char)

    def _send_message(self, message: str):
        encrypted_message = []
        for char in message.upper():
            encrypted_message.append(self._encode(char))
        return "".join(encrypted_message)

    def encrypt(self, message: str) -> str:
        """Encrypts a message using the reflector."""
        key = self.get_key()
        return f"{key}{self._send_message(message)}"

    def decrypt(self, message: str) -> str:
        key = message[:3]
        message = message[3:]

        self.set_key(key)
        return self._send_message(message)

enigma = Enigma(
    reflector=['QJ', 'AZ', 'RP', 'XK', 'MW', 'TG', 'YB', 'NS', 'LU', 'VO', 'HE', 'IC', 'DF']
)

def http_get_json(url: str):
    """Simple HTTP client"""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()  # Parse JSON response
    _logger.info("Data received:", data)
    return data

def http_post_json(url: str, data: str):
    """Simple HTTP client"""
    response = requests.post(url=url, data=data)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()  # Parse JSON response
    _logger.info("Response from post:", data)
    return data


@router.get("/key")
def get_key() -> str:
    """Fetches a key from the rotors in the enigma."""
    return enigma.get_key()


@router.post("/key")
def set_key(key: str) -> str:
    """Sets the positions of the rotors."""
    return enigma.set_key(key)


@router.post("/encrypt")
def encrypt(
    message: str,
):
    """Encrypts a message using the Enigma machine."""
    if not message.isalpha():
        raise HTTPException(status_code=400, detail="Message must contain only alphabetic characters.")

    return enigma.encrypt(message)


@router.post("/decrypt")
def decrypt(
    message: str,
):
    """Encrypts a message using the Enigma machine."""
    if not message.isalpha():
        raise HTTPException(status_code=400, detail="Message must contain only alphabetic characters.")

    return enigma.decrypt(message)

@router.get("/plug/list")
def list_plugs() -> str:
    """Encrypts a message using the Enigma machine."""
    return ",".join(enigma.plugs)

@router.post("/plug", response_class=Response, status_code=201)
def add_plug(
    message: str,
):
    """Encrypts a message using the Enigma machine."""
    try:
        enigma.add_plug(message)
    except ValueError:
        raise HTTPException(400, detail="Plug must consist of two different alphabetic characters.")
    except IndexError:
        raise HTTPException(400, detail="Some characters already occur in the plug settings.")
    return Response(status_code=201)

@router.delete("/plug/reset")
def reset_plugs():
    """Encrypts a message using the Enigma machine."""
    return enigma.clear_plugs()
