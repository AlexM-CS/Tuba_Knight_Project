# Created: 11-22-2024
# Last updated: 12-14-2024

# IO packages:
from IO.Inputs import *
from IO import Window
from IO.Menu import *

# Graphics packages:
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# Built-in packages:

# External packages:

# Internal packages:
import Config
from tubaKnight.Entities.Characters.Stats import Stats
from tubaKnight.Entities.Items import Items
from tubaKnight.Entities.Items.Items import *
from PlayerData.PlayerData import PlayerData
from tubaKnight.Entities.Characters.PlayerCharacter import PlayerCharacter

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

    def getPlayerData(self) -> bool:
        """
        Gets the data for the currently selected player-character,
        and creates new playerData if the given name is not recognized.
        Before doing this, asks the player if they meant to create
        a new character. When a new character is created returns True.
        This return value will be used to automatically start a new Story or not.

        @return: whether a new character was created
        """
        try:
            f = open(f".\\PlayerData\\saveData\\{self.playerName}.txt", "r")

            # Read any potential nicknames from line 1.
            line = f.readline().split("_")
            nick = line[2].strip()

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

            self.playerData = PlayerData(self.playerName, nick, playerLevel, playerExp, playerRegion, playerStats, playerItems)
            f.close()
            return False

        except FileNotFoundError:
            Text(f"Would you like to create a new character named {self.playerName}?").display()
            answer = nextStr(f"[Y]/[N]: ").lower()
            while (answer != "y" and answer != "n"):
                answer = nextStr(f"[Y]/[N] : ").lower()
            if (answer == "y"):
                self.playerData = PlayerData(f"{self.playerName}", f"None")
                return True
            else:
                Text(f"Quitting...").display()
                quit()

        except ValueError:
            print(f"A ValueError occurred")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save(self) -> bool:
        """
        Saves the game. Returns True if the save was successful, and False otherwise.
        @return: whether the save was successful
        """
        try:
            f = open(f".\\PlayerData\\saveData\\{self.playerName}.txt", "w")
            f.write(f"{self.playerData.__repr__()}")
            f.close()
            print(f"Saved successfully.")
            return True
        except:
            print(f"An Error occurred while saving. My sure you don't lose your progress!")
            return False

    def start(self):
        """ Starts the game. """
        # Before running, get this player's data
        newCharacter = self.getPlayerData()
        user = PlayerCharacter(self.playerName, self.playerData)
        menu = Menu(user)
        if (Config.debug):
            Text(f"debug = True", Style("red", "black")).display(sleep = 0.2)
        if (Config.commands_on):
            Text(f"commands_on = True", Style("red", "black")).display(sleep = 0.2)
        if (Config.show_IDs):
            Text(f"show_IDs = True", Style("red", "black")).display(sleep = 0.2)

        # If the user created a new character, automatically load the main story
        pre = 0
        if (newCharacter):
            pre = 1

        # Main game loop
        while True:
            Window.clear()
            # Set the Menu's options to be the Main Menu
            menu.setMenu(0)
            # Gets the user's option from the current Menu
            selection = menu.select(pre = pre)

            # This detects what the player chose to do from the main menu
            match selection:
                case 1: # The user wants to run the main game
                    menu.setMenu(1)

                    while True:
                        Window.clear()
                        selection2 = menu.select(pre = pre)
                        pre = 0

                        match selection2:
                            case 1: # Story
                                pass

                            case 2: # Wander
                                pass

                            case 3: # Travel...
                                pass

                            case 4: # Level Up...
                                Window.clear()
                                before = (f"Current Level: {user.myData.level}\n\n"
                                           f"Current EXP: {user.myData.experience}\n"
                                           f"EXP Needed: {user.getExpNeeded()}\n")
                                menu.options = ("Level Up", "Back...")
                                selection3 = menu.select(before)

                                match selection3:
                                    case 1: # The user wants to level up
                                        success = user.levelUp()
                                        if (success):
                                            Window.clear()
                                            Text(f"========================================\n"
                                                 f"Current Level: {user.myData.level}\n\n"
                                                 f"Leveled Up!\n"
                                                 f"========================================").display(sleep=2)

                                        else:
                                            Window.clear()
                                            Text(f"========================================\n"
                                                 f"{before}\n"
                                                 f"Not enough Experience!\n"
                                                 f"========================================").display(sleep=2)

                                    case 2: # Back..
                                        pass

                                menu.setMenu(1)

                            case 5: # View Items...
                                itemMenu = ItemMenu(user)
                                while True:
                                    Window.clear()
                                    selection3 = itemMenu.select()
                                    # Try converting the input into an integer
                                    # This means the user wants to view an item
                                    try:
                                        selection3 = int(selection3)
                                        selection3 -= 1
                                        if (itemMenu.page > 1):
                                            selection3 += 6
                                        # We should only allow the user to view valid items
                                        maxVal = (36 if itemMenu.page == 0 else 31)
                                        if (selection3 >= 0 and selection3 < maxVal and selection3 in itemMenu.options):
                                            display = (f"========================================\n"
                                                       f"{user.myData.items[selection3].__str__()}\n"
                                                       f"{user.myData.items[selection3].description()}\n\n"
                                                       f"Stats:\n"
                                                       f"{user.myData.items[selection3].stats.__str__()}\n"
                                                       f"========================================")
                                            Text(display).display()
                                            enter_to_continue()
                                            continue

                                    except ValueError:
                                        selection3 = selection3.lower()
                                        match (selection3):
                                            case "a":  # Scroll Left
                                                itemMenu.scroll(-1)

                                            case "d":  # Scroll Right
                                                itemMenu.scroll(1)

                                            case "e":  # Exit the item menu
                                                break

                            case 6: # View Character...
                                Window.clear()
                                display = (f"========================================\n"
                                           f"Name: {user.name}\n"
                                           f"Nickname: {user.myData.nick}\n"
                                           f"Stats:\n"
                                           f"   Level: {user.myData.level}\n"
                                           f"   Experience: {user.myData.experience}\n"
                                           f"{user.myData.stats.__str__()}\n"
                                           f"Weapon: {user.myData.items[0].name}\n"
                                           f"========================================")
                                Text(display).display()
                                enter_to_continue()
                                continue

                            case 7: # Back...
                                break

                case 2: # The user wants to save their progress
                    menu.setMenu(2)
                    while True:
                        selection2 = menu.select()
                        if (selection2 == 3): # Back...
                            break
                        else: # 1 - Save ; 2 - Save and Quit
                            self.save()
                            Window.clear()
                            if (selection2 == 2):
                                quit()

if __name__ == "__main__":
    tk = TubaKnight("Alex")
    tk.start()