from termcolor import colored

# Function to create a list of n players and return it
def init(n):
    global list
    list = []

    for i in range(n):
        list.append(player(f"player{i + 1}      ", i + 1))

# Define the class player
class player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.gold = 0
        self.hand = []
        self.isking = False
        self.character = None
        self.city = []
        self.points = 0

# Count the score of all player
def countScores():
    for p in list:
        green = blue = yellow = red = magenta = False
        colorCount = 0
        for d in p.city:
            # Count the cost of the district
            p.points += d.cost
            # Count the points of the special districts
            if d.name == colored("Trésor Impérial  ", "magenta"):
                p.points += p.gold
            elif d.name == colored("Salle des Cartes ", "magenta"):
                p.points += len(p.hand)
            elif d.name == colored("Université       ", "magenta"):
                p.points += 2
            elif d.name == colored("Dracoport        ", "magenta"):
                p.points += 2
            # Handle the 3 points of the having 5 colors and the Haunted City
            if d.color == "green":
                green = True
            elif d.color == "blue":
                blue = True
            elif d.color == "yellow":
                yellow = True
            elif d.color == "red":
                red = True
            elif d.color == "magenta" and d.name != colored("Cour des Miracles", "magenta"):
                magenta = True
            elif d.name == colored("Cour des Miracles", "magenta"):
                colorCount += 1
        for color in [green, blue, yellow, red, magenta]:
            if color :
                colorCount += 1
        if colorCount >= 5:
            p.points += 3
        print(colorCount)
            
            