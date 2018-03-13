from rpg_game import Character

class Goblin(Character):
    def __init__(self, name):
        super().__init__()
        self.name = ""
        self.health = 20
        self.power = 20
    