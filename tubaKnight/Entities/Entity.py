# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from Tuba_Knight_Project import Config

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

    def __init__(self, ID : int):
        """
        Initializes this entity

        Args:
            str name - the name for this entity
            int ID - the ID for this entity
        """
        self.ID = ID
        self.name = f"Entity {self.ID}"

    def __repr__(self):
        """
        Returns the ID of this entity when debugging.
        Returns the name of this entity during gameplay.
        """
        if (Config.debug):
            return f"{type(self)} {self.ID}"
        else:
            return self.name

    def act(self):
        """
        Performs this entity's action.
        To be overridden by subclasses.
        """
        raise NotImplementedError("This entity does not implement act()")