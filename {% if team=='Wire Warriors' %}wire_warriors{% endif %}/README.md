## The Wire Warriors

You will be building the body and internal structure of the ENIGMA machine.

> [!IMPORTANT]
> You will depend heavily on the progress of the Revolutionaries. Make sure to communicate with them on their progress of the implementation the `Encode` endpoint, `Rotate` endpoint and `Position` endpoints.
> 
> If they are there, the Keyboard Clan will depend on your implementations of the `Encrypt`, `Decrypt` and `Key` endpoints, so make sure to communicate your progress clearly. They may need some of these endpoints before you can finish them, so provide reasonable defaults and endpoint skeletons!

### Main tasks

1. Create an API. Endpoints for it will be developed in later instructions.

> [!IMPORTANT]
> The API should be accessible by other groups, so make sure you are listening to IPs other than own host, and that the firewall allows access to your API. You should probably not use a work laptop for this exercise.

> [!NOTE]
> You may hardcode any initialisation values, and will typically not be required to allow the user to change machine settings other than the key.

2. Create an `Enigma` object. It should be initialised with a `reflector` variable, consisting of an array of 13 pairs of unique letters. Every letter in the alphabet occurs exactly once in the reflector array.

3. Implement a `_reflect(input: str) -> str` function. This function takes an input character, and returns the other character in the pair in the reflection array.

> [!NOTE]
> A reflector is a symmetrical static encoder. For example, if it consists of the array `["AB", "CD", ...]`, the reflector would reflect `A` as `B`, and `B` as `A`.

4. Write an HTTP client that can get JSON data from the Rotor API.

5. Create a `Key` GET endpoint. You can get the key by calling the `Position` GET endpoint on the rotor. `Position` returns a single letter representing the rotor's current position. The key is the combination of the position of all the rotors.

> [!NOTE]
> Discuss with the Revolutionaries what their implementation of the `Position` GET endpoint is, so you know what to expect.

6. Create a POST endpoint called `Encrypt`. It should take the following JSON input: `{"message": str}` and should do the following:
	1. Retrieve the current key and save it for output
	2. Call the Revolutionaries' `Encode` endpoint for each letter in the message through the 3 rotors in the "in" direction, passing the output of each rotor as the input for the next one , then pass the result through the `_reflect` function, then encode the message through the 3 rotors *in reverse order* in the "out" direction.
	3. Prepend the saved key in front of the encrypted message so that it becomes `[KEY][ENCODED MESSAGE]`, e.g. with key `ABC` and an encoded message `AXXGE`, return `ABCAXXGE`
	4. Return the message as a JSON: `{"message": str}`

> [!NOTE]
> The Rotor has an `Encode` GET endpoint, which encodes a single character in the provided direction. This should be implemented by the Revolutionaries. Encryption is a symmetrical process! Encrypting the letter `A` to `F`, for example, means that `F` also encrypts to `A`.

7. Create a POST endpoint called `Key`. This endpoint takes a JSON file `{"key": str}`, of which the key is a 3-letter string, and sets the rotor position for the 3 rotors in the Enigma. You can use the rotor's `Position` POST endpoint on each rotor to set its position to that letter. This `Position` endpoint will be implemented by the Revolutionaries.

8. Implement a `Decrypt` POST endpoint, which takes a JSON `{"message": str}`, and does the following:
	1. Take the 3 letter key and remove it from the front of the message. Set the Enigma machine key to this key.
	2. Decrypt each character using exactly the same procedure as above. As you can see it's symmetrical, so you can use the same function!
	3. Return the decrypted message as `{"message": str}`

9. Adjust the `Encrypt` and `Decrypt` endpoints so that they rotate the first rotor *after every* encoded letter using the rotor's `Rotate` endpoint. If the `Rotate` endpoint of the first rotor returns `trigger_next=True` the second rotor should also rotate. If the encode function of the second one returns True, the third one should rotate.
### Bonus tasks

7. Implement a `Plug` POST endpoint. It should take a JSON file like `{"plug": str}`, where plug should be a 2-letter string. Calling it adds a plug to the set of plugs (see info below), and needs to perform some validation:
	- the plugs may contain up to 13 pairs of letters
	- plug pairs on may only contain letters, no numbers or other characters
	- a letter may only occur once in any plug pair, either as the first or second letter of the pair
	If all of the above conditions are met, return True, otherwise False.
	
> [!NOTE]
> A plug is a connection that performs optional static encoding of letters before sending the signal through the machine.
> 
> **Example** if the letter `A` is plugged to `E`, and the user inputs an `A`, this then is first encoded to an `E`, then sent through the machine for encryption. Similarly, if the the user types an `E`, it's first encoded to an `A`. If a user typed an `F`, and it comes out of encryption as an `A` the plug would then also encode that to an `E` as the final output.

8. Implement a `Plug` DELETE endpoint that removes all plugs.

9. Create a `_plugged(letter: str)->str` that returns the plugged letter if one is available, and otherwise returns the same letter that was sent.

10. Adjust the `Encrypt` endpoint so that it calls the `_plugged` function before sending the signal into the first rotor, and again after signal comes out of the last rotor

11. Clean up your code! Write tests! Refactor and abstract! Make it GOOD!