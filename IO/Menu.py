# Created: 12-2-2024
# Last updated: 12-11-2024

# IO packages:
from .Inputs import *

# Graphics packages:
from Graphics.Text.Text import Text

# Built-in packages:

# External packages:

# Internal packages:
import Config
from tubaKnight.Entities.Characters.PlayerCharacter import PlayerCharacter

class Menu:
    """
    Description:
    The Menu class is used to display the menu to the player.
    A Menu can only exist while a PlayerCharacter exists and is in a "Menu State".
    This is also a parent class for other Menus with more specific functions.

    Fields:
    PlayerCharacter player - The player currently using the Menu
    tuple[str] options - The currently selectable options for the player
    tuple[str] defaultOptions - The default options for this Menu. Changed by subclasses.
    """
    player = None
    options = None
    default = ("Play...", "Save...")
    game = ("Story", "Wander", "Travel...", "Level Up...", "View Items...", "View Character...", "Back...")
    saveFromMenu = ("Save", "Save and Quit", "Back...")
    saveFromGame = ("Continue...", "Save and Continue...", "Save and Quit")

    def __init__(self, player : PlayerCharacter, options = default):
        """ Initializes this Menu object. """
        self.player = player
        self.options = options

    def __repr__(self, before : str = None, after : str = None):
        """ Default representation for the Menu. Returns the current options. """
        display = f"==============================\n"

        if (before is not None):
            display += before + "\n"

        for i in range(0, len(self.options)):
            display += f"{i + 1}. {self.options[i]}\n"

        if (after is not None):
            display += after + "\n"

        display += f"=============================="
        return display

    def select(self, before : str = None, after : str = None, pre : int = None) -> int:
        """ Selects an option from the Menu. """
        if (pre is not None and pre > 0):
            return pre
        Text(self.__repr__(before, after)).display()
        while True:
            option = nextInt(f"Select an option: ")
            if (option is not None) and (option > 0) and (option <= len(self.options)):
                return option
            else:
                Window.clear()
                Text(self.__repr__(before, after)).display()

    def setMenu(self, mode : int = 0):
        match mode:
            case 0: # Main Menu mode
                self.options = self.default
            case 1: # Game Menu mode
                self.options = self.game
            case 2: # SaveFromMenu mode
                self.options = self.saveFromMenu
            case 3: # SaveFromGame mode
                self.options = self.saveFromGame
            case _: # Illegal mode
                raise ValueError("Invalid mode.")