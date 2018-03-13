from rpg_game import Character

class Zombie(Character):
    def __init__(self):
        # super()__init__()
        self.name = ""
        self.health = 1000
        self.power  = 2
    def alive(self):
        return True