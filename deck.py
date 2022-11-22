# Function to create the deck of districts
def init():
    # Create each district
    tavern           = district("Taverne          ", 1, "green",   "")
    tradingPost      = district("Échoppe          ", 2, "green",   "")
    market           = district("Marché           ", 2, "green",   "")
    docks            = district("Comptoir         ", 3, "green",   "")
    harbor           = district("Port             ", 4, "green",   "")
    townHall         = district("Hôtel de Ville   ", 5, "green",   "")
    temple           = district("Temple           ", 1, "blue",    "")
    church           = district("Église           ", 2, "blue",    "")
    monastery        = district("Monastère        ", 3, "blue",    "")
    cathedral        = district("Cathédrale       ", 5, "blue",    "")
    watchtower       = district("Tour de Guet     ", 1, "red",     "")
    prison           = district("Prison           ", 2, "red",     "")
    battlefield      = district("Caserne          ", 3, "red",     "")
    fortress         = district("Forteresse       ", 5, "red",     "")
    manor            = district("Manoir           ", 3, "yellow",  "")
    castle           = district("Château          ", 4, "yellow",  "")
    palace           = district("Palais           ", 5, "yellow",  "")
    hauntedCity      = district("Cour des Miracles", 2, "magenta", "Pour le calcul du score, la Cour des Miracles est considérée comme un quartier de la couleur de votre choix.")
    keep             = district("Donjon           ", 3, "magenta", "Le Donjon ne peut pas être détruit par le Condottiere.")
    observatory      = district("Observatoire     ", 4, "magenta", "Si vous choississez de piocher des cartes au début de votre tour, piochez en 3 au lieu de 2. Choisissez-en une et défaussez les 2 autres.")
    laboratory       = district("Laboratoire      ", 5, "magenta", "Une fois par tour, vous pouvez défausser 1 carte et recevoir 2 pièces d'or.")
    smithy           = district("Forge            ", 5, "magenta", "Une fois par tour, vous pouvez payer 2 pièces d'or pour piocher 3 cartes.")
    graveyard        = district("Cimetière        ", 5, "magenta", "Lorsque le Condottiere détruit un quartier, vous pouvez payer 1 pièce d'or pour le prendre dans votre main. Vous ne pouvez pas le faire si vous êtes vous-même Condottiere")
    imperialTreasure = district("Trésor Impérial  ", 5, "magenta", "A la fin de la partie, marquez 1 point supplémentaire pour chaque pièce d'or dans votre trésor.")
    mapRoom          = district("Salle des Cartes ", 5, "magenta", "A la fin de la partie, marquez 1 point supplémentaire pour chaque carte dans votre main.")
    schoolOfMagic    = district("École de Magie   ", 6, "magenta", "Pour la perception des revenues, l'Ecole de Magie est considérée comme un quartier de la couleur de votre choix.")
    library          = district("Bibliothèque     ", 6, "magenta", "Si vuos choisissez de piocher des cartes au début de votre tour, conservez-les toutes.")
    greatWall        = district("Grande Muraille  ", 6, "magenta", "Le prix à payer par le Condottiere pour détruire vos autres quartiers est augmenté de 1.")
    university       = district("Université       ", 6, "magenta", "Coûte 6 pièces d'or à bâtir mais vaut 8 points pour le calcul du score.")
    dragonGate       = district("Dracoport        ", 6, "magenta", "Coûte 6 pièces d'or à bâtir mais vaut 8 points pour le calcul du score.")
    
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
    def __init__(self, name, cost, color, effect):
        self.name = name
        self.cost = cost
        self.color = color
        self.effect = effect

# Return a list of n cards from the top of the districtDeck and remove them from it
def draw(n):
    cards = []
    for i in range(n):
        cards.append(districts[0])
        districts.remove(districts[0])
    return cards

# Put a card (or cards) at the bottom of the deck
def discard(card):
    districts.append(card)


