from typing import Callable
import pytest

from .keyboard import get_prompt, get_command, run
from plugs.plugs import Enigma
from rotor.rotor import Rotor


class TestKeyboard():

    prompts: list[str] = []
    commands: list[str] = []
    machine: Enigma = Enigma(
        plugs=[],
        reflector=['QM', 'WN', 'EB', 'RV', 'TC', 'YX', 'UZ', 'IA']
        + ['OS', 'PD', 'LF', 'KG', 'JH'],
        rotor1=Rotor(
            "QAZWSXEDCR'FVTGBYHNUJMIKOLP",
"WJAGOKCPEHLTXFBNIMVUYQZDRS"
        ),
        rotor2=Rotor(
            "HARGCNWVXSJFPYZODUIELT'KMQB",
            "EUPNJRTZGSXVBFKMALWDIHOCQY"
        ),
        rotor3=Rotor(
            "BFLHQZXRKGSNAU'JDTWYCOEVMPI",
            "TSRQXDZEUNMPHLYVBJIWCAGOFK"
        ),
    )

    def reset(self):
        self.prompts.clear()
        self.commands.clear()
        self.machine.reset()

    def add_to_prompt(self):
        def append_prompt(prompt: str):
            self.prompts.append(prompt)
        return append_prompt

    def add_to_commands(self):
        def append_command(command: str):
            self.commands.append(command)
        return append_command

    def simulate_command(self):
        def simulate_input(prompt: str) -> str:
            try:
                self.prompts.append(prompt)
                return self.commands.pop(0)
            except IndexError:
                return "q"

        return simulate_input

    def test_get_prompt(self):
        assert "Please enter your command > " == get_prompt()

    def test_get_command(self):
        assert "quitting" == get_command(
            None,
            self.simulate_command(),
        )
        assert "quitting" == get_command(
            None,
            self.simulate_command(),
        )
        self.commands = ["z"]
        self.prompts = []
        assert "invalid_command" == get_command(
            None,
            self.simulate_command(),
        )

    def _run_keyboard(self):
        run(
            self.machine,
            self.simulate_command(),
            self.add_to_prompt()
        )

    def assert_commands_and_prompts(self, commands: list[str], prompts: list[str]):
        self.reset()
        self.commands = commands
        self.prompts = []
        self._run_keyboard()
        assert not self.commands
        assert self.prompts == prompts

    def test_run(self):
        self.assert_commands_and_prompts(
            ["q"],
            ["Please enter your command > "]
        )

        self.assert_commands_and_prompts(
            [],
            ["Please enter your command > "]
        )

    def test_run_set_key(self):
        self.assert_commands_and_prompts(
            ["k","q"],
            [
                "Please enter your command > ",
                "Please enter a 3-letter key > "
            ]
        )
        self.assert_commands_and_prompts(
            ["k", "abc", "q"],
            [
                "Please enter your command > ",
                "Please enter a 3-letter key > ",
                'Set key "ABC".',
                "Please enter your command > ",
            ]
        )

    def test_run_list_plugs(self):
        self.assert_commands_and_prompts(
            ["l", "q"],
            [
                "Please enter your command > ",
                "Current plug state: []",
                "Please enter your command > ",
            ]
        )
        self.assert_commands_and_prompts(
            ["p", "ab", "l"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'Added plug "AB"',
                "Please enter your command > ",
                "Current plug state: [AB]",
                "Please enter your command > ",
            ]
        )

    def test_run_add_plugs(self):
        self.assert_commands_and_prompts(
            ["p", "q"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
            ]
        )
        self.assert_commands_and_prompts(
            ["p", "q"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
            ]
        )
        self.assert_commands_and_prompts(
            ["p", "ab", "q"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'Added plug "AB"',
                "Please enter your command > ",
            ]
        )
        self.assert_commands_and_prompts(
            ["p", "ab", "p", "ab", "q"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'Added plug "AB"',
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'The letters "A" and "B" are already plugged.',
                "Please enter your command > ",
            ]
        )
        self.assert_commands_and_prompts(
            ["p", "ab", "p", "bc", "q"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'Added plug "AB"',
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'The letters "B" are already plugged.',
                "Please enter your command > ",
            ]
        )

    def test_run_clear_plugs(self):
        self.assert_commands_and_prompts(
            ["r", "q"],
            [
                "Please enter your command > ",
                "Current plug state: []",
                "Please enter your command > ",
            ]
        )
        self.assert_commands_and_prompts(
            ["p", "ab", "r", "q"],
            [
                "Please enter your command > ",
                "Please enter a 2-letter plug combination > ",
                'Added plug "AB"',
                "Please enter your command > ",
                "Current plug state: []",
                "Please enter your command > ",
            ]
        )

    def test_encrypt_message(self):
        self.assert_commands_and_prompts(
            ["k", "zxy", "e", "hello"],
            [
                "Please enter your command > ",
                "Please enter a 3-letter key > ",
                'Set key "ZXY".',
                "Please enter your command > ",
                "Please enter the message to encrypt > ",
                "Encrypted message: ZXYWKKPL",
                "Please enter your command > ",
            ]
        )

    def test_decrypt_message(self):
        self.assert_commands_and_prompts(
            ["d", "zxywkkpl"],
            [
                "Please enter your command > ",
                "Please enter the message to decrypt > ",
                "Decrypted message: HELLO",
                "Please enter your command > ",
            ]
        )