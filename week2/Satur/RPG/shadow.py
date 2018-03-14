from rpg_game import Character
from random import randint

class Shadow(Character):
    def __init__(self, health, power):
        super().__init__(health, power, bounty=2)

    