# Created: 12-2-2024
# Last updated: 12-2-2024

# IO packages:
from Tuba_Knight_Project.IO.Inputs import *

# Graphics packages:
from Tuba_Knight_Project.Graphics.Text.Text import Text

# Built-in packages:

# External packages:

# Internal packages:
from Tuba_Knight_Project import Config
from Entities.Characters.PlayerCharacter import PlayerCharacter

class Menu:
    """
    Description:
    The Menu class is used to display the menu to the player.
    A Menu can only exist while a PlayerCharacter exists and is in a "Menu State".
    This is also a parent class for other Menus with more specific functions.

    Fields:
    PlayerCharacter player - The player currently using the menu
    tuple[str] options - The currently selectable options for the player
    """
    player = None
    options = None

    def __init__(self, player : PlayerCharacter, options = ("Play...", "Settings...", "Save...")):
        """ Initializes this Menu object. """
        self.player = player
        self.options = options

    def setOptions(self, options : list[str]) -> bool:
        """
        Sets the list of options for the player.
        For debugging only.
        """
        if (Config.debug):
            self.options = options
            return True
        return False

    def __repr__(self):
        """ Default representation for the Menu. Returns the current options. """
        display = f"==============================\n"
        for i in range(0, len(self.options)):
            display += f"{i}. {self.options[i]}\n"
        display += f"=============================="
        return display

    def select(self):
        Text(self.__repr__()).display()
        while True:
            option = nextInt()
            option -= 1
            if (option is not None) and (option >= 0) and (option < len(self.options)):
                return self.options[option]

class GameMenu(Menu):
    """
    Description:
    The GameMenu class is used during gameplay.
    """
    def __init__(self, player : PlayerCharacter):
        """ Initializes this GameMenu object. """
        super().__init__(player, options = ("Story", "Wander", "Travel...", "Level Up...", "View Items...", "View Character...", "Back..."))

class SettingsMenu(Menu):
    pass

class SaveMenu(Menu):
    pass