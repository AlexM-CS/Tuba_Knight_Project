# Created: 11-22-2024
# Last updated: 11-26-2024

# IO packages:

# Graphics packages:

# Built-in packages

# External packages:

# Internal packages:
from Tuba_Knight_Project.tubaKnight.Entities.Characters.Stats import Stats
from Tuba_Knight_Project.tubaKnight.Entities.Items.Items import *

# The items field of PlayerData has 6 special slots, 0-5.
# Slot 0 is the player-character's weapon/held item.
# Slots 1-5 are the player-character's equipped passive items.
# All other slots are items contained within the inventory.
defaultItems = {
     0 : Item(0x0001),
     1 : Item(0x0000),
     2 : Item(0x0000),
     3 : Item(0x0000),
     4 : Item(0x0000),
     5 : Item(0x0000),
     6 : Item(0x0000),
     7 : Item(0x0000),
     8 : Item(0x0000),
     9 : Item(0x0000),
    10 : Item(0x0000),
    11 : Item(0x0000),
    12 : Item(0x0000),
    13 : Item(0x0000),
    14 : Item(0x0000),
    15 : Item(0x0000),
    16 : Item(0x0000),
    17 : Item(0x0000),
    18 : Item(0x0000),
    19 : Item(0x0000),
    20 : Item(0x0000),
    21 : Item(0x0000),
    22 : Item(0x0000),
    23 : Item(0x0000),
    24 : Item(0x0000),
    25 : Item(0x0000),
    26 : Item(0x0000),
    27 : Item(0x0000),
    28 : Item(0x0000),
    29 : Item(0x0000),
    30 : Item(0x0000),
    31 : Item(0x0000),
    32 : Item(0x0000),
    33 : Item(0x0000),
    34 : Item(0x0000),
    35 : Item(0x0000)
}

# The PlayerData class is what player-characters use to hold all
# their relevant data, such as Stats, Items, Level, etc.
class PlayerData:
    """
    Description:
    The PlayerData class is what player-characters use to hold all
    their relevant data, such as Stats, Items, Level, etc.

    Fields:
    str name - the name of the current player-character
    int level - the current level of the player
    int experience - the current experience held by the player
    int regionID - the current region the player is located
    Stats stats - the current player-character's Stats
    dict items - the current player-character's items
    """
    name = None
    level = None
    experience = None
    regionID = None
    stats = None
    items = None

    def __init__(self, name : str, level : int = 0x0001, experience : int = 0x0000, regionID : int = 0x00, stats : Stats = Stats(), items : dict = None):
        """
        Initializes a PlayerData object with the current player-character's data.
        """
        self.name = name
        self.level = level
        self.experience = experience
        self.regionID = regionID
        self.stats = stats
        if (items is not None):
            self.items = items
        else:
            # Dummy values for items. Used mostly when creating new player-characters.
            # Dummy value for equipped and inventory items is Item ID 0.
            self.items = defaultItems

    def __repr__(self):
        """
        The current player-character's PlayerData, displayed as a string.
        Used when saving.
        """
        LVL = "0x%04x" % self.level
        EXP = "0x%04x" % self.experience
        RGNID = "0x%02x" % self.regionID

        output = (f"PlayerData_{self.name}\n"
                  f"Stats_LVL:{LVL},EXP:{EXP},{self.stats.__repr__()}\n"
                  f"RegionID_{RGNID}\n"
                  f"Items_")

        # Append the weapon/held item
        output += f"\nHELD_{self.items[0].__repr__()}"

        # Append the equipped passive items
        for i in range(1, 6):
            output += f"\nITM{i}_{self.items[i].__repr__()}"

        # Append the items in the inventory
        for i in range(6, 36):
            output += f"\nITMi_{self.items[i].__repr__()}"

        return output