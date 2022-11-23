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
def drawBottom(question, cardList):
    screen = [" "] * 12
    screen[0] += question
    for i in range(7):
        try:
            screen[i + 1] += colored(" " + cardList[i].name + " ", attrs=pointer[i])
        except:
            ""
    clear()
    for str in screen:
        print(str)

def loop(question, cardList):
    nbLine = len(cardList)
    global pointer
    pointer = [[]] * nbLine
    line = 0
    while True:
        sleep(.1)
        pointer[line] = ["reverse"]
        drawBottom(question, cardList)
        pointer[line] = []
        key = keyboard.read_key()
        if key == "down" and line != nbLine - 1:
            line += 1
        elif key == "up" and line != 0:
            line -= 1
        elif key == "enter":
            print("\033[1A", end="")
            return cardList[line]
        elif key == "esc":
            return esc()

# Class used to escape from the loop
class esc:
    def __init__(self):
        self.number = 0

