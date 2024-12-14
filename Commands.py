# Created: 11-22-2024
# Last updated: 12-14-2024

# IO packages:

# Graphics packages:

# Built-in packages:
from argparse import ArgumentError

# External packages:

# Internal packages:
from tubaKnight.Entities.Characters.PlayerCharacter import PlayerCharacter

# This file contains various commands that can be used while playing the game

commandList = [
    "setStat",
    "giveItem"
]

def setStat(user : PlayerCharacter, stat : str, value : int) -> None:
    """
    Sets the user's given stat to the given value.
    @param user: the user to edit
    @param stat: the stat to edit
    @param value: the value to change the stat to
    """
    match (stat):
        case "LVL":
            user.myData.level = value
        case "EXP":
            user.myData.experience = value
        case "HPS":
            user.myData.stats.hitpoints = value
        case "MPS":
            user.myData.stats.magicpoints = value
        case "STR":
            user.myData.stats.strength = value
        case "DEX":
            user.myData.stats.dexterity = value
        case "MGC":
            user.myData.stats.magic = value
        case "DFN":
            user.myData.stats.defense = value
        case "SPD":
            user.myData.stats.speed = value
        case "CRT":
            user.myData.stats.critchance = value
        case _:
            raise ArgumentError(None, f"Illegal Argument: {stat}")