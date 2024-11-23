# Created: 11-22-2024
# Last updated: 11-22-2024

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
            line = f.readline()

            # Line 2 format:
            # Stats_LVL:0x0000,EXP:0x0000,HPS:0x0000,MPS:0x0000,STR:0x0000,DEX:0x0000,MGC:0x0000,DFN:0x0000,SPE:0x0000,CRT:0x0000
            line = f.readline()[6:].strip().split(",")
            for i in range(0, len(line)):
                line[i] = line[i][4:]
            level = int(line[0], 16)
            experience = int(line[1], 16)
            stats = Stats(int(line[2], 16), int(line[3], 16), int(line[4], 16), int(line[5], 16), int(line[6], 16), int(line[7], 16),
                          int(line[8], 16), int(line[9], 16))

            # Line 3 format:
            # ItemIDs_HELD:0x0000,ITM1:0x0000,ITM2:0x0000,ITM3:0x0000,ITM4:0x0000,ITM5:0x0000
            line = f.readline()[8:]
            line = line.strip().split(",")
            for i in range(0, len(line)):
                print(line[i])
                line[i] = line[i][5:]
            weapon = Item(int(line[0], 16))
            print(Items.getName(weapon.ID))
            items = [Item(int(line[1], 16)), Item(int(line[2], 16)), Item(int(line[3], 16)), Item(int(line[4], 16)), Item(int(line[5], 16))]
            self.playerData = PlayerData(f"{self.playerName}", level, experience, stats, weapon, items)
            print(self.playerData.__repr__())
            f.close()

        except FileNotFoundError:
            Text(f"Would you like to create a new character named {self.playerName}?").display()
            answer = nextStr(f"[Y]/[N] : ")
            while (answer.lower() != "y" and answer.lower() != "n"):
                answer = nextStr(f"[Y]/[N] : ")
            if (answer == "Y"):
                self.playerData = PlayerData(f"{self.playerName}")
            else:
                Text(f"Returning to main menu...").display()
                quit()
        except ValueError:
            print(f"A ValueError occurred")

    def save(self) -> bool:
        try:
            f = open(f".\\PlayerData\\saveData\\{self.playerName}.txt", "w")
            f.write(f"{self.playerData.__repr__()}\n"
                    f"ItemIDs_HELD:0x0001,ITM1:0x0000,ITM2:0x0000,ITM3:0x0000,ITM4:0x0000,ITM5:0x0000\n"
                    f"RegionID_0x00\n"
                    f"InvItem_0x0000")
            print(f"Saved successfully.")
            return True
        except:
            print(f"An Error occurred while saving. My sure you don't lose your progress!")
            return False

    def play(self):
        """ Runs the game. """
        pass