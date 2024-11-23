# Created: 11-21-2024
# Last updated: 11-21-2024

# IO packages:
from Tuba_Knight_Project.IO.Inputs import enter_to_continue

# Graphics packages:
from .Style import Style

# Built-in packages:
from time import time_ns, time

# External packages:
from rich.console import Console

# Internal packages:

class Text:
    """
    Description:
    Used to display Text on the terminal screen.

    Fields:
    str contents - the text to write on the terminal
    Style style - the Style used when writing contents
    float speed - the speed used when displaying this text
    """
    contents = None
    style = None
    speed = None

    def __init__(self, contents = "default", style = Style(), speed = 0):
        """ Initializes the Text object with the given attributes. """
        self.contents = contents
        self.style = style
        self.speed = speed

    def display(self, enter_prompt : bool = False):
        """ Displays this Text according to the contents and style. """
        if (self.speed > 0):
            startTime = time()
            i = 0
            while (i < len(self.contents)):
                if ((time_ns() - startTime) > self.speed):
                    Console().print(f"{self.style}{self.contents[i]}", end = "")
                    i += 1
        else:
            Console().print(f"{self.style}{self.contents}")

        if (enter_prompt):
            enter_to_continue()
            pass