# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:

class Structure:
    """
    Description:
    The Structure class is used to define a structure type for the
    game, usually in the form of a collection. All Structures are
    static typed, and have no random access by default.

    Fields:
    class type dataType: the dataType of this structure.
    int maxSize: the maxSize of this structure, if any
    list[dataType] content: the contents of this structure.
    """
    dataType = None
    maxSize = None
    content = list()

    def __init__(self, dataType, maxSize : int = None, content : list = None):
        """
        Initializes this structure

        Args:
            class type dataType: the dataType for this structure
            int maxSize: the maxSize for this structure
            list[dataType] content: the contents of this structure
        """
        self.dataType = dataType
        self.maxSize = maxSize
        self.content = content

    def add(self, item) -> bool:
        """ Adds an item to the end of this Structure """
        if (type(item) != self.dataType):
            return False
        else:
            self.content.append(item)
            return True

    # Displays the contents of this Structure
    def __repr__(self):
        return f"{self.content.__repr__()}"