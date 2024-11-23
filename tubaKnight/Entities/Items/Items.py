# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from ..Entity import Entity
from ItemTags import *

"""
Static Fields:
idle = 0 - indicates that this item is idle
battling = 1 - indicates that this item is battling
list[str] ITEM_NAMES - list containing the names of items
dict ITEM_DEGREES - a dictionary of item degrees. Higher item degree = more damage
"""

idle = 0
battling = 1

ITEM_NAMES = ["No Item", "Fists"]

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
    int ID - the ID of this item
    str name - the name of the item
    int state - the state of this item
    list[str] tags - tags belonging to this item
    """

    ID = None
    degree = None
    state = None
    tags = None

    def __init__(self, ID : int, degree : int = ITEM_DEGREES["Pianissimo"], state : int = idle):
        """ Instantiates this Item. """
        super().__init__(ID)
        self.name = getName(ID)
        self.degree = degree
        self.state = state
        self.tags = addTagsToItemByID(ID)

    def act(self):
        """
        The actions this item can perform are detailed above.
        Actions 1, 2, 3, and 4 can be accessed while the player is not in battle.
        Actions 5 and 6 can be accessed while the player is in battle.
        """
        if (self.state == idle):
            equip(self.tags.__contains__("Weapon"))
            putAway()
            upgrade()
            fuseWith()
        elif (self.state == battling):
            attack()
            performSkill()
        else:
            raise RuntimeError("This enemy's state is illegal.")
        return

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