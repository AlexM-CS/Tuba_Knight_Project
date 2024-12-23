# Created: 11-22-2024
# Last updated: 11-27-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from ..Entity import Entity
from ..Entity import IDLE, BATTLING, DEAD
from ..Items.Items import Item
from .Stats import Stats
from ...Regions.Special.GlobalLootTables import *

"""
Static Fields:
list[str] ENEMY_NAMES - list containing the names of enemies
"""

ENEMY_NAMES = ["Dummy"]

def getName(ID : int) -> str:
    """ Returns the name of the enemy with the given ID. """
    if (ID >= len(ENEMY_NAMES)):
        raise IndexError("Enemy ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Enemy IDs may not be negative.")
    return ENEMY_NAMES[ID]

class Enemy(Entity):
    """
    Description:
    An Enemy is an Entity that the player fights.
    As with other entities, Enemies can be interacted with:
    Action 1 - Enemies can be fought
    Action 2 - Enemies can alter the player's temporary Stats while in battle
    Action 4 - Enemies can reward experience after battle
    Action 4 - Enemies can reward items after battle

    Fields:
    int ID - the ID of this enemy
    str name - the name of the enemy
    int state - the state of this enemy
    int level - the level of this enemy
    Stats stats - the stats of this enemy
    Item weapon - the weapon held by this enemy
    dict lootTable - the items this enemy is able to drop
    """

    level = None
    stats = None
    weapon = None
    lootTable = None

    def __init__(self, ID: int, level : int = 1, stats : Stats = None, weapon : Item = Item(0x0001), lootTable : dict = globalTable):
        """ Instantiates this enemy. """
        super().__init__(ID)
        self.name = getName(ID)
        self.level = level
        self.stats = stats
        self.weapon = weapon
        self.lootTable = lootTable

    def act(self):
        """
        The actions this enemy can perform are detailed above.
        Action 1 can be accessed while the enemy is idle.
        Action 2 can be accessed while the enemy is battling.
        Actions 3 and 4 can be accessed while the enemy is dead.
        """
        if (self.state == IDLE):
            output = engage()
        elif (self.state == BATTLING):
            output = attack(self.stats)
        elif (self.state == DEAD):
            output = (rewardExp(self.name, self.level), rewardItems(self.name, self.level, self.lootTable))
        else:
            raise RuntimeError("This enemy's state is illegal.")
        return output

    def setState(self, state : int):
        pass

def engage():
    """ Starts a battle with the player. """
    pass

def attack(stats : Stats):
    """ Attacks the player. """
    pass

def rewardExp(name : str, level : int):
    """ Gives experience to the player. """
    pass

def rewardItems(name : str, level : int, lootTable : dict):
    """ Give an ItemList to the player."""
    pass