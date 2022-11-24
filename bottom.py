import sys
import os
from termcolor import colored
import keyboard
from time import sleep

# Get the size of the terminal
termSize = os.get_terminal_size()

# Clear the bottom of the screen
def clear():
    for i in range(12):
        print("\x1b[2K", end="")
        print("\033[1A", end="")
    print("\r\x1b[2K", end="")

# Draw the board
def drawBottom(question, choiceList, pl):
    line = pointer.index(["reverse"])
    screen = [""] * 12
    if len(pl.hand) > 9:
        handSize = str(len(pl.hand)) + " cartes en main: "
    else:
        handSize = str(len(pl.hand)) + " cartes en main:  "
    screen[0] += " " + question + "│" + " " * (termSize[0] - 140) + "│" + handSize + "│"
    for i in range(11):
    # Draw the choice list
        try:
            screen[i + 1] += colored(" " + choiceList[i].name , attrs=pointer[i])
            if choiceList[i].__class__.__name__ != "choice":
                screen[i + 1] += "                                         "
                if choiceList[i].__class__.__name__ == "player":
                    screen[i + 1] += "    "
            screen[i + 1] += "│" + " " * (termSize[0] - 140)  + "│"
        except:
            screen[i + 1] += "                                                           │" + " " * (termSize[0] - 140)  + "│"
    # Draw the hand
        try:
            screen[i + 1] += str(pl.hand[i].cost) + " " + pl.hand[i].name + "│"
        except:
            screen[i + 1] += "                   │"
    # Draw the effect of a district card
    if choiceList[line].__class__.__name__ == "district":
        screen[0] += f" {choiceList[line].name}:"
        screen[1] += f" Coût de construction {choiceList[line].cost}:"
        screen[3] += " " + choiceList[line].effect[0]
        screen[4] += " " + choiceList[line].effect[1]
        screen[5] += " " + choiceList[line].effect[2]
    # Draw the effect of a character card
    elif choiceList[line].__class__.__name__ == "character":
        screen[0] += " " + choiceList[line].name
        screen[2] += " " + choiceList[line].effect[0]
        screen[3] += " " + choiceList[line].effect[1]
        screen[4] += " " + choiceList[line].effect[2]
    # Print the bottom of the screen
    clear()
    for string in screen:
        print(string)

def loop(question, choiceList, pl):
    nbLine = len(choiceList)
    global pointer
    pointer = [[]] * nbLine
    line = 0
    while True:
        sleep(.2)
        pointer[line] = ["reverse"]
        drawBottom(question, choiceList, pl)
        pointer[line] = []
        key = keyboard.read_key()
        if key == "down" and line != nbLine - 1:
            line += 1
        elif key == "up" and line != 0:
            line -= 1
        elif key == "enter":
            print("\033[1A", end="")
            return choiceList[line]
        elif key == "esc":
            return esc()

# Class used to escape from the loop
class esc:
    def __init__(self):
        self.number = 0

