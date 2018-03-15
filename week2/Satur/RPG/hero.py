from rpg_game import Character
from random import randint

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        