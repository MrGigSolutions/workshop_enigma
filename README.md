# Workshop mob programming
Create an Enigma machine

## About mob programming
### Benefits:
(https://www.techtarget.com/searchsoftwarequality/definition/mob-programming)
- **Enables continuous learning** - Everyone has total access to the shared knowledge of team members. Teams can quickly solve problems that come up, and team members [continuously learn](https://www.techtarget.com/whatis/definition/continuous-learning) more about the development process.
- **Ensures coding standards are met** - By having the navigator and mob review the code as the driver writes it, the team can make sure coding standards are met. Having another separate code review is not required. Best practices can also be reviewed in real time.
- **Overcomes individual weaknesses** - As development continues, the strengths and weaknesses of individual team members become more obvious. With shared access to knowledge, those team members can learn how to address those weaknesses.
- **Provides fast feedback** - Constant feedback can be given and discussed by mob members.
- **Enables continuous work** - If one team member is out of office, work can continue as planned.
- **Cultivates both hard and soft skills** - Not only do team members enhance their technical skills, but they also develop soft skills, like communication and time management abilities.

### How it works:
There are 3 roles in mob programming:
- The mob: a group of developers responsible for discussing the program and coming up with good ideas to improve it
- The navigator: listens to the mobs discussions, and communicates instructions to the driver. The navigator is the decision maker on where to go with the code.
- The driver: the driver converts the navigator's instructions into code. The driver shows NO initiative! He may only convert the instructions into code
For this session, we'll switch roles every 5 minutes (normally it's longer). The navigator becomes the driver. The driver becomes the mob.
- On switching, immediately drop what you are doing, even in the middle of writing something. Do not finish, the next driver will take over
- 5 minutes stat as soon as everyone has assumed their positions
- If there are more than 3 mob members in a group: switch 1 mob member to the next group this group can carry progress reports or instructions to the next group.

### For this session:
- We will use TDD: write a failing test and then fix it by implementing new functionality or correcting old functionality. Always start with a test!
- As a navigator, it can be tempting to undo the work that the previous navigator did, if it is not how you would do it.
  Try not to do this - explore what the other navigator was trying to before discarding it!

### To get started:
- Create a folder and `cd` into it
- Create a virtual environment with `python -m venv .venv`
- Activate the environment with `source .venv/bin/activate` (Linux) or `.\.venv\Scripts\activate` (Windows)
- Install copier: `pip install copier`
- Copy this template with `copier copy git+https://www.github.com/MrGigSolutions/workshop_enigma .`
- Follow the template instructions.
- Your team will have its own folder in which to play. Try to only work in your own folder,
  as the other teams will be working in theirs.
