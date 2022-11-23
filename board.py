import sys
import os
from termcolor import colored
import keyboard
from time import sleep

# Get the size of the terminal
termSize = os.get_terminal_size()

# Clear the screen
def clear():
    os.system("clear")

# Draw the board
def draw(playerList, nbPlayer, discardList, line, column):
    # Create the pointer to highlight an item of the board
    pointer = []
    for i in range(12):
        pointer.append([[]] * nbPlayer)
    
    if line >= 0 and line <= 11 and column >=0 and column <= nbPlayer - 1:
        pointer[line][column] = ["reverse"]
 

    # Use a number of blank space calculated from the terminal size to center the board
    screen = [" " * int(((termSize[0] - (20 * nbPlayer)) / 2))] * (termSize[1] - 2)
    screen[0] += "up"
    screen[9]  += ("┌" + ("─" * 19 + "┬") * nbPlayer)[:-1] + "┐"
    screen[10] += "│"
    screen[11] += ("├" + ("─" * 19 + "┼") * nbPlayer)[:-1] + "┤"
    screen[12] += "│"
    screen[13] += ("├" + ("─" * 19 + "┼") * nbPlayer)[:-1] + "┤"
    screen[14] += "│"
    screen[15] += "│"
    screen[16] += ("├" + ("─" * 19 + "┼") * nbPlayer)[:-1] + "┤"
    screen[17] += "│"
    screen[18] += "│"
    screen[19] += "│"
    screen[20] += "│"
    screen[21] += "│"
    screen[22] += "│"
    screen[23] += "│"
    screen[24] += "│"
    screen[25] += "│"
    screen[26] += ("└" + ("─" * 19 + "┴") * nbPlayer)[:-1] + "┘"
    
    # Add bottom line to screen
    if ["reverse"] in pointer[11]:
        screen[termSize[1] - 15] = colored("-" * termSize[0], attrs=["reverse"])
    else:
        screen[termSize[1] - 15] = "-" * termSize[0]
    # Add players and city to screen
    for j in range(nbPlayer):
        pl = playerList[j]
        # Handle the name of the player
        crown = "     "
        if pl.isking:
            crown = colored(" Roi ", "yellow")
        name = colored(" " + playerList[j].name + crown, attrs=pointer[0][j])
        # Handle the character card of the player
        char = playerList[j].character
        if char == None:
            char = "                   "
        elif char.revealed == False:
            char = " xxxxxxxxxxxxxxxxx "
        else:
            char = " " + char.name
        char = colored(char, attrs=pointer[1][j])
        # Handle number of cards in hand and gold of the player
        handsize = len(playerList[j].hand)
        if handsize > 9:
            handsize = str(handsize) + " cartes en main  "
        else:
            handsize = str(handsize) + " cartes en main   "
        # Handle gold of the player
        gold = playerList[j].gold
        if gold > 9:
            gold = str(gold) + " pièces d'or     "
        else:
            gold = str(gold) + " pièces d'or      "
        # Add name, handsize and gold to the screen
        screen[10] += name + "│"
        screen[12] += char + "│"
        screen[14] += handsize + "│"
        screen[15] += gold + "│"
        # Add the city of the player to the screen
        for i in range(9):
            try:
                di = playerList[j].city[i]
                di = colored(str(di.cost) + " " + di.name, attrs=pointer[i + 2][j])
            except IndexError:
                di = colored("                   ", attrs=pointer[i + 2][j])
            screen[17 + i] += di + "│"
    # Add the discard list to the screen
    screen[27] += "Discard List :"
    screen[28] += " xxxxxxxxxxxxxxxxx "
    try: 
        screen[29] += discardList[1][0].name
        screen[30] += discardList[1][1].name
    except:
        ""
    clear()
    for s in screen:
        print(s)

def loop(plList, nbPlayer, discardList):
    line = 0
    column = 0
    while True:
        draw(plList, nbPlayer, discardList, line, column)
        sleep(.1)
        key = keyboard.read_key()
        if key == "down" and line != 11:
            line += 1
        elif key == "up" and line != 0:
            line -= 1
        elif key == "right" and column != nbPlayer - 1:
            column += 1
        elif key == "left" and column != 0:
            column -= 1
        elif key == "enter" and line == 11:
            print("\033[1A", end="")
            break
        elif key == "esc":
            break
