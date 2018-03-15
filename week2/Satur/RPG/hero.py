from rpg_game import Character
from random import randint

class Hero(Character):
    def __init__(self, health, power, armor=0):
        self.armor = armor
        super().__init__(health, power)
        