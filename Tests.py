# Created: 11-23-2024
# Last updated: 12-11-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from TubaKnight import *

# This file contains tests used while writing the code for this project.

def test1_saving():
    name = input("What is your name?: ")
    tk = TubaKnight(name)
    tk.getPlayerData()
    tk.save()

def test3_Menus():
    name = input(f"What is your name?: ")
    tk = TubaKnight(name)
    tk.start()