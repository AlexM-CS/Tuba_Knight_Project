# Created: 11-22-2024
# Last updated: 11-27-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:
from abc import abstractmethod

# Internal packages:
from Tuba_Knight_Project import Config

"""
Static Fields:
int IDLE - indicates that this Entity is idle
int BATTLING - indicates that this Entity is battling
int DEAD - indicates that this Entity is dead
int MENU - the user is in a menu
int CUTSCENE - the user is in a cutscene
"""

IDLE = 0
BATTLING = 1
DEAD = 2
MENU = 3
CUTSCENE = 4

class Entity:
    """
    Description:
    An Entity is an interactable object within the game.
    All entities have a method of interacting with them, which
    will be specified in subclasses.

    Fields:
    int ID - the ID of this entity
    str name - the name of the entity
    """
    name = None
    ID = None
    state = None

    def __init__(self, ID : int):
        """ Initializes this entity. """
        self.ID = ID
        self.name = f"Entity {self.ID}"
        self.state = IDLE

    def __repr__(self):
        """ Returns the type and ID of this Entity. """
        if (Config.show_IDs):
            return f"TYPE:{type(self)},ID:{self.ID}"
        else:
            return f"{self.name}"

    @abstractmethod
    def act(self):
        """
        Performs this entity's action.
        To be overridden by subclasses.
        """
        raise NotImplementedError("This entity does not implement act()")

    def setState(self, state : int):
        """ Sets this entity's state. """
        self.state = state