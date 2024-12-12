# Created: 11-22-2024
# Last updated: 12-11-2024

# IO packages:

# Graphics packages:

# Built-in packages
import random

# External packages:

# Internal packages:
from tubaKnight.Entities.Characters.Stats import Stats
from tubaKnight.Entities.Items.Items import Item

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
    nick = None
    level = None
    experience = None
    regionID = None
    stats = None
    items = None

    def __init__(self, name : str, nick : str = "", level : int = 0x0001, experience : int = 0x0000, regionID : int = 0x00, stats : Stats = Stats(), items : dict = None) -> None:
        """ Initializes a PlayerData object with the current player-character's data. """
        self.name = name
        self.nick = nick
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

        if (self.nick == ""):
            self.nick = "None"

        output = (f"PlayerData_{self.name}_{self.nick}\n"
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

    def levelUp(self, expNeeded : int):
        self.level += 1
        self.experience -= expNeeded

        self.stats.hitpoints += 1
        self.stats.magicpoints += 1
        self.stats.strength += 1
        self.stats.dexterity += 1
        self.stats.magic += 1
        self.stats.defense += 1
        self.stats.speed += 1
        self.stats.critchance += 1

    def getStatUps(self) -> list[int]:
        boosts = [0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(0, 7):
            item = self.items[i]
            if (item.stats.health > 0):
                boosts[0] += 1
            if (item.stats.magicpoints > 0):
                boosts[1] += 1
            if (item.stats.strength > 0):
                boosts[2] += 1
            if (item.stats.dexterity > 0):
                boosts[3] += 1
            if (item.stats.magic > 0):
                boosts[4] += 1
            if (item.stats.defense > 0):
                boosts[5] += 1
            if (item.stats.speed > 0):
                boosts[6] += 1
            if (item.stats.critchance > 0):
                boosts[7] += 1

        for stat in boosts:
            stat += random.randrange(3, 7)

        return boosts