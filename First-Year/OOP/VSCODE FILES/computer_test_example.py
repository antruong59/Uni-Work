#1 
def calculate_area(edge):
    area = 6 * (edge ** 2)
    return area

#2
import random
class Warrior:
    def __init__(self, health, min_attack, max_attack, armour):
        self. health = health
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.armour = armour

    def do_damage(self):
        damage = random.randint(self.min_attack, self.max_attack)
        return damage

    def take_damage(self, damage):
        self.health -= damage

#3
class Game:
    def __init__(self):
        self.name = None
        self.cost = None

    def setter(self, name, cost):
        self.name = name
        self.cost = cost

    def getter(self):
        print(self.name)
        print(self.cost)

class Board_Game(Game):
    number_of_players = 0

    def __init__(self):
        super().__init__()

    def setter(self, name, cost, player):
        self.name = name
        self.cost = cost
        Board_Game().number_of_players = player

    def getter(self):
        print(self.name)
        print(self.cost)
        print(Board_Game().number_of_players)

class Video_Game(Game):
    is_multiplayer = None
    def __init__(self):
        super().__init__()

    def setter(self, name, cost, is_Multiple = True):
        self.name = name
        self.cost = cost
        Video_Game().is_multiplayer = is_Multiple

    def getter(self):
        print(self.name)
        print(self.cost)
        print(Video_Game().is_multiplayer)

class FPS(Video_Game):
    def __init__(self):
        super().__init__()

    def setter(self, name, cost, is_Multiple = True):
        self.name = name
        self.cost = cost
        Video_Game().is_multiplayer = is_Multiple

    def getter(self):
        print(self.name)
        print(self.cost)
        print(Video_Game().is_multiplayer)




