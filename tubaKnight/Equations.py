# Created: 12-2-2024
# Last updated: 12-2-2024

# IO packages:

# Graphics packages:

# Built-in packages:
import random
import math

# External packages:

# Internal packages:
from Entities.Characters.PlayerCharacter import PlayerCharacter
from Entities.Characters.Enemies import Enemy
from Entities.Items.Items import Item

# This file contains equations/calculations used throughout the game

def attack(attacker : PlayerCharacter | Enemy, defender : PlayerCharacter | Enemy, weapon : Item):
    # Damage formula:
    # NOTE: This damage formula was adapted from that of the Pokemon games. The Pokemon damage
    #       formula can be found using the link in the file Sources_and_Research.
    # Damage Dealt = ((2 * AtkLevel/ 5 + 2) * Power * ATK / (2 * DfnLevel + DFN) / 50 + 2) * (Degree / 2) * Crit * Roll
    #
    # AtkLevel - The level of the attacker.
    # Power - The attack stat of the attacker's weapon
    # ATK - The attacker's attacking stat
    # DfnLevel - The level of the defender
    # DFN - The defender's defense stat
    # Degree - the degree of the attacker's weapon
    # Crit - 2 if the attack is a critical hit, and 1 otherwise.
    # Roll - A random constant between 0.9 and 1.1, rounded to 3 digits.
    #
    # After this calculation is run, the result is truncated to an integer.
    # ==========================================================================================
    # NOTE: The ATK variable used in this calculation depend on the user.
    #       It can be either STR, DEX, or MGC, and will be chosen from
    #       these three depending on which is the largest.
    #       Similarly, the Power variable is based on the user's weapon.
    #       However, the weapon stat used will match the one chosen for
    #       the ATK variable.
    # ==========================================================================================
    # Example: Player Level = 5
    #          Player's Weapon's STR = 10
    #          Player's STR = 10
    #          Enemy's Level = 20
    #          Enemy's Defense = 50
    #          Player's Weapon's Degree = 10
    #          Crit = 1 (The player's attack did not crit)
    #          Roll = 1.1 (The player's attack did the max damage)
    #
    # Damage Dealt = ((2 * 5 / 5 + 2) * 10 * 10 / (2 * 20 + 50) / 50 + 2) * (10 / 2) * 1 * 1.1
    #              = ((2 * 1 + 2) * 10 * 10 / (40 + 50) / 50 + 2) * 5 * 1.1
    #              = ((2 + 2) * 100 / 90 / 50 + 2) * 5 * 1.1
    #              = (4 * 100 / 90 / 50 + 2) * 5.5
    #              = (400 / 90 / 50 + 2) * 5.5
    #              = (4.44... / 50 + 2) * 5.5
    #              = (0.088... + 2) * 5.5
    #              = 2.088... * 5.5
    #              = 11.488...
    #              = 11 (truncated)
    # ==========================================================================================

    # We'll use this to decide which stat of the attacker's to use
    attackerStats = [attacker.stats.strength, attacker.stats.dexterity, attacker.stats.magic]

    # First, get the attacker's level
    atkLevel = attacker.level

    # Second, get the highest value from the attackerStats list
    ATK = max(attackerStats)

    # We index the grid to see which of the stats was chosen
    # While doing this, we also get the weapon degree
    if (attackerStats.index(ATK) == 0): # Strength stat
        if (isinstance(attacker, PlayerCharacter)):
            # If the attacker is a player, index their "items" field at 0 to get their weapon
            power = attacker.myData.items[0].stats.strength
            degree = attacker.myData.items[0].stats.degree
        else:
            # If the attack is an enemy, access their "weapon" field to get their weapon
            power = attacker.weapon.stats.strength
            degree = attacker.weapon.stats.degree
    elif (attackerStats.index(ATK) == 1): # Dexterity stat
        if (isinstance(attacker, PlayerCharacter)):
            power = attacker.myData.items[0].stats.dexterity
            degree = attacker.myData.items[0].stats.degree
        else:
            power = attacker.weapon.stats.dexterity
            degree = attacker.weapon.stats.degree
    else: # Magic stat
        if (isinstance(attacker, PlayerCharacter)):
            power = attacker.myData.items[0].stats.magic
            degree = attacker.myData.items[0].stats.degree
        else:
            power = attacker.weapon.stats.magic
            degree = attacker.weapon.stats.degree

    # Next, collect the defender's level
    dfnLevel = defender.level

    # Next, the defender's defense
    DFN = defender.stats.defense

    # Use a random roll to decide if the attack crits or not
    critRoll = random.randrange(0, 1001)
    if (critRoll > attacker.stats.critchance):
        crit = 1
    else:
        crit = 2

    # Last, every attack is affected by a random roll from 9.9 to 1.1.
    roll = round(random.triangular(0.9, 1.1), 3)

    # Finally, calculate the total damage
    damage = ((2 * atkLevel/ 5 + 2) * power * ATK / (2 * dfnLevel + DFN) / 50 + 2) * (degree / 2) * crit * roll

    # Return the total damage, truncated to an integer
    return math.trunc(damage)