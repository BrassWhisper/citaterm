from termcolor import colored

# Function to create the deck of districts
def init():
    # Create each district
    tavern           = district(colored("Taverne          ", "green"  ), 1, "green",   1,  
                                        ["", "", ""])
    tradingPost      = district(colored("Échoppe          ", "green"  ), 2, "green",   2,  
                                        ["", "", ""])
    market           = district(colored("Marché           ", "green"  ), 2, "green",   3,  
                                        ["", "", ""])
    docks            = district(colored("Comptoir         ", "green"  ), 3, "green",   4,  
                                        ["", "", ""])
    harbor           = district(colored("Port             ", "green"  ), 4, "green",   5,  
                                        ["", "", ""])
    townHall         = district(colored("Hôtel de Ville   ", "green"  ), 5, "green",   6,  
                                        ["", "", ""])
    temple           = district(colored("Temple           ", "blue"   ), 1, "blue",    7,  
                                        ["", "", ""])
    church           = district(colored("Église           ", "blue"   ), 2, "blue",    8,  
                                        ["", "", ""])
    monastery        = district(colored("Monastère        ", "blue"   ), 3, "blue",    9,  
                                        ["", "", ""])
    cathedral        = district(colored("Cathédrale       ", "blue"   ), 5, "blue",    10, 
                                        ["", "", ""])
    watchtower       = district(colored("Tour de Guet     ", "red"    ), 1, "red",     11, 
                                        ["", "", ""])
    prison           = district(colored("Prison           ", "red"    ), 2, "red",     12, 
                                        ["", "", ""])
    battlefield      = district(colored("Caserne          ", "red"    ), 3, "red",     13, 
                                        ["", "", ""])
    fortress         = district(colored("Forteresse       ", "red"    ), 5, "red",     14, 
                                        ["", "", ""])
    manor            = district(colored("Manoir           ", "yellow" ), 3, "yellow",  15, 
                                        ["Une résidence de choix au mileu de bois", 
                                        "giboyeux. Ce prestigieux domaine se transmet", 
                                        "de générations en générations"])
    castle           = district(colored("Château          ", "yellow" ), 4, "yellow",  16, 
                                        ["Cet édfice massif surplombe toute la région. Les ennemis", 
                                        "du royaume comme ses habitant se sentent souvent écrasés", 
                                        "par la puissance qui en émane."])
    palace           = district(colored("Palais           ", "yellow" ), 5, "yellow",  17, 
                                        ["Les richesses amassées dans tout le royaume sont réunies", 
                                        "dans ce majestueux palace. Les réceptions fréquentes", 
                                        "rassemblent parfois les dirigeants des pays voisins"])
    hauntedCity      = district(colored("Cour des Miracles", "magenta"), 2, "magenta", 18,
                                        ["Pour le calcul du score, la Cour des Miracles est", 
                                        "considérée comme un quartier de la couleur de votre choix.",
                                        ""])
    keep             = district(colored("Donjon           ", "magenta"), 3, "magenta", 19,
                                        ["Le Donjon ne peut pas être détruit par le Condottiere.",
                                        "",
                                        ""])
    observatory      = district(colored("Observatoire     ", "magenta"), 4, "magenta", 20,
                                        ["Si vous choississez de piocher des cartes au début de", 
                                        "votre tour, piochez en 3 au lieu de 2. Choisissez-en une", 
                                        "et défaussez les 2 autres."])
    laboratory       = district(colored("Laboratoire      ", "magenta"), 5, "magenta", 21,
                                        ["Une fois par tour, vous pouvez défausser 1 carte et", 
                                        "recevoir 2 pièces d'or.",
                                        ""])
    smithy           = district(colored("Forge            ", "magenta"), 5, "magenta", 22,
                                        ["Une fois par tour, vous pouvez payer 2 pièces d'or pour",
                                        "piocher 3 cartes.",
                                        ""])
    graveyard        = district(colored("Cimetière        ", "magenta"), 5, "magenta", 23,
                                        ["Lorsque le Condottiere détruit un quartier, vous pouvez", 
                                        "payer 1 pièce d'or pour le prendre dans votre main. Vous",
                                        "ne pouvez pas le faire si vous êtes vous-même Condottiere"])
    imperialTreasure = district(colored("Trésor Impérial  ", "magenta"), 5, "magenta", 24,
                                        ["A la fin de la partie, marquez 1 point supplémentaire", 
                                        "pour chaque pièce d'or dans votre trésor.",
                                        ""])
    mapRoom          = district(colored("Salle des Cartes ", "magenta"), 5, "magenta", 25,
                                        ["A la fin de la partie, marquez 1 point supplémentaire", 
                                        "pour chaque carte dans votre main.",
                                        ""])
    schoolOfMagic    = district(colored("École de Magie   ", "magenta"), 6, "magenta", 26,
                                        ["Pour la perception des revenus, l'Ecole de Magie est", 
                                        "considérée comme un quartier de la couleur de votre",
                                        "choix."])
    library          = district(colored("Bibliothèque     ", "magenta"), 6, "magenta", 27,
                                        ["Si vous choisissez de piocher des cartes au début de votre",
                                        "tour, conservez-les toutes.",
                                        ""])
    greatWall        = district(colored("Grande Muraille  ", "magenta"), 6, "magenta", 28,
                                        ["Le prix à payer par le Condottiere pour détruire vos",
                                        "autres quartiers est augmenté de 1.",
                                        ""])
    university       = district(colored("Université       ", "magenta"), 6, "magenta", 29,
                                        ["Coûte 6 pièces d'or à bâtir mais vaut",
                                        "8 points pour le calcul du score.",
                                        ""])
    dragonGate       = district(colored("Dracoport        ", "magenta"), 6, "magenta", 30,
                                        ["Coûte 6 pièces d'or à bâtir mais vaut", 
                                        "8 points pour le calcul du score.",
                                        ""])
    
    # Assign to each district the number of times it has to be in the deck
    deck = {
            # Green
            tavern:           5,
            tradingPost:      3,
            market:           4,
            docks:            3,
            harbor:           3,
            townHall:         2,
            # Blue
            temple:           3,
            church:           3,
            monastery:        3,
            cathedral:        2,
            # Red
            watchtower:       3,
            prison:           3,
            battlefield:      3,
            fortress:         2,
            # Yellow
            manor:            5,
            castle:           4,
            palace:           3,
            # Purple
            hauntedCity:      1,
            keep:             2,
            observatory:      1,
            laboratory:       1,
            smithy:           1,
            graveyard:        1,
            imperialTreasure: 1,
            mapRoom:          1,
            schoolOfMagic:    1,
            library:          1,
            greatWall:        1,
            university:       1,
            dragonGate:       1
            }
    
    # Create the final deck by appending each district to a list that init() return
    global districts
    districts = []
    for card in deck:
        for i in range(deck[card]):
            districts.append(card)

# District class
class district:
    def __init__(self, name, cost, color, number, effect):
        self.name = name
        self.cost = cost
        self.color = color
        self.number = number
        self.effect = effect

# Return a list of n cards from the top of the districtDeck and remove them from it
def draw(n):
    cards = []
    for i in range(n):
        cards.append(districts[0])
        districts.remove(districts[0])
    return cards

# Put a card (or cards) at the bottom of the deck
def discard(cards):
    districts.extend(cards)


