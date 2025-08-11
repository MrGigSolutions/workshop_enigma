## The Keyboard Clan

You will be responsible for the machine's front end and UI.

>[!IMPORTANT]
>You will depend heavily on the progress of the Wire Warriors. Make sure to communicate with them on their progress of the implementation of the Enigma initializer, the `get_key` method, `encrypt` method, and `set_key` method. You may need these methods before they are ready to deliver them, so coordinate carefully.
### Main tasks

1. Write a command prompt utility. The user should be given a welcome message, and allow the user to type the letter `Q` to quit.

> [!NOTE]
> It's not very easy to test command prompts. You could consider creating an object that has methods for each command. A good way to do this is to pass the command and the current state into such a method, have the command do something to the state, and then return the state.

2. Implement that if a user gives a wrong command, the application shows an Invalid command message, and then returns to the initial prompt.

3. Instantiate an `Enigma` object in the utility. Follow the correct init method provided by the Wire Warriors.

> [!NOTE]
> You may hardcode any initialisation values. It's beyond the scope of this UI to ask the user for input. See it as a machine setup - this was handled by an operator and had nothing to do with UI.

4. Add an `E` option (for encrypt). The user should be able to follow this command with a message. Only letters `A-Z` should be allowed. On success, the prompt should return the "encrypted" message: `[KEY][MESSAGE]` (without the brackets). E.g. key `XYZ`, message `HELLO` could return `XYZXDRQD. You may get the encrypted message by calling the `encrypt(message)` method on the `Enigma` object.

5. Add a D option (for decrypt). This should allow the user to type in a message in the format above, e.g. `XYZHELLO`, and should now output `HELLO`. Also, the key should now be set to `XYZ`. The method to use for this is the `decrypt(message)` method.

6. Add a K option (for "set key"). This should be followed by a prompt for the user to type in a 3 letter key. Only letters A-Z are allowed, and the key must be exactly 3 letters. You can call the `set_key(key: str)` function on the `Enigma` object for this.

> [!WARNING]
> You must not store any internal state of the ENIGMA machine. This is handled by the Wire Warriors. You may, however, store UI state, for example to remember that a user is currently encrypting a message, or is setting a key.

### Bonus tasks

7. Add an L option (for listing plugs). If the user enters this command, the output should be a list of letter pairs, e.g. `["AB", "CD", "EF"]`. The list should be empty when called the first time. but we'll populate it in the next step. The plugs are reflected in the `plugs` list in the `Enigma` object, and will be one of the first things implemented by The Wire Warriors. You can access this by accessing the `plugs` property on the Enigma object.

8. Add a P option (for adding plugs). Entering this option should allow the user to add a letter pair to the plug list. Requirements: every letter may only occur once in the entire list (whether first or second in the pair). There may only be pairs of letters, not 3, or 1. Give the user some feedback whether the plug was added successfully. The Enigma will have an `add_plug(plug: str)` function for this.

9. Add an R option (for remove plugs). This will clear the combinations from the list and should display a list. You can call the `clear_plugs()` function on the Enigma object for this.

10. Add validation to the user's input on steps 6 (no more than 3 letters, etc) and 7. You can use the result of the `add_plug()` function for the latter (returns True if the plug was added, False otherwise)

