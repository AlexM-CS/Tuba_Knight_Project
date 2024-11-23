# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages

# External packages:

# Internal packages:
from Tuba_Knight_Project.tubaKnight.Entities.Characters.Stats import Stats
from Tuba_Knight_Project.tubaKnight.Entities.Items.Items import *

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
    Stats stats - the current player-character's Stats
    Item weapon - the current player-character's held weapon
    ItemList items - the current player-character's equipped items
    Inventory inventory - the current player-character's inventory
    """
    name = None
    level = None
    experience = None
    stats = None
    weapon = None
    items = None
    inventory = None

    def __init__(self, name : str, level : int = 0x0001, experience : int = 0x0000, stats : Stats = Stats(), weapon : Item = Item(0x0001), items : list = None, inventory : list = None):
        """
        Initializes a PlayerData object with the current player-character's data.
        """
        self.name = name
        self.level = level
        self.experience = experience
        self.stats = stats
        self.weapon = weapon
        self.items = items
        self.inventory = inventory

    # The current player-character's PlayerData, displayed as a string.
    # Used when saving
    def __repr__(self):
        LVL = "0x%04x" % self.level
        EXP = "0x%04x" % self.experience
        if (self.stats is None):
            self.stats = Stats()
        if (self.items is None):
            self.items = []
        if (self.inventory is None):
            self.inventory = []

        return (f"PlayerData_{self.name}\n"
                f"Stats_LVL:{LVL},EXP:{EXP},{self.stats.__repr__()}")