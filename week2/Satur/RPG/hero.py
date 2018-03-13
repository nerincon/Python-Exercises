from rpg_game import Character

class Hero(Character):
    def __init__(self):
        # super()__init__():
        self.name = ""
        self.health = 15
        self.power = 5
        