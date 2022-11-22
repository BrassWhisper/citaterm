# Function to create a list of n players and return it
def init(n):
    global list
    list = []

    for i in range(n):
        list.append(player(f"player{i + 1}          ")) 
# Define the class player
class player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.hand = []
        self.isking = False
        self.character = None
        self.city = []
        self.points = 0
