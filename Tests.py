# Created: 11-23-2024
# Last updated: 11-23-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from TubaKnight import *
from Structures.EntityLists import ItemList, EquipmentList

"""
This file contains tests used while writing the code for this project.
"""

def test1_saving():
    name = input("What is your name?: ")
    tk = TubaKnight(name)
    tk.getPlayerData()
    tk.save()

def test2_ItemList():
    list1 = EquipmentList(5)
    list1.weapon = Item(1)
    print(list1.__repr__())