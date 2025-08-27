from enum import Enum
import logging
import sys

from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

_logger = logging.getLogger(__name__)
logging.basicConfig(handlers=[logging.StreamHandler(sys.stdout)], level=logging.INFO)

router = APIRouter(
    prefix="/rotor",
    tags=["Rotor"],
    responses={404: {"description": "Not found"}},
    dependencies=[],
)

class Rotor(BaseModel):
    """Rotor model for the Enigma machine."""

    rotor_string: str = Field(..., description="Rotor string, which indicates the current position of the rotor.")
    wiring_string: str = Field(..., description="The wiring string, consisting of 26 unique letters.")
    encryption_string: str = Field("", description="The encryption string, consisting of 26 unique letters.")
    position: int = Field(0, description="The encryption string, consisting of 26 unique letters.")

    def __init__(self, **data):
        super().__init__(**data)
        self.position = 0
        self.encryption_string = self._filtered_wiring_string()
        if len(self.encryption_string) != 26 or len(set(self.encryption_string)) != 26:
            raise ValueError("Wiring string must contain 26 unique letters and notch indicators (').")

    def encode(self, character: str, direction: "Direction") -> str:
        if direction == Direction.IN:
            return self.encryption_string[ord(character) - 65]
        return chr(self.encryption_string.index(character) + 65)

    def get_position(self):
        return self.rotor_string[self.position]

    def set_position(self, position_key: str):
        position = self.rotor_string.index(position_key)
        self._rotate_to(position)

    def _filtered_wiring_string(self):
        return self.wiring_string.replace("'", "")

    def _prepend_last_characters(self, encryption_string: str, modulated_count: int):
        if modulated_count == 0:
            return encryption_string
        return encryption_string[-modulated_count:26] + encryption_string[0:26-modulated_count]

    def _increase_encryption_index(self, encryption_string: str, modulated_count: int):
        return "".join([chr(65 + (ord(i) - 65 + modulated_count) % 26) for i in encryption_string])

    def _compute_new_position(self, count: int):
        return (count + self.position) % 26

    def _rotate_to(self, new_position: int):
        self.position = new_position
        old_encryption_string = self.encryption_string
        self.encryption_string = self._increase_encryption_index(
            self._prepend_last_characters(self._filtered_wiring_string(), new_position),
            new_position,
        )
        _logger.info(f"Rotated rotor: {old_encryption_string} -> {self.encryption_string}")

    def rotate(self, count: int):
        new_position = self._compute_new_position(count)
        has_notch = count == 1 and self.wiring_string[self.position + 1] == "'"
        self._rotate_to(new_position)
        return has_notch



class RotorPosition(BaseModel):
    """Model for rotor position."""

    rotor_index: int = Field(..., description="Index of the rotor (0-based).")
    position: str = Field(..., description="Letter that represents the current rotor position.")


class Direction(Enum):
    IN="in"
    OUT="out"


class EncoderData(BaseModel):
    """Input model for encoding a character with the rotor."""

    rotor_index: int = Field(..., description="Index of the rotor to use for encoding (0-based).")
    character: str = Field(..., description="Character to encode using the rotor.")
    direction: Direction = Field(Direction.IN, description="Direction to encode the character.")


class RotationInstruction(BaseModel):
    rotor_index: int = Field(..., description="Index of the rotor to use for rotating.")
    position_count: int = Field(1, description="Number of positions to rotate.")


class RotationResult(BaseModel):
    rotor_index: int = Field(..., description="Index of the rotor to use for rotating.")
    trigger_next: bool = Field(..., description="Whether the rotation also triggers the next rotor.")
    position: str = Field(..., description="The new position indicator of after rotating.")

rotors = [
    Rotor(
        rotor_string="PYQZJXKLMNOBVHTGUESRACIDWF",
        wiring_string="QJZKXG'ELVYBNSMUPWHTOIRADCF"
    ),
    Rotor(
        rotor_string="XQJZKLMNOBVYHUPTGWESRACFID",
        wiring_string="WQZJXKLM'NOBVYHUPTGFESRACID'"
    ),
    Rotor(
        rotor_string="JQZKXLMNOBVYHUPTGWERSACFID",
        wiring_string="Y'QJXKZVBNMLWUPGHTOIRFESDAC"
    ),
]

@router.get(
    "/position/{rotor_index}",
    response_model=RotorPosition,
    summary="Get rotor position",
    description="Retrieve the current position of a specific rotor by its index.",
)
async def get_rotor_position(rotor_index: int) -> RotorPosition:
    """Get the wiring string of a specific rotor by its index."""
    if 0 <= rotor_index < len(rotors):
        rotor = rotors[rotor_index]
        return RotorPosition(
            rotor_index=rotor_index,
            position=rotor.get_position(),
        )
    else:
        raise HTTPException(status_code=404, detail="Rotor not found.")

@router.post(
    "/position",
    response_model=RotorPosition,
    summary="Set rotor position",
    description="Set a rotor to a specific position",
)
async def post_rotor_position(rotor_position: RotorPosition) -> RotorPosition:
    """Get the wiring string of a specific rotor by its index."""
    if 0 <= rotor_position.rotor_index < len(rotors):
        rotor = rotors[rotor_position.rotor_index]
        rotor.set_position(rotor_position.position)
        return rotor_position
    else:
        raise HTTPException(status_code=404, detail="Rotor not found.")


@router.get(
    "/encode",
    response_model=EncoderData,
    summary="Encode a character",
    description="Pass a character through the rotor to encode it.",
)
async def encode(rotor_index: int, character: str, direction: str) -> EncoderData:
    """Encode a character using a specific rotor."""
    if 0 <= rotor_index < len(rotors):
        rotor = rotors[rotor_index]
        parsed_direction = Direction(direction)
        return EncoderData(
            rotor_index=rotor_index,
            character=rotor.encode(character, parsed_direction),
            direction=parsed_direction,
        )
    else:
        raise HTTPException(status_code=404, detail="Rotor not found.")

@router.post(
    "/rotate",
    response_model=RotationResult,
    summary="Rotate the rotor",
    description="Change the position of the rotor to its next position. Returns true"
                "if the rotor passed a notch and should trigger the next rotor.",
)
async def rotate(instruction: RotationInstruction) -> RotationResult:
    """Rotate a specific rotor by a given number of positions."""
    if 0 <= instruction.rotor_index < len(rotors):
        rotor = rotors[instruction.rotor_index]
        return RotationResult(
            rotor_index=instruction.rotor_index,
            trigger_next=rotor.rotate(instruction.position_count),
            position=rotor.get_position(),
        )
    else:
        raise HTTPException(status_code=404, detail="Rotor not found.")