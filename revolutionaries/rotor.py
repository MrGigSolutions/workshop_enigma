from operator import indexOf

ALL_LETTERS = {k for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ'"}

class Rotor():
    rotor_string: str
    connection_string: str
    notched_letters: set

    def __init__(self, rotor_string: str, connection_string: str):
        self.notched_letters = set()
        while "'" in rotor_string:
            notched_letter = rotor_string[rotor_string.index("'") - 1]
            rotor_string = rotor_string.replace(
                f"{notched_letter}'",
                notched_letter
            )
            self.notched_letters.add(notched_letter)
        letters = {l.upper() for l in rotor_string}
        if letters != ALL_LETTERS and len(rotor_string) != 26:
            raise ValueError("The rotor must have exactly 26 unique letters on its wheel.")

        letters = {l.upper() for l in connection_string}
        if letters != ALL_LETTERS and len(connection_string) != 26:
            raise ValueError("The rotor must connect every letter to every position.")

        self.rotor_string = rotor_string.upper()
        self.connection_string = connection_string.upper()

    def get_position(self) -> str:
        return self.rotor_string[0]

    def _encode_in(self, letter: str):
        index_of_letter = ord(letter) - 65
        return self.connection_string[index_of_letter: index_of_letter + 1]

    def _encode_out(self, letter: str):
        return chr(self.connection_string.index(letter) + 65)

    def encode_letter(self, letter: str, direction: int):
        return (self._encode_in, self._encode_out)[direction](letter)

    def _set_rotor_position(self, positions: int) -> bool:
        """Advances the rotor position by positions steps.
        Returns True if the current step contains a notch."""
        connections = ""
        # bqf...s -> pe...ra
        # a->b, b->q, c->f... ,z->s
        # z->a, a->p, b->e..., y->r
        for letter in self.connection_string:
            translated_letter = f"{chr((ord(letter) - 65 + 26 - positions) % 26 + 65)}"
            connections = f"{connections}{translated_letter}"
        self.connection_string = f"{connections[positions:]}{connections[0:positions]}"

        result = self.rotor_string[positions-1] in self.notched_letters
        self.rotor_string = f"{self.rotor_string[positions:]}{self.rotor_string[0:positions]}"
        return result

    def rotate(self) -> bool:
        return self._set_rotor_position(1)

    def set_position(self, letter):
        index = self.rotor_string.index(letter)
        self._set_rotor_position(index)