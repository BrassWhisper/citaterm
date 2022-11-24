import os
from sys import argv
from time import sleep
import random as rand
from termcolor import colored

import deck 
import characters
import player
import board
import bottom
import power

START_GOLD = 50
START_HAND = 2

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
    # Initialize global variable deck.districts and player.list
    deck.init()             # Create deck.districts
    player.init(nbPlayer)   # Create player.list 

    # Shuffle the deck
    rand.shuffle(deck.districts)

    # Make a random player the king
    rand.choice(player.list).isking = True

    # Make the players draw and get their gold
    for p in player.list:
        p.hand = deck.draw(START_HAND)
        p.city = deck.draw(6)
        p.gold = START_GOLD

def game():
    initgame()
    # Main loop
    while True:
        # Refresh the character list
        global charList
        charList = characters.init()
        # Remove each player character
        for pl in player.list:
            pl.character = None
        # Loop to find the king
        for i in range(nbPlayer):
            if player.list[i].isking:
                break

        # Discard a number of character cards based on the number of players
        discardChar(nbPlayer)
        
        # Draw the board
        board.draw(player.list, nbPlayer, discardList, -1, -1)

        # Players choose their character beginning by the king and clockwise
        for j in range(nbPlayer):
            # If j == 6 that mean there is 7 players and this is the last choice, we add the face down character to the charList according to rules
            if j == 6:
                charList.append(discardList[0])
            # Player of index i gets to choose his character
            board.draw(player.list, nbPlayer, discardList, 0, i)
            player.list[i].character = choose("Quel personnage choisissez-vous ?                         ", charList, player.list[i])
            i += 1
            # Go back to the beggining of the player list
            if i == nbPlayer:
                i = 0
        
        # Decide which player has to play based on the character they pick
        end = False
        for i in range(1, 9):
            for pl in player.list:
                if pl.character.number == i and pl.character.murdered == False:
                    turn(pl)
                    # Other players that trigger their city trigger this
                    if end and len(pl.city) >= 7:
                        pl.points += 2
                    # First player to end his city trigger this
                    if endOfGame() and end == False:
                        pl.points += 4
                        end = True
        # Set the new king even if he was murdered
        for pl in player.list:
            if pl.character.number == 4:
                pl.isking = True
            else:
                pl.isking = False
                
        if end:
            break
    player.countScores()
    for p in player.list:
        print(p.name + ": " + str(p.points) + " points")

# Discard a number of character cards based on the number of players, return a list with the face down at index 0 and the face up at index 1
def discardChar(n):
    # Always discard one character face down
    global discardList
    discardList = [rand.choice(charList), [None, None, None]]
    charList.remove(discardList[0])
    # If 4 or 5 players, one discarded face up
    if n <= 5:
    # King can't be discarded face up
        char = rand.choice(charList)
        while char.number == 4:
            char = rand.choice(charList)
        discardList[1][0] = char
        charList.remove(char)
    # If 4 players, one more discarded face up
    if n <= 4:
    # King can't be discarded face up
        char = rand.choice(charList)
        while char.number == 4:
            char = rand.choice(charList)
        discardList[1][1] = char
        charList.remove(char)
    return discardList

# Make the active player choose a card from the list
def choose(question, cardList, pl):
    # Create the variable for the chosen card
    cho = power.choice("", 0)
    while cho.number == 0:
        cho = bottom.loop(question, cardList, pl)
    bottom.loop(f"Vous avez choisi {cho.name}                        ", [[]], pl)
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
        pl.isking = True
    # Steal the player if he is stealed
    if pl.character.stealed:
        for p in player.list:
            if p.character.number == 2:
                p.gold += pl.gold
        pl.gold = 0
    # Create the list of possible actions
    actions = [power.choice("Prendre de l'or ou des cartes                             ", 1)] + power.power(pl)
    # Number of the player
    plIndex = player.list.index(pl)
    # Loop until the end of turn happen
    while True:
        board.draw(player.list, nbPlayer, discardList, 0, plIndex)
        cho = bottom.loop("Quelle action faites-vous ?                               ", actions, pl)
        handSize = len(pl.hand)
        
        # Player choose between 2 gold or draw
        if cho.number == 1:
            # Handle the observatory
            drawNb = 2
            for d in pl.city:
                if d.name == colored("Observatoire     ", "magenta"):
                    drawNb = 3
            # Handle the Library
            drawString = f"Piochez {drawNb} quartiers, en conserver 1 et défausser le reste "
            haveLibrary = False
            for d in pl.city:
                if d.name == colored("Bibliothèque     ", "magenta"):
                    drawString = f"Piochez {drawNb} quartiers                                       "
                    haveLibrary = True
                    
            goldOrCard = bottom.loop("Choisissez vous l'or ou les cartes ?                      ",
                                    [power.choice(drawString, 1), 
                                     power.choice("Prendre 2 pièces d'or dans la banque                      ", 2)], pl)
            # Draw 2 or 3 cards, choose one and discard the other at the bottom of the deck
            if goldOrCard.number == 1:
                if haveLibrary:
                    pl.hand.extend(deck.draw(drawNb))
                else :
                    dra = deck.draw(drawNb)
                    dis = power.choice("", 0)
                    while dis.number == 0:
                        dis = bottom.loop("Quelle carte choisissez vous ?                            ", dra, pl)
                    pl.hand.append(dis)
                    dra.remove(dis)
                    deck.discard(dra)
            # Take 2 gold
            if goldOrCard.number == 2:
                pl.gold += 2
            # If we don't escape the choice remove the choice from the actions and add the 2 additional actions
            if goldOrCard.number != 0:
                actions.remove(cho)
                actions.extend([power.choice("Bâtir un quartier                                         ", 2), 
                                power.choice("Finir le tour                                             ", -1)])

        # Build a district in the city
        elif cho.number == 2 and handSize != 0:
            dis = bottom.loop("Quel bâtiment voulez-vous construire ?                    ", pl.hand, pl)
            if dis.number != 0:
                # Handle the case of the same district build twice
                double = False
                for d in pl.city:
                    if dis.name == d.name:
                        double = True
                if double:
                    bottom.loop("Vous avez déjà ce quartier dans votre cité                ", [[]], pl)
                elif dis.cost > pl.gold:
                    bottom.loop("Vous n'avez pas assez d'or pour contruire ce quartier.    ", [[]], pl)
                else:
                    bottom.loop(f"Vous construisez {dis.name} pour {dis.cost} pièces d'or.    ", [[]], pl)
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
            # Initialize a new characters list
            charList = characters.init()
            # Remove the assassin
            charList.remove(charList[0])
            # Remove the characters discarded face up
            for discarded in discardList[1]:
                for char in charList:
                    try:
                        if discarded.number == char.number:
                            charList.remove(char)
                    except:
                        ""
            victim = bottom.loop("Choisissez un joueur à assassiner.                        ", charList, pl)
            if victim.number != 0:
                # Add the victim of the assassin to the discardList to remove it from the choices of the thief
                discardList[1][2] = victim
                # Murder the character if a player owns it
                for p in player.list:
                    if p.character.number == victim.number:
                        p.character.murdered = True
                actions.remove(cho)
        # Power of the thief
        elif cho.number == 5:
            # Initialize a new characters list
            charList = characters.init()
            # Remove the assassin and the thief
            charList.remove(charList[0])
            charList.remove(charList[0])
            # Remove the characters discarded face up
            for discarded in discardList[1]:
                for char in charList:
                    try:
                        if discarded.number == char.number:
                            charList.remove(char)
                    except:
                        ""
            robbed = bottom.loop("Choisissez un joueur à voler.                             ", charList, pl)
            if robbed.number != 0:
                # Steal the character if a player owns it
                for p in player.list:
                    if p.character.number == robbed.number:
                        p.character.stealed = True
                actions.remove(cho)
        # Power1 of the magician
        elif cho.number == 6:
            if handSize == 0:
                bottom.loop("Vous n'avez aucune carte à défausser.                     ", [[]], pl)
            # Keep track of the discarded cards, print them and allow the player to get them back before swapping
            discarded = []
            while True:
                confirm = [power.choice(f"Echanger {len(discarded)} cartes contre {len(discarded)} cartes de la pioche            ", -1)]
                card = bottom.loop("Choisissez une carte à défausser.                         ", pl.hand + confirm + discarded, pl)
                # Esc was pressed, return to actions of the turn, cancel discard
                if card.number == 0:
                    pl.hand.extend(discarded)
                    break
                # Confirm the power of the magician: discard cards and draw that many
                elif card.number == -1:
                    pl.hand.extend(deck.draw(len(discarded)))
                    deck.discard(discarded)
                    # Remove the 2 powers of the magician
                    actIndex = actions.index(cho)
                    actions.remove(actions[actIndex])
                    actions.remove(actions[actIndex])
                    break
                # Put a card in the hand from the discard pile
                elif card.number == -2:
                    card.number = 1
                    pl.hand.extend([card])
                    discarded.remove(card)
                # Put a card in the discard pile from hand
                else:
                    card.number = -2
                    discarded.extend([card])
                    pl.hand.remove(card)
        # Power2 of the magician
        elif cho.number == 7:
            plList = player.list.copy()
            plList.remove(pl)
            p = bottom.loop("Echanger votre main avec quel joueur ?                    ", plList, pl)
            if p.number != 0:
                pIndex = player.list.index(p)
                tmpHand = player.list[pIndex].hand
                player.list[pIndex].hand = pl.hand
                pl.hand = tmpHand
                # Remove the 2 powers of the magician
                actIndex = actions.index(cho)
                actions.remove(actions[actIndex - 1])
                actions.remove(actions[actIndex - 1])
        # Power of the merchant
        elif cho.number == 8:
            pl.gold += 1
            actions.remove(cho)
        # Power of the architect
        elif cho.number == 9:
            pl.hand.extend(deck.draw(2))
            actions.remove(cho)
        # Power of the warlord
        elif cho.number == 10:
            p = bottom.loop("Détruire un bâtiment de la cité de quel joueur ?          ", player.list, pl)
            if p.number == 0:
                "Return to actions"
            elif p.number != 0 and len(p.city) != 0 and len(p.city) < 7:
                dis = bottom.loop("Détruire quel bâtiment ?                                  ", p.city, pl)
                if dis.number != 0:
                    cost = dis.cost - 1
                    for d in p.city:
                        if d.name == colored("Grande Muraille  ", "magenta"):
                            cost += 1
                    if dis.name == colored("Donjon           ", "magenta"):
                        bottom.loop("Vous ne pouvez pas détruire le donjon.                    ", [[]], pl)
                    elif cost > pl.gold:
                        bottom.loop("Vous n'avez pas assez de pièces d'or.                     ", [[]], pl)
                    else:
                        pl.gold -= cost
                        # Remove the district of the global player.list and discard it
                        p.city.remove(dis)
                        deck.discard([dis])
                        actions.remove(cho)
            elif len(p.city) == 0:
                bottom.loop("Aucun quartier à détruire dans cette cité                 ", [[]], pl)
            elif len(p.city) >= 7:
                bottom.loop("Vous ne pouvez pas détruire un quartier d'une cité finie. ", [[]], pl)
        # Power of the laboratory
        elif cho.number == 11:
            if handSize == 0:
                bottom.loop("Vous n'avez aucune carte à défausser.                     ", [[]], pl)
            dis = bottom.loop("Choisissez une carte à défausser.                         ", pl.hand, pl)
            if dis.number != 0:
                pl.gold += 2
                pl.hand.remove(dis)
                actions.remove(cho)
        # Power of the smithy
        elif cho.number == 12:
            if pl.gold >= 2:
                pl.gold -= 2
                pl.hand.extend(deck.draw(3))
                actions.remove(cho)
            else:
                bottom.loop("Vous n'avez pas assez de pièces d'or.                     ", [[]], pl)
        # End of turn
        elif cho.number == -1:
            break
        # See the board
        elif cho.number == 0:
            board.loop(player.list, nbPlayer, discardList)

# Test for a winner
def endOfGame():
    for p in player.list:
        if len(p.city) >= 7:
            return True
    return False

# Clear the entire board
def clear():
    os.system("cls||clear")

if __name__ == "__main__":
    # Launch the main function
    main()
