# Created: 11-24-2024
# Last updated: 11-24-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:

class ItemStats:
    """
    Description:
    The ItemStats class holds stats for a given item.

    Fields:
    int level - the item's level
    int degree - the item's degree
    int health - the health increase this item provides
    int magicpoints - the magicpoints increase this item provides
    int strength - the strength increase this item provides
    int dexterity - the dexterity increase this item provides
    int magic - the magic increase this item provides
    int defense - the defense increase this item provides
    int speed - the speed increase this item provides
    int crit - the crit chance increase this item provides
    """
    def __init__(self, level : int, degree : int, health : int, magicpoints : int, strength : int,
                 dexterity : int, magic : int, defense : int, speed : int, crit : int):
        """ Initializes this ItemStats object. """
        self.level = level
        self.degree  = degree
        self.health = health
        self.magicpoints = magicpoints
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.defense = defense
        self.speed = speed
        self.crit = crit

    def __repr__(self):
        """
        String representation of the ItemStats object.
        Can be used to re-create the object.
        """
        LVL = "0x%04x" % self.level
        DGR = "0x%01x" % self.degree
        HPS = "0x%04x" % self.health
        MPS = "0x%04x" % self.magicpoints
        STR = "0x%04x" % self.strength
        DEX = "0x%04x" % self.dexterity
        MGC = "0x%04x" % self.magic
        DFN = "0x%04x" % self.defense
        SPE = "0x%04x" % self.speed
        CRT = "0x%04x" % self.crit

        return f"Stats_LVL:{LVL},DGR:{DGR},HPS:{HPS},MPS:{MPS},STR:{STR},DEX:{DEX},MGC:{MGC},DFN:{DFN},SPE:{SPE},CRT:{CRT}"

    def getExpNeeded(self):
        """ Returns the Experience needed to level up this item. Returns None if item level greater than 99. """
        if (self.level > 99):
            return None
        else:
            return self.level**1.5 * self.degree

    def setStats(self, stats : list[tuple[str, int]]):
        """ Changes the specified stats. """
        for stat in stats:
            match (stat[0]):
                case "LVL":
                    self.level = stat[1]
                case "DGR":
                    self.degree = stat[1]
                case "HPS":
                    self.health = stat[1]
                case "MPS":
                    self.magicpoints = stat[1]
                case "STR":
                    self.strength = stat[1]
                case "DEX":
                    self.dexterity = stat[1]
                case "MGC":
                    self.magic = stat[1]
                case "DFN":
                    self.defense = stat[1]
                case "SPE":
                    self.speed = stat[1]
                case "CRT":
                    self.crit = stat[1]
                case _:
                    raise ValueError(f"Invalid stat: {stat}")