# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:


class Stats:
    """
    Description:
    The Stats class represents the Stats of a Character object.
    Stats are mainly used during damage calculations for Characters.

    Fields:
    int hitpoints - the hitpoints of the character
    int magicpoints - the magicpoints of the character
    int strength - the strength of the character
    int dexterity - the dexterity of the character
    int magic - the magic of the character
    int defense - the defense of the character
    int speed - the speed of the character
    int critchance - the critchance of the character
    """

    hitpoints = None
    magicpoints = None
    strength = None
    dexterity = None
    magic = None
    defense = None
    speed = None
    critchance = None

    def __init__(self, hitpoints : int = 0x000a, magicpoints : int = 0x000a, strength : int = 0x000a, dexterity : int = 0x000a,
                 magic : int = 0x000a, defense : int = 0x000a, speed : int = 0x000a, critchance : int = 0x000a):
        """ Initializes this Stats object. """
        self.hitpoints = hitpoints
        self.magicpoints = magicpoints
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.defense = defense
        self.speed = speed
        self.critchance = critchance

    def __repr__(self):
        """
        String representation of the Stats object.
        Can be used to re-create the object.
        """
        HPS = "0x%04x" % self.hitpoints
        MPS = "0x%04x" % self.magicpoints
        STR = "0x%04x" % self.strength
        DEX = "0x%04x" % self.dexterity
        MGC = "0x%04x" % self.magic
        DFN = "0x%04x" % self.defense
        SPE = "0x%04x" % self.speed
        CRT = "0x%04x" % self.critchance

        return f"HPS:{HPS},MPS:{MPS},STR:{STR},DEX:{DEX},MGC:{MGC},DFN:{DFN},SPE:{SPE},CRT:{CRT}"