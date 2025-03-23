## The Revolutionaries

You will be implementing the Enigma machine's rotor. The rotor will work as follows:
- The rotor consists of a wheel with internal wiring connecting 26
  **input signals** to 26 **output signals**. The wiring can be represented by a
  string, which we will designate the **connection string**, where the input letter is
  represented by the position of the output letter the string.
  A simplified connection string with 5 letters could look like this:
  `BDEAC`, this can be read as:
  *Input A encodes to output B, B to D, C to E, D to A, E to C*.
  Encoding can work in both directions, so a letter connected to the **output** `B`
  should result in the **input** being `A`
- When a rotor rotates, the wiring of the rotor changes. The input AND the
  output both move 1 letter "down", so if `E` connected to `C`, rotating will instead cause
  `D` to be connected to `B`. Moving the **input** 1 letter down is
  represented by shifting the string so that its second letter becomes its first letter.
  In above example, we could shift `BDEAC` 1 letter to become `DEACB`. However, the
  output also needs to shift. So this we can do by lowering each letter in the string
  by 1 letter, i.e. `B` becomes `A`, etc. So now the string becomes `CDEBA`.
  The result of these changes is that input `A` is now connected to output `C`, etc.
- To set the position of a rotor, each rotor is represented by a string of letters in
  random order, which we'll call the **rotor string**. . As a simplified example, 
  we can apply the letters `ABCDE` to the rotor. The first letter of this rotor string is 
  always visible on the operator's keyboard, and can be used to set the position of 
  the rotor. We can now use this setting to describe a rotor by its rotor string and 
  connection string, for example: `ABCDE BDEAC`
- To represent how the rotor string changes when rotating the rotor, the first letter 
- is removed from the front of the rotor string,
  and is then put at the back of the string, so rotating a rotor with rotor string
  `ABCDE` will result in the rotor string being `BCDEA`, meaning that the `B` will now
  be visible to the user.
  So rotating `ABCDE BDEAC` by 1 position will result in `BCDEA DEACB`. Manually
  setting the rotor to position `A` will now ensure that the rotor is back in the
  starting position: `ABCDE BDEAC`.
- The "rotor setting" is a 1-based index that determines the first letter in the
  rotor string. For example, if we were to use a rotor setting of 2 in the rotor from
  example above, we would shift the rotor string `ABCDE` by 1 position during setup, 
  so the rotor would now be represented by `BCDEA EDABC`. As this is the same rotor 
  as in the example above, while the `B` is visible to the user in rotr position 2, the
  internal wiring is the same as if the rotor was set to an `A` with rotor position 1.
- An Enigma machine consists of at least 3 rotors. After a letter has been encoded,
  the first rotor will rotate 1 position, changing its wiring positions. Each rotor 
  also has a 1 or 2 notches. When a rotor passes a notch by being rotated,
  it will trigger the next rotor to also rotate. Notches could be represented by an
  apostrophe in the rotor string: `ABC'DE BDEAC`

To implement the rotor, you must do the following:
1. Create a `Rotor` object. The `Rotor` object should be initialised with a
   **rotor string** and a **connection string**.
2. Implement a validation on the initialisation function:
	- There should be 26 unique alphabetic letters in the rotor string,
	- There should be 26 unique alphabetic letters in the connection string
3. Implement getting the current position of the rotor by its visible letter:
   `get_position() -> str`
4. Implement the `encode(message: str) -> str` function: encodes a single 
   character based on the current rotor settings. The direction of the encoding
   should also be supported. E.g. given rotor connections `BDEAC`, encoding 
   "inward" (i.e. input to output) would encode `A` to `B`: 
   `assert encode("A", direction="in") == "B"`, similarly, encoding
   "outward" (i.e. output to input) should encode `B` back to
   `A`: `assert encode("B", direction="out") == "A"` but of course
   `assert == encode("B", direction="in") == "D"`
5. Implement the `rotate() -> None` function: Imagine that a rotor has a connection that
   connects input `A` to input `C` and input `B` to `F` (`CF...`). Rotating it by 1 step
   would cause that connection to shift 1 place, so now it would connect `Z` to `B`, and
   `A` to `E` (`E...B`). This rotation can therefore be simulated by performing 2
   operations:
   1. On the **connection string** only: decrease each letter to its previous letter.
      E.g. if the connection string is `BDEAC` (modulo 26), it should now become
      `ACDEB`
   2. On **both** the **rotor string** and the **connection string**: remove the first
      letter and append it to the end of the string. e.g. `ABCDE` becomes `BCDEA`
      `rotate()` called on a rotor `ABCDE ABCDE`, on step 1 would become `ABCDE EABCD`,
      and on step 2 would become `BCDEA ABCDE`. This is of course a bad example,
      because a connection string `ABCDE` doesn't actually translate anything. A better
      example would be that `ABCDE BDCAE` would similarly transform to `ABCDE ACBED`,
      then `BCDEA CBEDA`.
6. Implement the `set_position(letter)` function. Set the rotor position by providing
   a letter: `set_position("A")`. This should rotate the rotor to the position where
   the indicated letter is the first one in its rotor string. For example: `ABCDE BDEAC`
   has position `A`. Rotating it to position `C` would result in: `CDEAB EDABC`.
   Ensure to deal gracefully with edge cases, such as setting the position to a
   position it is already in, or setting it to the last character in the rotor string.
7. Optional: implement notches. When a rotor rotates past a letter with a notch,
   indicate to the machine that the *next* rotor also needs to rotate by making the
   result of the `rotate` a boolean. Each rotor has 1 or more notches. A notch could be
   implemented by applying an apostrophe after the notched letter, e.g. `ABC'DEF`.
   Ensure that the `rotate`, `set_position` and `set_rotors` functions all play nice
   with the notches (a notch should never be the first character in the rotor string)!
   Update your unit tests. Also, update the `rotate()` function to return True if the
   next rotor should rotate, and False otherwise. Hint: it may be
   easier to store and manipulate the rotor strings without the notches, and keep
   track of the notches separately.
8. Optional: enter rotor setting. Pass a 1-based integer that sets the position of the
   rotor string over the rotor as was explained above in the bullet point about the
   rotor setting. Naturally changing the rotor setting without rotating the rotor
   should cause a different letter indicating the current position of the rotor to be
   visible. `set_rotor(13)`.


**Dependencies**
You are not dependent on the other groups, but the other groups will be very dependent
on you! Make sure to align your progress and output with the other groups. Especially
be aware that the Wire Warriors need (in this order) your implementation of
instantiating new `Rotor` objects, and the `encode()`, and `rotate()` and
`set_position()` functions, so try to implement stubs with a good signature as soon as
possible to accomodate them.
Hint: the `Enigma` machine will work if the `rotate()` and `set_position()` functions
do nothing. If you run out of time, leave it a stub, as you do not need to implement
this yet.
It will make your code much easier for Alan Turing to crack, but then again he had a
few years to do it, not a few hours, and he invented the computer specifically to do
it...
