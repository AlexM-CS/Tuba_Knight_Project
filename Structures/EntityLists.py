# Created: 11-22-2024
# Last updated: 11-24-2024

# IO packages:

# Graphics packages:

# Built-in packages
from argparse import ArgumentError

# External packages:

# Internal packages:
from Tuba_Knight_Project.tubaKnight.Entities.Entity import *
from Tuba_Knight_Project.tubaKnight.Entities.Characters.Enemies import Enemy
from Tuba_Knight_Project.tubaKnight.Entities.Items.Items import Item

class EntityList:
    """
    Description:
    A list of Entity objects.

    Fields:
    int maxSize - the maxSize of this structure, if any
    list[dataType] - content: the contents of this structure.
    """
    maxSize = None
    content = list()

    def __init__(self, maxSize : int = None, content : list[Entity] = None):
        """ Initializes this EntityList. """
        self.maxSize = maxSize
        self.content = content

    def __getitem__(self, index : int):
        """ Gets an item from this list. Positive indexing only. """
        if (index >= self.maxSize or index >= len(self.content) or index < 0):
            raise IndexError(f"Index out of range.")
        else:
            self.content.__getitem__(index)

    def add(self, item : Entity, index : int = None) -> bool:
        """ Adds an item to the end of this EntityList. """
        if (index is not None):
            self.content.insert(index, item)
        else:
            self.content.append(item)
        return True

    def __repr__(self):
        return f"{self.content.__repr__()}"

class EnemyList(EntityList):
    """
    Description:
    A list of Enemy objects.
    """
    def __init__(self, maxSize : int = None, content : list[Enemy] = None):
        """ Initializes this EnemyList. """
        super().__init__(maxSize, content)

    def add(self, enemy : Enemy, index : int = None) -> bool:
        """ Adds an enemy to the end of this EnemyList. """
        return super().add(enemy, index)

class ItemList(EntityList):
    """
    Description:
    A list of Item objects.
    """
    def __init__(self, maxSize : int = None, content : list[Item] = None):
        """ Initializes this ItemList. """
        super().__init__(maxSize, content)

    def add(self, item : Item, index : int = None) -> bool:
        """ Adds an item to the end of this ItemList. """
        return super().add(item, index)

class EquipmentList(ItemList):
    """
    Description:
    A list of Item objects.
    Represents the player's equipped items.
    Requires a max size, with a separate field for held weapon.

    Fields:
    Item weapon - the player's held weapon
    """
    weapon = None

    def __init__(self, maxSize : int, content : list[Item] = None):
        """ Initializes this EquipmentList. """
        self.weapon = None

        if (content is not None):
            if (len(content) > self.maxSize):
                raise ArgumentError(None, f"The given list is too large.")
            else:
                super().__init__(maxSize, content)

        else:
            self.content = list()
            for i in range(0, maxSize):
                self.content.append(None)

    def add(self, item : Item, index : int = None) -> bool:
        if (len(self.content) == self.maxSize):
            return False
        elif (index >= self.maxSize or index < 0):
            raise IndexError(f"Index must be within {self.maxSize}.")
        else:
            return super().add(item, index)

    def setItem(self, item, index : int) -> bool:
        """ Sets an item at a specific index. """
        if (index >= self.maxSize or index < 0):
            raise IndexError(f"Index must be within {self.maxSize}.")
        else:
            self.content.__setitem__(index, item)
        return True

    def __repr__(self):
        """ Displays this EquipmentList. Also used when saving. """
        WPN = self.weapon.__repr__()
        if (self.content[0] is not None):
            ITM1 = self.content[0].__repr__()
        else:
            ITM1 = Item(0).__repr__()
        if (self.content[1] is not None):
            ITM2 = self.content[1].__repr__()
        else:
            ITM2 = Item(0).__repr__()
        if (self.content[2] is not None):
            ITM3 = self.content[2].__repr__()
        else:
            ITM3 = Item(0).__repr__()
        if (self.content[3] is not None):
            ITM4 = self.content[3].__repr__()
        else:
            ITM4 = Item(0).__repr__()
        if (self.content[4] is not None):
            ITM5 = self.content[4].__repr__()
        else:
            ITM5 = Item(0).__repr__()

        return f"Items_\nHELD_{WPN}\nITM1_{ITM1}\nITM2_{ITM2}\nITM3_{ITM3}\nITM4_{ITM4}\nITM5_{ITM5}"