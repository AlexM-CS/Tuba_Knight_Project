# Created: 12-2-2024
# Last updated: 12-14-2024

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
        """
        Initializes this Menu object.
        @param player: the player currently using the Menu
        @param options: the currently selectable options for the player
        """
        self.player = player
        self.options = options

    def __repr__(self, before : str = None, after : str = None):
        """
        Default representation for the Menu. Returns the current options.
        @param before: optional text to display before the menu item
        @param after: optional text to display after the menu item
        """
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
        """
        Selects an option from the Menu.
        @param before: optional text to display before the menu item
        @param after: optional text to display after the menu item
        @param pre: optional pre-selected option
        @return an integer representing the selected option
        """
        if (pre is not None and pre > 0):
            return pre
        Text(self.__repr__(before, after)).display()
        while True:
            if (Config.commands_on):
                option = nextCommand(self.player, f"Select an option: ")
            else:
                option = nextInt(f"Select an option: ")
            if (option is not None) and (type(option) is not str) and (option > 0) and (option <= len(self.options)):
                return option
            else:
                Window.clear()
                Text(self.__repr__(before, after)).display()

    def setMenu(self, mode : int = 0):
        """
        Sets the menu to a pre-built one
        @param mode: the mode to switch to
        """
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

class ItemMenu(Menu):
    """
    Description:
    The ItemMenu class is a custom-made Menu that allows the player
    to view their items. Because this Menu can have multiple pages,
    it has more specific functionality.

    Fields:
    int page - the current page number
    str pageName - the name of the current page
    """
    page = None
    pageName = None

    def __init__(self, player : PlayerCharacter):
        """
        Initializes this ItemMenu object.
        """
        super().__init__(player, None)
        self.page = 1
        self.scroll(0)

    def __repr__(self, before : str = None, after : str = None) -> str:
        """
        Default representation for the ItemMenu. Displays the current page's items.
        """
        display = f"==============================\n"

        if (before is not None):
            display += before + "\n"

        if (self.page < 2):
            for value in self.options:
                display += f"{value + 1}:\t{self.player.myData.items[value].__str__()}\n"
                display += f"\t{self.player.myData.items[value].description()}\n"
        else:
            for value in self.options:
                display += f"{value - 5}:\t{self.player.myData.items[value].__str__()}\n"
                display += f"\t{self.player.myData.items[value].description()}\n"

        display += (f"\n{self.pageName}\n\n"
                    f"Use [A] to scroll left, [D] to scroll right, and [E] to exit\n"
                    f"Type an Item's number to view it\n")

        display += f"=============================="
        return display

    def select(self, before : str = None, after : str = None, pre : str = None) -> str:
        """
        Selects an option from the ItemMenu. Also allows for string inputs
        @param before: optional text to display before the menu item
        @param after: optional text to display after the menu item
        @param pre: optional pre-selected option
        @return the selected option
        """
        if (pre is not None):
            return pre
        Text(self.__repr__(before, after)).display()
        if (Config.commands_on):
            option = nextCommand(self.player, f"Select an option: ")
        else:
            option = nextStr(f"Select an option: ")

        return option

    def scroll(self, scrollNum : int) -> None:
        """
        Scrolls the current "page"- that is, displays different items
        depending on the current page number.
        """
        minVal = -1 if Config.debug else 0
        if (self.page + scrollNum > minVal and self.page + scrollNum < 8):
            self.page += scrollNum

        match (self.page):
            case 0: # Page 0: All Items
                # NOTE: This page can only be accessed during debugging
                self.pageName = f"Page 0: All Items (Debug)"
                self.options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                30, 31, 32, 33, 34, 35]
            case 1: # Page 1: Equipped Items
                self.pageName = f"Page 1: Equipped Items"
                self.options = [0, 1, 2, 3, 4, 5]
            case 2: # Page 2: Inventory (1 - 5)
                self.pageName = f"Page 2: Inventory (1 - 5)"
                self.options = [6, 7, 8, 9, 10]
            case 3: # Page 3: Inventory (6 - 10)
                self.pageName = f"Page 3: Inventory (6 - 10)"
                self.options = [11, 12, 13, 14, 15]
            case 4: # Page 4: Inventory (11 - 15)
                self.pageName = f"Page 4: Inventory (11 - 15)"
                self.options = [16, 17, 18, 19, 20]
            case 5: # Page 5: Inventory (16 - 20)
                self.pageName = f"Page 5: Inventory (16 - 20)"
                self.options = [21, 22, 23, 24, 25]
            case 6: # Page 6: Inventory (21 - 25)
                self.pageName = f"Page 6: Inventory (21 - 25)"
                self.options = [26, 27, 28, 29, 30]
            case 7: # Page 7: Inventory (26 - 30)
                self.pageName = f"Page 7: Inventory (26 - 30)"
                self.options = [31, 32, 33, 34, 35]
            case _: # Invalid page number
                raise ValueError(f"Invalid page.")