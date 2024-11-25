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

class TempStats(Stats):
    """
    Description:
    The TempStats class is a temporary version of the Stats class,
    meant to be altered during battles.
    """
    def __init__(self, hitpoints : int = 0x000a, magicpoints : int = 0x000a, strength : int = 0x000a, dexterity : int = 0x000a,
                 magic : int = 0x000a, defense : int = 0x000a, speed : int = 0x000a, critchance : int = 0x000a):
        """ Initializes this TempStats object. """
        super().__init__(hitpoints, magicpoints, strength, dexterity, magic, defense, speed, critchance)

    def buff(self, stat : str, amount : int, isMultiplier : bool = False) -> int:
        """ Buffs the given stat by the given amount. """
        match (stat):
            case "HPS":
                if (isMultiplier):
                    self.hitpoints *= amount
                    return self.hitpoints
                self.hitpoints += amount
                return self.hitpoints
            case "MPS":
                if (isMultiplier):
                    self.magicpoints *= amount
                    return self.magicpoints
                self.magicpoints += amount
                return self.magicpoints
            case "STR":
                if (isMultiplier):
                    self.strength *= amount
                    return self.strength
                self.strength += amount
                return self.strength
            case "DEX":
                if (isMultiplier):
                    self.dexterity *= amount
                    return self.dexterity
                self.dexterity += amount
                return self.dexterity
            case "MGC":
                if (isMultiplier):
                    self.magic *= amount
                    return self.magic
                self.magic += amount
                return self.magic
            case "DFN":
                if (isMultiplier):
                    self.defense *= amount
                    return self.defense
                self.defense += amount
                return self.defense
            case "SPE":
                if (isMultiplier):
                    self.speed *= amount
                    return self.speed
                self.speed += amount
                return self.speed
            case "CRT":
                if (isMultiplier):
                    self.critchance *= amount
                    return self.critchance
                self.critchance += amount
                return self.critchance
            case _:
                raise ValueError(f"Invalid stat: {stat}")

    def alter(self, stat : str, amount : int) -> None:
        """ Sets the given stat to the given amount. """
        match (stat):
            case "HPS":
                self.hitpoints = amount
            case "MPS":
                self.magicpoints = amount
            case "STR":
                self.strength += amount
            case "DEX":
                self.dexterity += amount
            case "MGC":
                self.magic = amount
            case "DFN":
                self.defense = amount
            case "SPE":
                self.speed = amount
            case "CRT":
                self.critchance = amount
            case _:
                raise ValueError(f"Invalid stat: {stat}")

    def damageThis(self, amount : int) -> bool:
        """ Damages the given amount. """
        isDead = False
        self.hitpoints -= amount
        isDead = self.hitpoints <= 0
        return isDead

    def cast(self, amount : int) -> bool:
        """ Casts a skill using magicpoints. Return value indicates if the cast is successful. """
        allowed = True
        if (self.magicpoints - amount < 0):
            allowed = False
        else:
            self.magicpoints -= amount
        return allowed