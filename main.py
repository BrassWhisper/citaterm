import csv
from sys import argv
from time import sleep
import random as rand
import os

import deck 
import characters
import player

START_GOLD = 2
START_HAND = 4

def main():
    nbPlayer = 7
    # Initialize global variable deck.districts characters.list and player.list
    deck.init()             # Create deck.districts
    characters.init()       # Create characters.list
    player.init(nbPlayer)   # Create player.list

    # Shuffle the deck
    rand.shuffle(deck.districts)

    # Make a random player the king
    rand.choice(player.list).isking = True

    # Make the players draw and get their gold
    for p in player.list:
        p.hand = deck.draw(START_HAND)
        p.gold = START_GOLD

   # Main loop
    while True:
        # Refresh the character list
        characters.init()
        # Loop to find the king
        for i in range(nbPlayer):
            if player.list[i].isking:
                break

        # Discard a number of character cards based on the number of players
        discardList = discard(nbPlayer)

        # Players choose their character beginning by the king and clockwise
        for j in range(nbPlayer):
            # If j == 6 that mean there is 7 players and this is the last choice, we add the face down character to the character.list according to rules
            if j == 6:
                characters.list.append(discardList[0])
            # Player of index i gets to choose his character
            choose(i)
            i += 1
            # Go back to the beggining of the player list
            if i == nbPlayer:
                i = 0
            clearBottom(9)
        
        # Decide which player has to play based on the character they pick
        for i in range(1, 9):
            for pl in player.list:
                if pl.character.number == i and pl.character.murdered == False:
                    turn(pl)
        drawBoard()

        break

# Discard a number of character cards based on the number of players, return a list with the face down at index 0 and the face up at index 1
def discard(n):
    # Always discard one character face down
    discardList = [rand.choice(characters.list), [None, None]]
    characters.list.remove(discardList[0])
    # If 4 or 5 players, one discarded face up
    if n <= 5:
        discardList[1][0] = rand.choice(characters.list)
        characters.list.remove(discardList[1][0])
    # If 4 players, one more discarded face up
    if n <= 4:
        discardList[1][1] = rand.choice(characters.list)
        characters.list.remove(discardList[1][1])
    return discardList

# Make the active player choose their character card for the turn
def choose(plindex):
    # Print The choices available to the player on the screen
    for j in range(7):
        try:
            print(f"{j + 1}: {characters.list[j].name} | {characters.list[j].effect}")
            i = j + 1
        except:
            print()
    # Loop until the player has chosen
    x = 35383113
    while True:
        # If first time print a blank line then set x to 0
        if x == 35383113:
            print("\x1b[2K")
            x = 10
        # If x correspond to a character break the loop
        elif x <= i and x >= 1:
            break
        # Else print the error message
        else:
            print("Entrée invalide")
        # Get the input from the user
        try:
            x = int(input("Choississez un personnage en entrant son numéro: "))
        except:
            ""
        # Clear the bottom of the screen
        clearBottom(2)
    print(f"\nVous avez choisi le {characters.list[x - 1].name}")
    sleep(.5)
    # Add the character to the player and remove it from the list
    player.list[plindex].character = characters.list[x - 1]
    characters.list.remove(characters.list[x - 1])
    return

# Make the active player play his turn
def turn(pl):
    print(pl.name)

# Clear n lines from the bottom of the screen and move the cursor up
def clearBottom(n):
    for i in range(n):
        print("\x1b[2K", end="")
        print("\033[1A", end="")
    print("\x1b[2K", end="")

# Draw the entire board
def drawBoard():
    os.system("cls||clear")

if __name__ == "__main__":
    # Launch the main function
    main()
