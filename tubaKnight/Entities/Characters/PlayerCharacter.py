# Created: 11-27-2024
# Last updated: 11-27-2024

# IO Packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from ..Entity import IDLE, BATTLING, DEAD, MENU, CUTSCENE
from Tuba_Knight_Project.TubaKnight import *
from Tuba_Knight_Project.tubaKnight.Regions.Area import Area

class PlayerCharacter(Entity):
    """
    Description:
    The PlayerCharacter class represents a player-character,
    Player-characters are the action behind all the data they
    store (handled by the PlayerData class).
    # NOTE: By default, players are Entity ID 0.
    Players have the most actions out of all entities:
    Group 1: Menu Actions
        Action 1: Players can interact with the main menu
        Action 2: Players can progress the main story
        Action 3: Players can view their items
        Action 4: Players can equip, unequip, and upgrade items, as well as themselves, with experience
        Action 5: Players can alter game settings
        Action 6: Players can save
        Action 7: Players can quit the game
    Group 2: Game Actions
        Action 8: Players initiate interactions with other entities
        Action 9: Players can start battles
        Action 10: Players can alter the stats of other entities while in battle
        Action 11: Players can initiate and end dialogue sequences
        Action 12: Players can change the current Region
    Group 3: Other
        Action 13: Players can save and load Region data

    Fields:
    str nick - the nickname of the player-character, if any
    PlayerData myData - the current player's data
    """

    myNick = None
    myData = None

    def __init__(self, myName : str, myData : PlayerData, myNick : str = None):
        super().__init__(0)
        self.name = myName
        self.myData = myData
        self.myNick = myNick

    def act(self):
        """
        The actions the player can perform are detailed above.
        Actions 1-7 can be accessed while in the menu.
        Action 8-12 can be accessed while in game
        Action 13 can be accessed when moving between areas
        (This is the only action that the user does not initiate)
        """
        pass

    def setState(self, state : int):
        pass

def menuActions(self):
    """
    From the menu, the following options can be chosen:
    Actions 2, 3, 5, 6, and 7
    """
    pass

def viewItems(self):
    """
    From the item menu, the following options can be chosen:
    Action 4
    """
    pass

def interact(self, other : Entity):
    """ Controls interactions between the player and another Entity. """
    pass

def attack(self):
    """ Attacks the given entitty """
    pass

def changeRegion(self, newArea : Area):
    pass

def loadRegion(self):
    pass