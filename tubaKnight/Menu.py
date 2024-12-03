# Created: 12-2-2024
# Last updated: 12-2-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from Entities.Characters.PlayerCharacter import PlayerCharacter

class Menu:
    """
    Description:
    The Menu class is used to display the menu to the player.
    A Menu can only exist while a PlayerCharacter exists and is in a "Menu State".

    Fields:
    PlayerCharacter player - The player currently using the menu
    """
    player = None

    def __init__(self, player : PlayerCharacter):
        """ Initializes this Menu object. """
        self.player = player

    pass