# Workshop mob programming
Create an Enigma machine

### Announcement
It's the early 20th century. You and your team are in a unique situation. An English spy has convinced the German Army that they have plans for an unbreakable code machine. Only problem is: the English don't have those plans. Your team has been asked to do the almost impossible: design an encryption machine that is *almost* unbreakable but will convince the Germans they have a fool proof system. You will have opportunity to design the world's most famous encryption apparatus - ENIGMA - with all the modern tools that are available today. Can you and your fellow teams do in 2 hours what the Germans did in 20 years?

For this assignment, you will be split up in multiple teams that have to work together to come up with a solution. Each team will use mob programming to come up with a solution for their parts. Extra challenges come from the need for coordination.

## About mob programming
Mob Programming, also known as Team or Ensemble Programming, is an innovative practice where a group of software engineers works collaboratively on the same task, at the same time, in the same space, and on a single computer. This approach fosters teamwork, facilitates knowledge sharing, and produces high-quality code while promoting a deeper understanding of the project.

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

For this session, we'll switch roles every 10 minutes (normally it's longer). The navigator becomes the driver. The driver becomes the mob.
- On switching, immediately drop what you are doing, even in the middle of writing something. Do not finish, the next driver will take over
- 10 minutes start as soon as everyone has assumed their positions

### For this session:
- You'll need to start by setting up an API - make sure other teams can get to yours. Check firewall settings etc.
- It's useful to have good knowledge of the language your group uses. Pick a group that works in a language you are a bit familiar with. We have a lot of ground to cover!
- You'll be rotating in slightly longer shifts than earlier exercises - 10 minutes each. Suggestion: start with more experienced navigators and pilots, to get the project up asap.
- As a navigator, it can be tempting to undo the work that the previous navigator did, if it is not how you would do it. Try not to do this - explore what the other navigator was trying to before discarding it
- There is a lot of reading involved. It may be an idea to have at least one of the mob read any additional text for the assignment, so you know what is expected.
- You will NOT be allowed to communicate with other teams, other than sending a message through the moderators now and then. You will want to think carefully about documenting your APIs so that the other teams are clear on how to use them!
- We'll hold a 5-minute break after the first round, in which you are allowed to discuss your progress and how to better exchange designs and information. This is the only time you can speak to the other teams
- Opposed to many of the earlier katas, you will NOT be required to write unit tests. You may want to for your own team, but for this kata, the result, and the process is more important.
- You are NOT in a competition with the other teams. You are all working together to create a solution. You'll all be working on complex problems, and other teams may not be able to quickly respond to your questions. Allow for this! You are trying to win a war!

### To get started in Python:
- Create a folder and `cd` into it
- Create a virtual environment with `python -m venv .venv`
- Activate the environment with `source .venv/bin/activate` (Linux) or `.\.venv\Scripts\activate` (Windows)
- Install copier: `pip install copier`
- Copy this template with `copier copy git+https://www.github.com/MrGigSolutions/workshop_enigma .`
  On Windows, if you run in a bash shell, you may need to call
 `winpty copier copy git+https://www.github.com/MrGigSolutions/workshop_enigma .`- Follow the template instructions.
- Your team will have its own folder in which to play. Try to only work in your own folder,
  as the other teams will be working in theirs.
