# Created: 11-22-2024
# Last updated: 12-11-2024

# IO packages:

# Graphics packages:

# Built-in packages
from argparse import ArgumentError

# External packages:

# Internal packages:
from tubaKnight.Entities.Entity import *
from tubaKnight.Entities.Characters.Enemies import Enemy

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