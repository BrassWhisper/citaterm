def init():
    char1 = character("Assassin   ", 1, "L'Assassin peut tuer un personnage de son choix. Celui-ci ne jouera pas durant ce tour.")
    char2 = character("Voleur     ", 2, "Le Voleur peut voler le personnage de son choix. Quand le personnage détroussé sera révélé, il donnera tout son or au voleur;")
    char3 = character("Magicien   ", 3, "Au Choix : -Echanger sa main avec celle du joueur de son choix - Echanger x cartes de sa main contre x cartes de la pioche")
    char4 = character("Roi        ", 4, "Le Roi prend la Couronne, il choisira son personnage en premier au prochain tour. Ses quartiers nobles rapportent")
    char5 = character("Evêque     ", 5, "L'Evêque est immunisé contre le Condottiere sauf s'il a été assassiné. Ses quartiers religieux rapportent")
    char6 = character("Marchand   ", 6, "Le Marchand reçoit 1 pièce d'or au début de son tour. Ses quatiers commerçants rapportent")
    char7 = character("Architecte ", 7, "L'Architecte pioche 2 cartes supplémentaires au début de son tour. Il peut bâtir jusqu'à 3 quartiers")
    char8 = character("Condottiere", 8, "Le Condottiere peut détruire un quartier en payant son coût de construction moins 1. Ses quartiers militaires rapportent")
    
    # Create the global list of characters
    global list
    list = [char1, char2, char3, char4, char5, char6, char7, char8]

# Character class
class character:
    def __init__(self, name, number, effect):
        self.name = name
        self.number = number
        self.effect = effect
        self.murdered = False
        self.stealed = False
