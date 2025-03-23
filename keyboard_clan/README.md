## The Keyboard Clan
You will be responsible for the machine's front end and UI. To this end,
you'll do the following tasks:
1. Write a command prompt utility. The user should be given a welcome message,
   and allow the user to type the letter Q to quit.
2. If the user types in a wrong/unknown command, the utility should give the
   user feedback, and allow the user to try again.
3. Add an E option (for encrypt). Only letters A-Z should be allowed. On
   success, the prompt should return the "encrypted" message:
   `[KEY][MESSAGE]` (without the brackets). E.g. key `XYZ`, message `HELLO`
   should return `XYZHELLO`
4. Add a D option for (decrypt). This should allow the user to type in a
   message in the format above, e.g. `XYZHELLO`, and should now output `HELLO`.
   Also, the key should now be set to `XYZ`
5. Add a K option (for "set key"). This should be followed by a prompt for the
   user to type in a 3 letter key. Only letters A-Z are allowed, and the key
   must be exactly 3 letters. If the user does it wrong, let them try again.
   But also allow the user a way to exit this option, e.g. by escape or typing
   only a Q. Confirm the output to the user.
6. Add an L option (for listing plugs). If the user enters this command, the
   output should be a list of letter pairs, e.g. `["AB", "CD", "EF"]`. The list
   should be empty when called the first time. but we'll populate it in the next
   step. The plugs are reflected in the `plugs` list in the `Enigma` object, and
   will be one of the first things implemented by The Wire Warriors.
7. Add a P option (for adding plugs). Entering this option should allow the user
   to add a letter pair to the plug list. Requirements: every letter may only
   occur once in the list (whether first or second in the pair). There may only
   be pairs of letters, not 3, or 1. Give the user some feedback whether the
   plug was added successfully.
8. Add an R option (for remove plugs). This will clear the combinations from the
   list and should display a list.
9. Optional: Add an S option for setting the position of the rotors. The input
   should be 3 indexes from 1-26, separated by commas, and these represent the
   positions of the rotors. For each entered value, convert the entered value
   to an integer between 1 and 26, and call the `set_rotors(x, y, z)` with each
   of the values.
10. Optional: make it more user friendly! Implement a help function, show the
    current key before any prompt.

**Dependencies**
- After the Wire Warriors have finished their step 1, change your step 1 to
  instantiate a new Enigma object when the application starts.
- After the  Wire Warriors have finished their step 2, change your step 2 code
  to call their `set_key(...)` with the letters the user has entered.
- After The Wire Warriors have finished their step 5, change the Encrypt
  feature of Step 6 to use their `encrypt(message)` function.
- After The Wire Warriors have finished their step 6, change the Decrypt
  feature of Step 7 to use their `decrypt(message)` function
