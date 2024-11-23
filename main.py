# Created: 11-22-2024
# Last updated: 11-22-2024

# IO packages:

# Graphics packages:

# Built-in packages:

# External packages:

# Internal packages:
from TubaKnight import *

def main():
    name = input("What is your name?: ")
    tk = TubaKnight(name)
    tk.getPlayerData()
    tk.save()

if __name__ == "__main__":
    main()