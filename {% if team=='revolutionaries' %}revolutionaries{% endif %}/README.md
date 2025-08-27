## The Revolutionaries

You will be implementing the rotor. The rotor is an essential component of the ENIGMA machine.

> [!IMPORTANT] **Dependencies**
> You are not dependent on the other groups, but the other groups will be very dependent on you! Make sure to align your progress and output with the other groups. Especially be aware that the Wire Warriors need (in this order) the `encode`, and `rotate`, `get_position` and `set_position` endpoints, so try to implement stubs with a good signature as soon as possible to accommodate them.

> [!TIP]
> The ENIGMA machine will work if the `rotate` and `set_position` endpoints do nothing. If you run out of time, leave it a stub, as you do not need to implement this yet. It will make your code much easier for Alan Turing to crack, but then again he had a few years to do it, not a few hours, and he invented computer science specifically to do it...
### Main tasks

To implement the rotor, you must do the following:

1. Create an API that supports submitting data using JSON objects. We'll add endpoints in the next steps. Don't worry about things like authentication, KISS.

>[!IMPORTANT]
>The API should be accessible by other groups, so make sure you are listening to IPs other than own host, and that the firewall allows access to your API. You should probably not use a work laptop for this exercise.

> [!NOTE] **Init values**
> You may hardcode any initialisation values, and will typically not be required to allow the user to change rotor settings other than the position.

2. Create a `Rotor` object. The `Rotor` object should be initialised with a **wiring string** of 26 unique letters A-Z.

> [!NOTE] **Wiring string**
>  Encoding letters to other letters can be represented as follows: `ABCDEF<->BDFACE`. This means letter `A` encodes to `B`, `B` to `D`, etc. A shorthand notation for this uses only a single string: `BDFACE`. The ***index*** of each letter in this string corresponds to the index of the letter in the alphabet for the input. The ***value*** of each letter corresponds to what that letter **encodes** to. We call this string the **wiring string**, as it represents the internal wiring of the rotor.
 
3. Instantiate 3 rotors for use within the API.

> [!NOTE] **Rotor state**
> You'll need to introduce state for this endpoint. The API should remember how many rotors there are. Use either a database, file, or some form of in-memory persistence. In later steps, additional details about the rotor need to be remembered.

4. Implement a `/rotor/position` GET endpoint. This takes a JSON object: `{"rotor_index": int}` and returns JSON object: `{ "rotor_index": int, "letter": str}`. The letter represents the number of rotation steps that have been made. Initialize each rotor at position `A`.

>[!NOTE] Positions
>**Example** The rotor initialises at position `A`. After rotating once (rotation will be introduced in a later step), the position becomes `B`, then `C`, etc. until eventually looping back to `A`.

5. Implement the `/rotor/encode` GET endpoint. It takes the following JSON object: `{ "rotor": int, "letter": str, "direction": str }`. This endpoint should encode a single character using the wiring string. It should return a JSON object with the format `{"encoded": str}` The direction of the encoding should also be supported (`in` or `out`). Use the wiring string to encode characters.

> [!NOTE] **Encoding**
> Encoding is a symmetrical process, so encoding can have an `in` and an `out` direction. 
> 
> **Example**: With wiring string `BDFACE`, "in-encoding" `A` becomes `B`, and "out-encoding" `B` becomes `A`. The wiring string `BDFACE` in the `in` direction can be read as `ABCDEF->BDFACE` and in the `out` direction it can be read as `ABCDEF<-BDFACE (= ABCDEF->DAEBFC)`.

6. Implement the `/rotor/rotate` POST endpoint. It takes the following JSON object: `{"rotor": int, "position_count": int}`, and returns: `{"rotor": int, "trigger_next": bool}` When a rotor rotates `n` positions, 2 operations happen to the encryption string:
   - `n` letters are popped from the end of the string and are then prepended to the string.
   - all the letters increase by `n` (it's a modulo operation, so after `Z` comes `A`) A.
   For now, this endpoint will return `trigger_next=True` when the current **encryption string** is the same as the **wiring string** (i.e. when the rotor has made a full rotation).

> [!NOTE] **Rotating**
> You'll need to create a new string called the **encryption string**. Rotations will cause this string to change. However, you need to have a way to remember the original settings as well, so that you can construct an encryption string for any rotor position.
> 
> **Example**: rotating `BDFACE` by 1 position results in: `BDFACE -> (pop & prepend 1) EBDFAC -> (increase by 1) FCEABD`. So after rotating, `A` now in-encodes to `F`, `B` to `C` etc.

6. Implement the `/rotor/position` POST endpoint. It takes a JSON object: `{"letter": str}`. It sets the rotor position by providing a letter. This should rotate the rotor from its original position. `{"letter": "B"}` indicates that the rotor should be rotated 1 position from its initial setting, regardless of its current state.

### Bonus tasks

6. Implement adding notches to the rotor at positions in the **wiring string**. When a rotor rotates past a letter with a notch, it indicates to the machine that the *next* rotor also needs to rotate by having the `rotate` endpoint return `{"trigger_next": True}` when the rotor passes a notch.
   - Ensure that the `Rotate` and `Position` endpoints all play nice with the notches.

> [!NOTE] **Notches**
> Each rotor typically has 1 or 2 notches. When a rotor passes a notch by being rotated, it will trigger the next rotor to also rotate. A good way to indicate the notch is to use an apostrophe in the wiring string, e.g. `ABC'DEF`. It's up to you to determine whether the apostrophe refers to the letter before it or after it. You may of course also use other methods to remember where the notches are.

7. Add a string of 26 unique letters, called the **rotor string**. Adjust `Position` POST to look up the input letter in this string, and set the position based on that. Also adjust the `Position` GET endpoint to correctly return the letter from the rotor string that represents the current position of the rotor.

> [!NOTE] **Rotor strings**
> In real ENIGMA, setting the positions of the rotors to A-Z without encryption would have been too easy to crack. They had different rotors, and these rotors would be overlaid with a set of letters. In the code book, the correct rotor and overlay settings would be stored.
> 
> **Example**: given a **rotor string** of `BADC`, and a **wiring string** of `CBDA`, `Position` GET for the initial position of the rotor should return `B` (index 0 of the rotor string).  `Position` POST`{"letter": "D"}` (rotor string index 2), would cause us to rotate the rotor 2 positions from its initial setting, resulting in an **encryption string** of `BCAD`.

8. Clean up your code! Write tests! Refactor and abstract! Make it GOOD!
