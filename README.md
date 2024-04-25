## AdventureKit: A Python Text Adventure Framework

AdventureKit is a Python framework designed to simplify the creation of text-based adventure games. Whether you're a novice developer looking to create your first interactive story or an experienced programmer seeking to streamline the process, AdventureKit offers an intuitive solution.

### Features:

- **Interactive Storytelling**: AdventureKit provides a straightforward approach to crafting engaging narratives through text-based interactions.
- **Yes or No Questions**: Easily incorporate decision points into your story with yes or no queries.
- **Multi-choice Questions**: Offer players multiple options to choose from, enhancing interactivity.
- **Text-based Input**: Allow players to input text, enabling more complex interactions and puzzles.
- **Room System**: Organize your game into distinct areas or rooms, maintaining clarity and structure in your code.
- **Player Stats Management**: Keep track of player progress and attributes with built-in stat management functionality.

### How to Use AdventureKit:

AdventureKit follows a simple structure, allowing developers to focus on crafting compelling stories rather than wrestling with complex code. Here's a brief overview of how to get started:

1. **Initialize Your Adventure**: Begin by importing the AdventureKit library and creating an instance of `TextAdventure()`.

2. **Define Paths**: Use decorators to define different paths within your adventure. Each path represents a distinct segment of your story.

3. **Craft Your Narrative**: Within each path, use the `adventure.say()` function to deliver narrative text to the player. Incorporate questions and choices using the provided functions such as `adventure.question.bool()` and `adventure.question.multiChoice()`.

4. **Navigate Through Paths**: Utilize `adventure.gotoPath()` to move between different paths based on player choices or story progression.

5. **Enhance Interactivity**: Experiment with additional features like wait times, keyboard input detection, and player stat manipulation to create dynamic and immersive experiences.

### Example Usage:

The provided code snippet offers a simple example of AdventureKit in action.

```py
from pyventurelib import TextAdventure


adventure = TextAdventure()

@adventure.path("start")
def start():
    adventure.say("This is an example project for AdventureKit.")
    choice = adventure.question.multiChoice("This is a multi choice question!", ["Wow!", "What is that?"])
    if choice == 1:
        adventure.say("Thank you!")
    elif choice == 2:
        adventure.say("Don't you have eyes?")
    adventure.say("You can also get yes or no input!")
    do_you_like = adventure.question.bool("Do you like this project?", pawn="The Developer")
    if do_you_like:
        adventure.say("I'm glad to hear! Oh yea, you can also use the pawn= to set the character/pawn saying it.", pawn="The Developer")
    if not do_you_like:
        adventure.say("Wow...")
    adventure.wait(1)
    adventure.say("There is also a room system, so that your code doesnt become diagonal.", pawn="The Developer")
    adventure.wait(3)
    adventure.say("Heres a list of rooms, you can go to any of them! They are all in their seperate code", pawn="The Developer")
    adventure.wait(2)
    adventure.gotoPath("elevator")

@adventure.path("elevator")
def elevator():
    elevator_panel = adventure.question.multiChoice("Pick a floor...", pawn="Elevator Panel", choices=["Gravity Room", "Test Chamber", "DO NOT ENTER"])
    if elevator_panel == 1:
        adventure.gotoPath("gravity room")
    elif elevator_panel == 2:
        adventure.gotoPath("test chamber")
    elif elevator_panel == 3:
        want_to_try = adventure.question.bool("That room requires a passcode, want to try at it?", pawn="Room Door")
        if want_to_try:
            while True:
                passcode = adventure.question.text("ENTER 4 DIGIT PASSCODE", pawn="Passcode Lock")
                if passcode == "1337":
                    adventure.say("Door unlocked!")
                    adventure.gotoPath("do not enter")
                    break
                else:
                    adventure.say("Incorrect", pawn="Passcode Lock")


@adventure.path("gravity room")
def gravity_room():
    adventure.say("Arrived at the Gravity Room!")
    adventure.say("It's just a room with low gravity, thats about it.")
    adventure.say("You can press B to go back")
    adventure.question.waitForKey("b")
    adventure.gotoPath("elevator")

@adventure.path("test chamber")
def test_chamber():
    adventure.say("Arrived at the Test Chamber!\nThere isnt really anything here right now.")
    adventure.say("You can press B to go back")
    adventure.question.waitForKey("b")
    adventure.gotoPath("elevator")

@adventure.path("do not enter")
def do_not_enter():
    adventure.say("Wow, you probably looked at the code and achieved nothing! Great job :D")
    adventure.say("You can press B to go back")
    adventure.question.waitForKey("b")
    adventure.gotoPath("elevator")

# NOTE
# This example doesnt show all of it, there are some extra functions like adventure.player.stats etc

adventure.start("start")
```

### Get Started:

AdventureKit is not on PyPi as of right now, though you can easily install it through the terminal.
Here are the commands to do so!

WINDOWS:
```bash
git clone https://github.com/AllergenStudios/AdventureKit
cd AdventureKit
pip install -r requirements.txt
Rename-Item -Path "main.py" -NewName "adventurekit.py"
Move-Item -Path "adventurekit.py" -Destination "..\"
```

LINUX
```bash
git clone https://github.com/AllergenStudios/AdventureKit
cd AdventureKit
pip install -r requirements.txt
mv main.py adventurekit.py
mv adventurekit.py ..
```

### All Functions:

| Function | Arguments |
|----------|----------|
| adventure.gotoPath() | path name |
| adventure.say() | text, (optional: pawn) |
| @adventure.path() | path name |
| adventure.question.text() | prompt, (optional: pawn) |
| adventure.question.bool() | prompt, (optional: pawn) |
| adventure.question.multiChoice() | prompt, choices, (optional: pawn) |
| adventure.question.waitForKey() | key using keyboard module |
| adventure.wait() | seconds |
| adventure.terminal.clear() | no arguments |
| adventure.player.currentPath() | no arguments |
| adventure.player.stats.setStat() | stat name, value |
| adventure.player.stats.getStat() | stat name |
