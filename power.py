# Class for choosing something (used by bottom.loop)
class choice:
    def __init__(self, name, number):
        self.name = name
        self.number = number



def power(pl):
    powers = []
    # Add the character's power to the powers list
    if pl.character.number == 1:
        powers.extend([choice("Assassiner un personnage", 4)])
    elif pl.character.number == 2:
        powers.extend([choice("Voler un personnnage", 5)])
    elif pl.character.number == 3:
        powers.extend([choice("Echanger x cartes de sa main contre x cartes de la pioche", 6), choice("Echanger sa main avec celle d'un joueur", 7)])
    elif pl.character.number == 4:
        powers.extend([choice("Percevoir les revenus de ses quartiers jaunes", 3)])
    elif pl.character.number == 5:
        powers.extend([choice("Percevoir les revenus de ses quartiers bleus", 3)])
    elif pl.character.number == 6:
        powers.extend([choice("Percevoir les revenus de ses quartiers verts", 3), choice("Prendre une pièce d'or", 8)])
    elif pl.character.number == 7:
        powers.extend([choice("Piocher 2 cartes supplémentaires", 9)])
    elif pl.character.number == 8:
        powers.extend([choice("Percevoir les revenus de ses quartiers rouges", 3), choice("Détruire un quartier pour son coût de construction moins 1", 10)])
    # Add the district's power to the power list
    for dis in pl.city:
        if dis.name == "Laboratoire      ":
            powers.extends([choice("Laboratoire: Se défausser d'une carte pour recevoir 2 pièces d'or", 11)])
        if dis.name == "Forge            ":
            powers.extends([choice("Forge: Payer 2 pièces d'or pour piocher 3 cartes", 12)])
    # Return powers
    return powers

def assassin(charList):
    return

def thief(charList):
    return

def magician():
    return

def king():
    return

def bishop():
    return

def merchant():
    return

def architect():
    return

def warlord():
    return

def takeGold(color, city):
    gold = 0
    for dis in city:
        if dis.color == color or dis.name == "École de Magie   ":
            gold += 1
    return gold
