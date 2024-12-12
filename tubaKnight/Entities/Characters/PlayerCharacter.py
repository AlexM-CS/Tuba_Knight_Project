# Created: 11-27-2024
# Last updated: 12-11-2024

# IO Packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from ..Entity import IDLE, BATTLING, DEAD, MENU, CUTSCENE
from ..Entity import Entity
from tubaKnight import *
from tubaKnight.Regions.Area import Area
from PlayerData.PlayerData import PlayerData

class PlayerCharacter(Entity):
    """
    Description:
    The PlayerCharacter class represents a player-character,
    Player-characters are the action behind all the data they
    store (handled by the PlayerData class).
    # NOTE: By default, players are Entity ID 0.
    Players have the most actions out of all entities:

    Fields:
    str nick - the nickname of the player-character, if any
    PlayerData myData - the current player's data
    int rand - the current random value needed to level up
    """
    myNick = None
    myData = None

    def __init__(self, myName : str, myData : PlayerData):
        super().__init__(0)
        self.name = myName
        self.myData = myData
        self.myNick = myData.nick

    def __str__(self) -> str:
        """ Displays the nickname of the player-character, if any. """
        if (self.myNick != ""):
            return f"{self.__repr__()}"
        else:
            return f"{self.myNick}"

    def __repr__(self) -> str:
        """ Displays the name of the player-character. """
        return f"{self.name}"

    def act(self):

        pass

    def getExpNeeded(self):
        """ Gets the EXP needed to level up. """
        return (self.myData.level * 14) + 23

    def levelUp(self) -> bool:
        """ Levels up the player. Returns True when successful. """
        if (self.myData.experience >= self.getExpNeeded()):
            self.myData.levelUp(self.getExpNeeded())
            return True
        else:
            return False

def changeRegion(self, newArea : Area):
    pass

def loadRegion(self):
    pass