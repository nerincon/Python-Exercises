from rpg_game import Character

class Zombie(Character):
    def __init__(self, health, power):
        super().__init__(health, power, bounty=2)