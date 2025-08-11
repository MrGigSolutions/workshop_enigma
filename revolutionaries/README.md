## The Revolutionaries

You will be implementing the rotor. The rotor is an essential component of the ENIGMA machine.

> [!IMPORTANT]
> You are not dependent on the other groups, but the other groups will be very dependent on you! Make sure to align your progress and output with the other groups. Especially be aware that the Wire Warriors need (in this order) your implementation of instantiating new `Rotor` objects, and the `encode()`, and `rotate()`, `get_position()` and `set_position()` functions, so try to implement stubs with a good signature as soon as possible to accommodate them.

> [!TIP]
> The ENIGMA machine will work if the `rotate()` and `set_position()` functions do nothing. If you run out of time, leave it a stub, as you do not need to implement this yet. It will make your code much easier for Alan Turing to crack, but then again he had a few years to do it, not a few hours, and he invented the computer specifically to do it...

### Main tasks

To implement the rotor, you must do the following:

1. Create a `Rotor` object. The `Rotor` object should be initialised with a **wiring string** of 26 unique letters A-Z.

> [!NOTE]
> Encoding letters to other letters can be represented as follows: `ABCDEF->BDFACE`. This means letter `A` encodes to `B`, `B` to `D`, etc. A shorthand notation for this uses only a single string: `BDFACE`. The ***index*** of each letter in this string corresponds to the index of the letter in the alphabet for the input. The ***value*** of each letter corresponds to what that letter **encodes** to. We call this string the **wiring string**, as it represents the internal wiring of the rotor.
 
2. Implement the `encode(input: str, direction: str) -> str` function: this encodes a single character based on the current rotor settings. The direction of the encoding should also be supported (`in` or `out`). We use the wiring string to encode characters.

> [!NOTE]
> Encoding is a symmetrical process, so encoding can have an `in` and an `out` direction. For example, with encryption string `BDFACE`, "in-encoding" `A` becomes `B`, and "out-encoding" `B` becomes `A`. The whole encryption string `BDFACE` in the "in" direction can be read as `ABCDEF->BDFACE` and in the "out" direction it can be read as `ABCDEF->DAEBFC`

3. Implement the `rotate(count: int) -> bool` function. When a rotor rotates `n` positions, 2 operations happen to the encryption string. **Firstly**: `n` letters are popped from the end of the string and are then prepended to the string. **Secondly**: all the letters increase by `n` (it's a modulo operation, so after `Z` comes `A`) A. For now, this function will always return `False`, except when the current state of the rotor matches the initial state (i.e. when the rotor has made a full rotation).

> [!NOTE]
> You'll need to introduce state for this function. You could do this by introducing a new string: the current wiring of the rotor. This string will be called the **encryption string**. In a real ENIGMA machine, the rotors consisted of inputs and outputs connected by wiring. Rotating the rotor caused both the input and output to shift one letter, which is represented by the 2 operations explained in the implementation above. However, you need to have a way to remember the original settings as well, which is why you should separate the current and original settings.
> 
> **Example**: rotating `BDFACE` by 1 position results in: `BDFACE -> (pop & prepend 1) EBDFAC -> (increase by 1) FCEABD`. So after rotating, `A` now in-encodes to `F`, `B` to `C` etc.

 4. Implement the `get_position() -> str` function. This returns a letter that represents the number of rotation steps that have been made. For example, the rotor initialises at position `A`. After a 1-letter rotation, the position becomes `B`, then `C`, etc.

> [!NOTE]
> In a real ENIGMA machine, the state of the machine was indicated by highlighting a letter for each rotor. This could be used to get and set rotor positions.

5. Implement the `set_position(position: str)` function. Set the rotor position by providing a letter: `set_position("A")`. This should rotate the rotor so that it is in its original position. `set_position("B")` should rotate it by 1 from its original, etc.

> [!NOTE]
> An ENIGMA machine only supports input letters A-Z, so this is why we need to use this rather convoluted way to set the rotor position.

### Bonus tasks

6. Implement adding 1 or 2 notches to the rotor at positions in the wiring string. When a rotor rotates past a letter with a notch, indicate to the machine that the *next* rotor also needs to rotate by having the `rotate` function return True when the rotor passes a notch.
   - Ensure that the `rotate`, `set_position` and `set_position` functions all play nice with the notches.
   - The `rotate` function should now return `True` when passing a notch, to indicate that a notch was just passed.

> [!NOTE]
> Each typically rotor has 1 or 2 notches. When a rotor passes a notch by being rotated, it will trigger the next rotor to also rotate. A good way to indicate the notch is to use an apostrophe in the wiring string, e.g. `ABC'DEF`. It's up to you to determine whether the apostrophe refers to the letter before it or after it. You may of course also use other methods to remember where the notches are.

7. Encrypt the positions string. Implement this by storing a string of 26 unique letters, called the **rotor string**. Implement setting this by creating a adding a second string to the Rotor initialiser. Adjust `set_position()` to look up the input letter in this string, and set the position based on that. Also adjust the `get_position`() function to correctly return the letter from the rotor string that represents the current position of the rotor.

> [!NOTE]
> In real ENIGMA, setting the positions of the rotors to A-Z without encryption would have been too easy to crack. They had different rotor types, each overlaid with a set of letters that could be rotated over the rotor. In the code book, the correct rotor and overlay settings would be stored.
> 
> **Example**: given a rotor string of `BADC`, and a wiring string of `CBDA`, `get_position()` for the initial position of the rotor should return `B` (the first letter in the rotor string).  Setting the rotor to position `A` (the second letter in the rotor string), would cause us to rotate the rotor once from its initial setting, resulting in an encryption string of `BDCA`
