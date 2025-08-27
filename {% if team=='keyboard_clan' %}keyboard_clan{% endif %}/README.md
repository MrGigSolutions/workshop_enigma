## The Keyboard Clan

You will be responsible for the machine's front end and UI.

>[!IMPORTANT] **Dependencies**
>You will depend heavily on the progress of the Wire Warriors. Make sure to communicate with them on their progress of the implementation  the `Key` endpoints, `Encrypt` endpoint and `Decrypt` endpoint. You may need these endpoints before they are ready to deliver them, so coordinate carefully.

> [!IMPORTANT] **State**
> You must not store any internal state of the ENIGMA machine. This is handled by the Wire Warriors. You may, however, store UI state, for example to remember that a user is currently encrypting a message, or is setting a key.
### Main tasks

1. Create a simple web page. The web page should for now contain a header with `ENIGMA` showing up.

> [!NOTE] **Init values**
> You may hardcode any initialisation values. It's beyond the scope of this UI to ask the user for input. See it as a machine setup - this was handled by an operator and had nothing to do with UI.

> [!TIP] Use Bootstrap
> Bootstrap can give you a very quick set of CSS classes to get a good looking starting site with minimal effort

2. Add a `Mode` button group to the website. The supported modes should be `Encrypt`, `Decrypt` and `Set Key`. The mode button should be highlighting to the user which mode is currently active.

3. Add an input and an output text field. The user should only be able to type code into the input text field. Also add a `Submit` button to the field. The output field will hold the result of the API when pressing the `Submit` button.

4. Implement showing the current Key of the Enigma machine. This key can be retrieved by calling get `machine/key` GET endpoint to retrieve the current key set in the machine. It should be visible for the user, either at all times, or at least when the machine is in `Encrypt` mode.

5. Implement `Set Key` mode. It should allow the user to type a 3-letter key (only capital letters), and when submitted should call the `machine/key` POST endpoint, implemented by the Wire Warriors. Refer to documentation provided by the Wire Warriors on how this is implemented.

6. Implement `Encrypt` mode. The user should type a message in only capitals (no numerics, lower case or special keys) and when submitted should call the `machine/encrypt` POST endpoint. Refer to documentation provided by the Wire Warriors on how this is implemented.

7. Implement `Decrypt` mode. This should allow the user to type in a message in the format above, e.g. `XYZGRVDC`, and should now output `HELLO`. Also, the key should now be set to to the machine key after decryption. The key changes after every encoded letter, and the final key state after decryption should now be visible. Call the Wire Warriors' `machine/decrypt` POST endpoint, and refer to their documentation.

### Bonus tasks

8. Add an extra mode, called `Plugs`. When the user selects this, they can enter 2-letter strings to add plugs to the machine. To do this, you can post the plug to the `/machine/plugs` POST endpoint.

> [!NOTE] **Plugs**
> A plug is a connection that performs optional static encoding of letters before sending the signal through the machine. A single letter may only ever be plugged once to a single other letter.
> 
> **Example** if the letter `A` is plugged to `E`, and the user inputs an `A`, this then is first encoded to an `E`, then sent through the machine for encryption. Similarly, if the the user types an `E`, it's first encoded to an `A`. If a user typed an `F`, and it comes out of encryption as an `A` the plug would then also encode that to an `E` as the final output.

9. Implement clearing the plugs by allowing the user to enter "-" in the input in plugs mode. In this case, you can call a DELETE endpoint: `/machine/plugs/clear`

10. Add validation to the user's input on steps 5-9. Think for example of not letting the user type spaces or numbers, limiting the size of the data entered, 

11. Clean up your code! Write tests! Refactor and abstract! Make it GOOD!