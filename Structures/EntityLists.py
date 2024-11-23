# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages

# External packages:

# Internal packages:
from . import Structure
from ..tubaKnight.Entities import Entity
from ..tubaKnight.Entities.Characters import Enemies as TYPE_ENEMY
from ..tubaKnight.Entities.Characters.Enemies import Enemy
from ..tubaKnight.Entities.Items import Items as TYPE_ITEM
from ..tubaKnight.Entities.Items.Items import Item

class EntityList(Structure):
    """
    A list of Entity objects, stored as a structure.
    Allows for random access.
    """
    def __init__(self, dataType=Entity):
        """ Initializes this EntityList. """
        super().__init__(dataType)

    def __getitem__(self):
        """ Gets an item from this list. """
        self.content.__getitem__(self)

class EnemyList(EntityList):
    """
    A list of Enemy objects.
    """
    def __init__(self):
        """ Initializes this EnemyList. """
        super().__init__(TYPE_ENEMY)

class ItemList(EntityList):
    """
    A list of Item objects.
    """
    def __init__(self):
        """ Initializes this ItemList. """
        super().__init__(TYPE_ITEM)