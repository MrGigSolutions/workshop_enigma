from rotor.rotor import Rotor

class Enigma:

    plugs: list[str] = []
    reflector: list[str] = []
    rotors: list[Rotor] = []

    def __init__(
        self,
        plugs: list[str],
        reflector: list[str],
        rotor1: Rotor,
        rotor2: Rotor,
        rotor3: Rotor
    ):
        self.plugs = plugs
        self.reflector = reflector
        self.rotors = [rotor1, rotor2, rotor3]

    def reset(self):
        self.plugs = []

    def _reflected(self, letter: str, reflections: list[str]):
        for reflection in reflections:
            if letter in reflection:
                return reflection[1] if letter == reflection[0] else reflection[0]
        return letter

    def plugged(self, letter: str):
        return self._reflected(letter, self.plugs)

    def reflect(self, letter: str):
        return self._reflected(letter, self.reflector)

    def _update_rotations(self):
        for rotor in self.rotors:
            if not rotor.rotate():
                break

    def _pass_through_machine(self, letter: str) -> str:
        letter = self.plugged(letter)
        for rotor in self.rotors:
            letter = rotor.encode_letter(letter, 0)
        letter = self.reflect(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.encode_letter(letter, 1)

        letter = self.plugged(letter)
        self._update_rotations()

        return letter

    def get_key(self):
        return ''.join(
            [r.get_position() for r in self.rotors]
        )

    def encode(self, message):
        result = []
        key = self.get_key()
        for letter in message:
            result.append(self._pass_through_machine(letter))
        return f"{key}{''.join(result)}"

    def set_key(self, key: str):
        for i, k in enumerate(key):
            self.rotors[i].set_position(k)

    def decode(self, message):
        self.set_key(message[:3])
        message = message[3:]
        result = []
        for letter in message:
            result.append(self._pass_through_machine(letter))
        return "".join(result)