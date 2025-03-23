
from random import randint
from wire_warriors.machine import Enigma
from revolutionaries.rotor import Rotor

def generate_random_string():
    letters_string = [k for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for r in range(25, 0, -1):
        n = randint(0, r-1)
        letter = letters_string[n]
        letters_string[n] = letters_string[r]
        letters_string[r] = letter
    return "".join(letters_string)

def combine_random_strings(string1: str, string2: str) -> list[str]:
    result = []
    for k1, k2 in zip(string1, string2):
        result.append(f"{k1}{k2}")
    return result

def test_machine():
    enigma = Enigma(
        plugs=[],
        reflector=['QM', 'WN', 'EB', 'RV', 'TC', 'YX', 'UZ', 'IA']
        + ['OS', 'PD', 'LF', 'KG', 'JH'],
        rotor1=Rotor(
            "QAZWSXEDCRFVTGBYHNUJMIKOLP",
            "WJAGOKCPEHLTXFBNIMVUYQZDRS"
        ),
        rotor2=Rotor(
            "HARGCNWVXSJFPYZODUIELTKMQB",
            "EUPNJRTZGSXVBFKMALWDIHOCQY"
        ),
        rotor3=Rotor(
            "BFLHQZXRKGSNAUJDTWYCOEVMPI",
            "TSRQXDZEUNMPHLYVBJIWCAGOFK"
        ),
    )

    enigma.rotors[0].set_position("Q")
    assert enigma.rotors[0].rotor_string == "QAZWSXEDCRFVTGBYHNUJMIKOLP"
    assert enigma.encode("H") == "QHBN"
    assert enigma.decode("QHBN") == "H"
    assert enigma.decode(enigma.encode("HELLO")) == "HELLO"
