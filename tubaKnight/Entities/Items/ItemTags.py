# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from Items import ITEM_NAMES

ITEM_TAGS = ["Dummy", "Weapon", "Passive", "Percussive", "Brass", "Stringed", "Soothing", "Heavy", "Jazzy"]

def addTagsToItemByID(ID : int) -> list[str]:
    """ Creates a list of tags based on an Item ID. """
    if (ID >= len(ITEM_NAMES)):
        raise IndexError("Item ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Item IDs may not be negative.")
    tags = list()
    match (ID):
        case 0:
            tags.append(addTagByID(0))
        case 1:
            tags.append(addTagByID(1))
            tags.append(addTagByID(3))
    return tags

def addTagByID(ID : int) -> str:
    """ Adds a specified tag to an item. """
    if (ID >= len(ITEM_TAGS)):
        raise IndexError("Tag ID exceeds maximum.")
    elif (ID < 0):
        raise IndexError("Tag IDs may not be negative.")
    return ITEM_TAGS[ID]