# Created: 11-22-2024
# Last updated: 12-14-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from ..Entity import Entity
from ..Entity import IDLE, BATTLING
from .ItemStats import *

"""
Static Fields:
list[str] ITEM_NAMES - list containing the names of items
list[str] ITEM_TAGS - list containing potential tags for items
dict ITEM_DEGREES - a dictionary of item degrees. Higher item degree = more damage
"""

ITEM_NAMES = ["No Item", "Fists"]

ITEM_TAGS = ["Dummy", "Weapon", "Passive", "Percussive", "Brass", "Stringed", "Soothing", "Heavy", "Jazzy"]

ITEM_DEGREES = {
    "Pianissimo" : 2,
    "Piano" : 3,
    "Mezzo-piano" : 4,
    "Mezzo-forte" : 5,
    "Forte" : 6,
    "Fortissimo" : 8,
    "Symphonic" : 10
}

def getName(ID : int) -> str:
    """ Returns the name of the item with the given ID. """
    if (ID >= len(ITEM_NAMES)):
        raise IndexError("Item ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Item IDs may not be negative.")
    return ITEM_NAMES[ID]

def addTagByID(ID : int) -> str:
    """ Adds a specified tag to an item. """
    if (ID >= len(ITEM_TAGS)):
        raise IndexError("Tag ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Tag IDs may not be negative.")
    return ITEM_TAGS[ID]

def addTagsToItemByID(ID : int) -> list[str]:
    """ Creates a list of tags based on an Item ID. """
    if (ID >= len(ITEM_NAMES)):
        raise IndexError("Item ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Item IDs may not be negative.")
    tags = list()
    match (ID):
        case 0:
            tags.append(addTagByID(0))
        case 1:
            tags.append(addTagByID(1))
            tags.append(addTagByID(3))
    return tags

def getStatsByID(ID : int, level : int, degree : int) -> ItemStats:
    """ Gets this item's stats based on its ID. """
    if (ID >= len(ITEM_NAMES)):
        raise IndexError("Item ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Item IDs may not be negative.")
    stats = ItemStats(level, degree, 0, 0, 0, 0, 0, 0, 0, 0)
    match (ID):
        case 0, 1:
            pass
    return stats

class Item(Entity):
    """
    Description:
    An Item is an Entity that the player can equip
    As with other entities, Items can be interacted with:
    Action 1 - Items can be equipped
    Action 2 - Items can be placed in the player's inventory
    Action 3 - Items can be upgraded outside of battle
    Action 4 - Items can be fused outside of battle
    Action 5 - Items can attack during battle
    Action 6 - Items can perform Skills

    Fields:
    int level - the level of this item
    int degree - the degree of this item
    int state - the state of this item
    list[str] tags - tags belonging to this item
    ItemStats stats - the stats of this item
    """

    degree = None
    state = None
    tags = None
    stats = None

    def __init__(self, ID : int, level : int = 1, degree : int = ITEM_DEGREES["Pianissimo"], state : int = IDLE):
        """ Instantiates this Item. """
        if (ID == 0x0000 or ID == 0x0001):
            super().__init__(ID)
            if (ID == 0x0000):
                self.name = "No Item"
                self.tags = ["Dummy"]
            else:
                self.name = "Fists"
                self.tags = ["Weapon", "Percussive"]
            self.level = 1
            self.degree = 2
            self.state = 0
            self.stats = ItemStats(1, 2, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            super().__init__(ID)
            self.name = getName(ID)
            self.level = level
            self.degree = degree
            self.state = state
            self.tags = addTagsToItemByID(ID)
            self.stats = getStatsByID(ID, level, degree)

    def description(self):
        return "DEFAULT DESCRIPTION"

    def act(self):
        """
        The actions this item can perform are detailed above.
        Actions 1, 2, 3, and 4 can be accessed while the player is not in battle.
        Actions 5 and 6 can be accessed while the player is in battle.
        """
        if (self.state == IDLE):
            equip(self.tags.__contains__("Weapon"))
            putAway()
            upgrade()
            fuseWith()
        elif (self.state == BATTLING):
            attack()
            performSkill()
        else:
            raise RuntimeError("This item's state is illegal.")
        return

    def setState(self, state : int):
        pass

    def __str__(self):
        """ Returns this item's name. """
        return self.name

    def __repr__(self) -> str:
        """
        Returns this item's ID and stats.
        Can be used to re-create this object.
        """
        ID = "0x%04x" % self.ID
        return f"ID_:{ID},{self.stats.__repr__()}"

def equip(isWeapon : bool):
    pass

def putAway():
    pass

def upgrade():
    pass

def fuseWith(other : Item):
    pass

def attack():
    pass

def performSkill():
    pass