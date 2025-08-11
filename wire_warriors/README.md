## The Wire Warriors

You will be building the body and internal structure of the ENIGMA machine.

>[!WARNING]
>You will depend heavily on the progress of the Revolutionaries. Make sure to communicate with them on their progress of the implementation of the Rotor initializer, the `encode` method, `rotate` method, `get_position` method, and `set_position` method.
>
>If they are there, the Keyboard Clan will depend on your implementations of the `encrypt`, `decrypt` and `set_key` methods, so make sure to communicate your progress clearly. They may need some of these methods before you can finish them, so provide reasonable defaults and stubs!

### Main tasks

1. Create an `Enigma` object. It should be initialised with a `reflector` variable, consisting of an array of 13 pairs of unique letters. Every letter in the alphabet occurs exactly once in the reflector array.

2. Implement a `_reflect(input: str) -> str` function. This function takes an input character, and returns the other character in the pair in the reflection array.

> [!NOTE]
> A reflector is a symmetrical static encoder. For example, if it consists of the array `["AB", "CD", ...]`, the reflector would reflect `A` as `B`, and `B` as `A`.

3. Adjust the `Enigma` object to be initialised with 3 `Rotor` objects, implemented by the Revolutionaries. Check the initialiser of the `Rotor` to ensure you initialise it correctly.

> [!WARNING]
> The Rotor initializer may change as the Revolutionaries work, so make sure to find this out on time and initialize your Enigma object correctly.

4. Create a `get_key()` function. You can get the key by calling the `get_position()` function on each rotor. `get_position()` returns a single letter representing the rotor's current position. The key is the combination of the position of all the rotors.

5. Create a function called `encrypt(message: str)` that does the following:
	1. Call `get_key()` and save it for output.
	2. Encode each letter in the message through the 3 rotors in the "in" direction (the output of the first rotor becomes the input for the second rotor, etc), then pass the result through the `_reflect` function, then encode the message through the 3 rotors *in reverse order* in the "out" direction.
	3. Prepend the saved key in front of the encrypted message so that it becomes `[KEY][ENCODED MESSAGE]`
	4. Return the message 

> [!NOTE]
> The Rotor has an `encode(input: str, direction: str) -> str`, which encodes a single character in the provided direction. This should be implemented by the Revolutionaries. Encryption is a symmetrical process! Encrypting the letter `A` to `F`, for example, means that `F` also encrypts to `A`.

6. Create a `decrypt(message: str)` function that does the following:
	1. Take the 3 letter key and remove it from the front of the message. We will use this later.
	2. Decrypt each character using exactly the same procedure as above. As you can see it's symmetrical, so you can use the same function!
	3. Return the decrypted message

7. Adjust the `encrypt()` function so that it rotates the first rotor *after every* encoded letter using the rotor's `rotate()` function. If the `rotate()` function of the first rotor returns True, the second rotor should also rotate. If the encode function of the second one returns True, the third one should rotate.

8. Create a function called `set_key(key: str)`. This function sets the rotor position for the 3 rotors in the Enigma. You can use the function `set_position("X")` on each rotor to set its position to that letter. This `set_position("X")` function will be implemented by the Revolutionaries.

9. Adjust the `decrypt()` function to first call the `set_key(...)` function with the key consisting of the first 3 letters of the encrypted message
### Bonus tasks

7. Implement a `add_plug(plug: str) -> bool` function. This adds a plug to the set of plugs, and needs to perform some validation:
	- the plugs may contain up to 13 pairs of letters
	- plug pairs on may only contain letters, no numbers or other characters
	- a letter may only occur once in a plug pair, either as the first or second letter of the pair
	If all of the above conditions are met, return True, otherwise False.
	
> [!NOTE]
> A plug is a connection that performs optional static encoding of letters before sending the signal through the machine.
> 
> **Example** if the letter `A` is plugged to `E`, and the user inputs an `A`, this then is first encoded to an `E`, then sent through the machine for encryption. Similarly, if the the user types an `E`, it's first encoded to an `A`. If a user typed an `F`, and it comes out of encryption as an `A` the plug would then also encode that to an `E` as the final output.

8. Implement a `clear_plugs()` function that removes all plugs.

9. Create a `_plugged(letter: str)->str` that returns the plugged letter if one is available, and otherwise returns the same letter that was sent.

10. Adjust the `encrypt` function so that it calls the `_plugged` function before sending the signal into the first rotor, and again after signal comes out of the last rotor
