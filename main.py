import csv
from sys import argv
from time import sleep
import random as rand
import os

import deck 
import characters
import player
import board
import bottom
import power

START_GOLD = 2
START_HAND = 4

def main():
    game()

def initgame():
    # Choose the number of players
    global nbPlayer
    while True:
        try:
            nbPlayer = int(input("Quel nombre de joueurs ? : "))
            if nbPlayer > 7 or nbPlayer < 4:
                print("Merci de choisir un nombre compris entre 4 et 7")
            else:
                break
        except ValueError:
            print("Ceci n'est pas un nombre valide")      
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

def game():
    initgame()
    # Main loop
    while True:
        # Refresh the character list
        characters.init()
        # Remove each player character
        for pl in player.list:
            pl.character = None
        # Loop to find the king
        for i in range(nbPlayer):
            if player.list[i].isking:
                break

        # Discard a number of character cards based on the number of players
        global discardList
        discardList = discard(nbPlayer)
        
        # Draw the board
        board.loop(player.list, nbPlayer, discardList)

        # Players choose their character beginning by the king and clockwise
        for j in range(nbPlayer):
            # If j == 6 that mean there is 7 players and this is the last choice, we add the face down character to the character.list according to rules
            if j == 6:
                characters.list.append(discardList[0])
            # Player of index i gets to choose his character
            board.draw(player.list, nbPlayer, discardList, 0, i)
            player.list[i].character = choose("Quel personnage choisissez-vous ?", characters.list)
            i += 1
            # Go back to the beggining of the player list
            if i == nbPlayer:
                i = 0
        
        # Decide which player has to play based on the character they pick
        for i in range(1, 9):
            for pl in player.list:
                if pl.character.number == i and pl.character.murdered == False:
                    turn(pl)
        # Set the new king even if he was murdered
        for pl in player.list:
            if pl.character.number == 4:
                pl.isking = True
            else:
                pl.isking = False

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

# Make the active player choose a card from the list
def choose(question, cardList):
    # Create the variable for the chosen card
    cho = power.choice("", 0)
    while cho.number == 0:
        cho = bottom.loop(question, cardList)
    bottom.loop(f"Vous avez choisi {cho.name}", [[]])
    sleep(.1)
    # Remove the chosen card from the list and return it
    cardList.remove(cho)
    return cho

# Make the active player play his turn
def turn(pl):
    # Reveal the character of the player
    pl.character.revealed = True
    # Set the buildLimit
    if pl.character.number == 7:
        buildLimit = 3
    else:
        buildLimit = 1
    # Set the new king if the king is revealed
    if pl.character.number == 4:
        for p in player.list:
            p.isking = False
        pl.isking == True
    # Create the list of possible actions
    actions = [power.choice("Prendre de l'or ou des cartes", 1)] + power.power(pl)
    # Number of the player
    plIndex = player.list.index(pl)
    # Loop until the end of turn happen
    while True:
        board.draw(player.list, nbPlayer, discardList, 0, plIndex)
        cho = bottom.loop("Quelle action faites-vous ?", actions)
        
        # Player choose between 2 gold or draw
        if cho.number == 1:
            goldOrCard = bottom.loop("Choisissez vous l'or ou les cartes ?",
                                    [power.choice("Piocher 2 quartiers, en conserver un et défausser l'autre", 1), 
                                     power.choice("Prendre 2 pièces d'or dans la banque", 2)])
            # Draw 2 cards, choose one and discard the other at the bottom of the deck
            if goldOrCard.number == 1:
                dra = deck.draw(2)
                dis = power.choice("", 0)
                while dis.number == 0:
                    dis = bottom.loop("Quelle carte choisissez vous ?", dra)
                pl.hand.append(dis)
                deck.discard(dra.remove(dis))
            # Take 2 gold
            if goldOrCard.number == 2:
                pl.gold += 2
            # If we don't escape the choice remove the choice from the actions and add the 2 additional actions
            if goldOrCard.number != 0:
                actions.remove(cho)
                actions.extend([power.choice("Bâtir un quartier", 2), power.choice("Finir le tour", -1)])

        # Build a district in the city
        elif cho.number == 2:
            dis = bottom.loop("Quel bâtiment voulez-vous construire ?", pl.hand)
            if dis.number != 0:
                if dis.cost > pl.gold:
                    bottom.loop("Vous n'avez pas assez d'or pour contruire ce quartier", [[]])
                else:
                    bottom.loop(f"Vous construisez {dis.name} pour {dis.cost} pièces d'or", [[]])
                    pl.gold -= dis.cost
                    pl.city.append(dis)
                    pl.hand.remove(dis)
                    buildLimit -= 1
                    if buildLimit == 0:
                        actions.remove(cho)
        # Receive gold based on color
        elif cho.number == 3:
            pl.gold += power.takeGold(pl.character.color, pl.city)
            actions.remove(cho)
        # Power of the assassin
        elif cho.number == 4:
            "assassin"
            actions.remove(cho)
        # Power of the thief
        elif cho.number == 5:
            "thief"
            actions.remove(cho)
        # Power1 of the magician
        elif cho.number == 6:
            "magician1"
            actions.remove(cho)
        # Power 2 of the magician
        elif cho.number == 7:
            "magician2"
            actions.remove(cho)
        # Power of the merchant
        elif cho.number == 8:
            "merchant"
            actions.remove(cho)
        # Power of the architect
        elif cho.number == 9:
            "architect"
            actions.remove(cho)
        # Power of the warlord
        elif cho.number == 10:
            "warlord"
            actions.remove(cho)
        # Power of the laboratory
        elif cho.number == 11:
            "laboratory"
            actions.remove(cho)
        # Power of the smithy
        elif cho.number == 12:
            "smithy"
            actions.remove(cho)
        # End of turn
        elif cho.number == -1:
            break
        # See the board
        elif cho.number == 0:
            board.loop(player.list, nbPlayer, discardList)


# Clear the entire board
def clear():
    os.system("cls||clear")

if __name__ == "__main__":
    # Launch the main function
    main()
