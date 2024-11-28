# Created: 11-27-2024
# Last updated: 11-27-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:

PATHS = {
    0 : ""
}

class Area:
    """
    Description:

    Fields:
    int ID - the ID of this Area
    str name - the name of this Area
    str path - the filepath this area will save and load to
    """
    ID = None
    name = None
    path = None

    def __init__(self, ID : int, name : str):
        self.ID = ID
        self.name = name
        self.path = PATHS[ID]

    def __str__(self):
        """
        Returns the name of this Area.
        Used during gameplay.
        """
        return f"{self.name}"

    def __repr__(self):
        """
        Returns the RegionID of this Area.
        Used when saving.
        """
        RGNID = "0x%02x" % self.ID
        return f"RegionID_{RGNID}"

    def load(self):
        pass

    def save(self):
        pass