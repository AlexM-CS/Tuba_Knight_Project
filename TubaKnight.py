# Created: 11-22-2024
# Last updated: 11-26-2024

# IO packages:
from IO.Inputs import *
from IO import Window

# Graphics packages:
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# Built-in packages:

# External packages:

# Internal packages:
from tubaKnight.Entities.Characters.Stats import Stats
from tubaKnight.Entities.Items import Items
from tubaKnight.Entities.Items.Items import *
from PlayerData.PlayerData import PlayerData

class TubaKnight:
    """
    Description:
    The TubaKnight class runs the game, and controls everything going on.

    Fields:
    str version - the current version of the game
    str playerName - the name of the player-character
    PlayerData playerData - the data of the player-character
    """
    playerName = None
    playerData = None

    def __init__(self, playerName : str):
        """ Initializes a game of TubaKnight. """
        self.playerName = playerName
        self.playerData = None

    def getPlayerData(self):
        """
        Gets the data for the currently selected player-character,
        and creates new playerData if the given name is not recognized.
        Before doing this, asks the player if they meant to create
        a new character.
        """
        try:
            f = open(f".\\PlayerData\\saveData\\{self.playerName}.txt", "r")

            # Skip line 1. It is meant for reading, not for data.
            f.readline()

            # Line 2 describes the player's stats, so we need to read it and parse the stats accordingly.
            # Slice from 6 to the end to get rid of the "Stats_" at the beginning.
            line = f.readline()[6:]
            line = line.split(",")
            stats = list()
            for i in range(0, len(line)):
                # Slice from 4 to the end to get rid of the stat's name,
                # as it is meant for reading.
                stats.append(int(line[i][4:], 16))

            playerLevel = stats[0]
            playerExp = stats[1]
            playerStats = Stats(stats[2], stats[3], stats[4], stats[5], stats[6], stats[7], stats[8], stats[9])

            # Line 3 describes the Area to be loaded when starting.
            # Slice from 9 to the end to get rid of the "RegionID_" at the beginning.
            line = f.readline()[9:]
            playerRegion = int(line, 16)

            # Skip line 4. It is meant for reading, not for data.
            f.readline()

            # Lines 5-40 are meant for reading in items.
            playerItems = {}

            for i in range(0, 36):
                # Slice from 5 to the end to get rid of the "HELD_" or "ITMX_" tags at the beginning.
                line = f.readline()[5:]
                line = line.split(",")
                playerItems[i] = Item(int(line[0][4:], 16), int(line[1][4:], 16), int(line[2][4:], 16))

            self.playerData = PlayerData(self.playerName, playerLevel, playerExp, playerRegion, playerStats, playerItems)
            f.close()

        except FileNotFoundError:
            Text(f"Would you like to create a new character named {self.playerName}?").display()
            answer = nextStr(f"[Y]/[N]: ").lower()
            while (answer!= "y" and answer != "n"):
                answer = nextStr(f"[Y]/[N] : ").lower()
            if (answer == "y"):
                self.playerData = PlayerData(f"{self.playerName}")
            else:
                Text(f"Returning to main menu...").display()
                quit()

        except ValueError:
            print(f"A ValueError occurred")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save(self) -> bool:
        try:
            f = open(f".\\PlayerData\\saveData\\{self.playerName}.txt", "w")
            f.write(f"{self.playerData.__repr__()}")
            f.close()
            print(f"Saved successfully.")
            return True
        except:
            print(f"An Error occurred while saving. My sure you don't lose your progress!")
            return False

    def play(self):
        """ Runs the game. """
        pass