from adventurekit import TextAdventure


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