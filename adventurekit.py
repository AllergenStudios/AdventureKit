from functools import wraps
import keyboard
import colorama
import time
import os


valid_yes = [
  "y"
  "true",
  "yes",
  "yeah",
  "yup",
  "yuppers",
  "yep",
  "yeppers",
  "yessir",
  "yessiree",
  "yessum",
  "yass",
  "ya",
  "yay",
  "yea",
  "indeed",
  "absolutely",
  "affirmative",
  "sure",
  "certainly",
  "of course",
  "right",
  "correct",
  "roger",
  "aye",
  "absolutely",
  "totally",
  "definitely",
  "most certainly",
  "you bet",
  "affirm",
  "agreed",
  "positively",
  "indubitably",
  "alright",
  "ok",
  "fine",
  "all right",
  "very well",
  "righto",
  "by all means",
  "without a doubt"
]

valid_no = [
  "n"
  "false",
  "no",
  "nah",
  "nope",
  "na",
  "nay",
  "negative",
  "not at all",
  "absolutely not",
  "never",
  "not really",
  "i don't think so",
  "i disagree",
  "not a chance",
  "definitely not",
  "i'm afraid not",
  "sorry, no",
  "no way",
  "not on your life",
  "not by a long shot",
  "no siree",
  "nope, nope, nope",
  "not in a million years",
  "no doubt about it",
  "no thanks",
  "no can do",
  "not possible",
  "nope, nada",
  "not in the slightest",
  "not by any means",
  "nope, sorry",
  "no, definitely not",
  "no chance",
  "no way, jose",
  "no sir/madam",
  "not gonna happen",
  "not in this lifetime",
  "i beg to differ",
  "not my cup of tea",
  "no siree bob",
  "not even close"
]


player_current_path = "Unset"

player_stats = {}



def hexColor(hex, background=False):
    h = hex.lstrip('#')
    r = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r[0], r[1], r[2])

class TextAdventure:
    def __init__(self):
        self.paths = {}

    def path(self, name):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                return name
            self.paths[name] = func
            return wrapper
        return decorator

    def gotoPath(self, path):
        if path in self.paths:
            self.paths[path]()
            player_current_path = path
        else:
            raise ValueError(f"Path '{path}' does not exist.")

    def start(self, start_path):
        current_path = start_path
        while current_path:
            current_path = self.gotoPath(current_path)

    class question:
        @staticmethod
        def text(prompt, pawn=None):
            if pawn is None:
                stdin = input(f"{hexColor('#4cb191')}{prompt}{hexColor('#1c1c25')}: {colorama.Fore.RESET}")
            elif pawn:
                stdin = input(f"{hexColor('#2596be')}{pawn}{hexColor('#1c1c25')}: {hexColor('#4cb191')}{prompt}{hexColor('#1c1c25')}: {colorama.Fore.RESET}")

        @staticmethod
        def bool(prompt, pawn=None):
            if pawn is None:
                while True:
                    stdin = input(f"{hexColor('#4cb191')}{prompt}{hexColor('#1c1c25')} (YES/NO): {colorama.Fore.RESET}")
                    if stdin.lower() in valid_yes:
                        return True
                        break
                    elif stdin.lower() in valid_no:
                        return False
                        break
                    else:
                        print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")
            elif pawn:
                while True:
                    stdin = input(f"{hexColor('#2596be')}{pawn}{hexColor('#1c1c25')}: {hexColor('#4cb191')}{prompt}{hexColor('#1c1c25')} (YES/NO): {colorama.Fore.RESET}")
                    if stdin.lower() in valid_yes:
                        return True
                        break
                    elif stdin.lower() in valid_no:
                        return False
                        break
                    else:
                        print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")

        @staticmethod
        def multiChoice(prompt, choices, pawn=None):
            if pawn is None:
                print(f"{hexColor('#4cb191')}{prompt}{hexColor('#1c1c25')} (MULTICHOICE){colorama.Fore.RESET}")
                for choice in choices:
                    print(f"  {hexColor('#1c1c25')}◆{choices.index(choice) + 1}{hexColor('#2596be')} {choice} {colorama.Fore.RESET}")
                while True:
                    try:
                        stdin = int(input(f"{hexColor('#1c1c25')}CHOICE: {colorama.Fore.RESET}"))
                    except ValueError:
                        print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")
                        continue
                    if stdin > 0:
                        if stdin < len(choices) + 1:
                            return stdin
                            break
                        else:
                            print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")
                    else:
                        print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")

            elif pawn:
                print(f"{hexColor('#2596be')}{pawn}{hexColor('#1c1c25')}: {hexColor('#4cb191')}{prompt}{hexColor('#1c1c25')} (MULTICHOICE){colorama.Fore.RESET}")
                for choice in choices:
                    print(f"  {hexColor('#1c1c25')}◆{choices.index(choice) + 1}{hexColor('#2596be')} {choice} {colorama.Fore.RESET}")
                while True:
                    try:
                        stdin = int(input(f"{hexColor('#1c1c25')}CHOICE: {colorama.Fore.RESET}"))
                    except ValueError:
                        print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")
                        continue
                    if stdin > 0:
                        if stdin < len(choices) + 1:
                            return stdin
                            break
                        else:
                            print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")
                    else:
                        print(f"{colorama.Fore.LIGHTRED_EX}That is not a valid answer.{colorama.Fore.RESET}")

        @staticmethod
        def waitForKey(key):
            while True:
                if keyboard.is_pressed(key):
                    break


    @staticmethod
    def say(text, pawn=None):
        if pawn is None:
            print(f"{hexColor('#4cb191')}{text}{colorama.Fore.RESET}")
        elif pawn:
            print(f"{hexColor('#2596be')}{pawn}{hexColor('#1c1c25')}: {hexColor('#4cb191')}{text}"
                  f"{colorama.Fore.RESET}")
    @staticmethod
    def wait(seconds):
        time.sleep(seconds)


    class terminal:
        @staticmethod
        def clear():
            if os.name == 'nt':
                _ = os.system('cls')

                # for mac and linux(here, os.name is 'posix')
            else:
                _ = os.system('clear')

    class player:
        @staticmethod
        def currentPath():
            return player_current_path

        class stats:
            @staticmethod
            def setStat(stat, value):
                player_stats[stat] = value

            @staticmethod
            def getStat(stat):
                return player_stats[stat]
