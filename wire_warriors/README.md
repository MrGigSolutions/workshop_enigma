## The Wire Warriors

An Enigma machine consists of the following parts:
- A keyboard with a light inside each key that causes that key to light up
  when it is the encoded version of the currently pressed key. E.g. pressing
  the "A" key could cause the "M" key to light up, signalling that that is the
  encoded letter of the letter typed by the operator.
- A plug board
- 3 rotors
- A reflector

A keyboard press causes an electrical signal to go through the set of plugs,
then into rotor 1, 2, then 3, then through the reflector, then back through
rotor 3, then 2, then 1, then back through the plug board, and finally back to
the keyboard to highlight the encoded letter.

Your job is to build the following parts of the machine:
- The reflector
- The internal wiring of the machine. You will connect all the different parts
  of the machine together.
- The plug board

The reflector does the following:
- For every letter in the alphabet, return another letter, so that there are 13
  pairs. Every letter must be connected to another letter and every letter may
  occur only once.
- When a letter goes into the reflector, its connected letter comes out, and
  when the connected letter goes into the reflector, the original letter comes
  out. e.g. if the reflector contains pairs `[AB, ...]`, `reflect("B")` should
  return `A`, and `reflect("A")` should return `B`

Plugs do the following:
- It symmetrically replaces an input letter by the letter it is connected to.
  E.g. if the letter `A` is plugged to the letter `P`, if a user types an A, it
  should be replaced by a `P` before going into the rest of the encoder,
  and after a signal has come through the encoder, if the result is a `P`,
  it should be output the letter `A`. The plug board is the first thing the 
  unencoded signal passes through, and the last thing the encoded passes through.
- It's possible to leave some letters unplugged. In this case the plug does
  nothing, and the letter stays as it is.

Your tasks are the following:
1. Create an `Enigma` object. For now the object will hold one variable:
   `reflector` (choose a variable type that can represent what the reflector
   does).
2. Implement the Enigma object's initialiser, so that it makes the following
   validations:
	- the reflector must contain 13 pairs of letters
	- there are only letters in the reflector pairs, no numbers or other
      characters
	- every letter in the alphabet occurs exactly once in the reflector, either
      as the first or second letter of a pair
3. Create a `get_key()` function. For now just let it return 3 letters. You can
   get the key using the Revolutionaries' `get_position()` function on each
   rotor. `get_position()` return a single letter representing the rotor's
   current position. The key is the combination of the position of all the
   rotors.
4. Create a function called `encrypt(message)` that does the following:
	1. Store machine's key setting.
	2. Encode each letter in the message through the 3 rotors in the "in"
       direction (the output of the first rotor becomes the input for the
       second rotor, etc), then pass the result through the `_reflect` function,
       then encode the message through the 3 rotors in reverse order in the
       "out" direction.
	3. Prepend the stored key in front of the encrypted message so that it
       becomes `[KEY][ENCODED MESSAGE]`
	4. Return the message
5. Create a `_reflect(letter)` function on `Enigma` that looks for a letter in
   `reflector` pairs, returns the other letter in the pair.
6. Adjust the `Enigma` object to be initialised with 3 `Rotor` objects. Check
   the initialiser of the rotor to ensure you initialise it correctly. This
   object should hold 3 `Rotor` objects (to be developed by the
   Revolutionaries).
7. Create a `decrypt(message)` function that does the following:
	1. Take the 3 letter key and remove it from the front of the message. We
       will use this later.
	2. Decrypt each character using exactly the same procedure as above. As you
       can see it's symmetrical, so you can use the same function!
	3. Return the decrypted message
8. Adjust the `encode()` function so that it rotates the first rotor after every
   encoded letter using the rotors `rotate()` function
9. Create a function called `set_key("XYZ")`. This function sets the rotor
   position for the 3 rotors in the Enigma. You can use the function
   `set_position("X")` on each rotor to set its position to that letter. This
   `set_position("X")` function will be implemented by the Revolutionaries.
   Also adjust the `decrypt()` function to first call the `set_key(...)`
   function with the key consisting of the first 3 letters of the encrypted
   message.
10. Add a `plugs` parameter, a list of 2-letter strings. Implement a `add_plug`
    function. This adds a plug to the set of plugs, and needs to perform some
    validation
	- the plugs may contain up to 13 pairs of letters
	- plug pairs on may only contain letters, no numbers or other characters
	- a letter may only occur once in a plug pair, either as the first or second letter of the pair
11. Implement a `clear_plugs` function that removes all plugs.
12. Create a `_plugged(letter)` that returns the plugged letter if one is
    available, and otherwise returns the same letter that was sent.
13. Adjust the encode function so that it calls the `_plugged` function before
    sending the signal into the first rotor, and to called the `_plugged`
    function again after signal comes out of the last rotor.
14. Optional: if the Revolutionaries have implemented notches (their step 7),
    the rotor will return a boolen value from its `rotate()` function. If this
    bool is true for the first rotor, also cause the second rotor to rotate.
    If that one also returns true, also cause the third rotator to rotate.
15. Optional: implement the `set_rotors(x, y, z)`, which calls `set_rotor(...)`
    on each of the rotors which is implemented by the Revolutionaries in their
    step 8.
