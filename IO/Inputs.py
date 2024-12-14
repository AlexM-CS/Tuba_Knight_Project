# Created: 11-21-2024
# Last updated: 12-14-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:
import maskpass

# Internal packages:
from . import Window
from Commands import *
from tubaKnight.Entities.Characters.PlayerCharacter import PlayerCharacter

# This file keeps track of various inputs the user can perform while playing.

def nextInt(text : str = "default", pre : int = None) -> int:
    """
    Loops until an integer is input, then returns the parsed integer.
    @param text: the Text to display
    @param pre: pre-determined choice
    @return: the parsed integer
    """
    while True:
        try:
            if (pre is None):
                num = int(input(text) + "\n")
            else:
                num = pre
            Window.clear()
            return num

        except ValueError:
            Window.clear()

def nextStr(text : str = "default", pre : str = None) -> str:
    """
    Returns a parsed string
    @param text: the Text to display
    @param pre: pre-determined choice
    @return: the parsed string
    """
    if (pre is None):
        string = input(text + "\n")
    else:
        string = pre
    Window.clear()
    return string

def nextCommand(player : PlayerCharacter, text : str = "default"):
    string = input(text + "\n")
    Window.clear()
    match (string):
        case "setStat": # setStat command
            arg1 = player
            arg2 = nextStr("arg2 stat")
            arg3 = nextInt("arg3 value")
            setStat(arg1, arg2, arg3)
            return
        case _: # Normal output
            try:
                return int(string)
            except ValueError:
                return string

def password(ask : str):
    """ Allows the user to enter a string that gets masked. """
    return maskpass.askpass(ask, mask="*")

def enter_to_continue():
    """ Waits until enter is pressed by the user. """
    input("Press Enter to continue...")
    Window.clear()