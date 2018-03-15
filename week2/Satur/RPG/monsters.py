from rpg_game import Character

class Medic(Character):
    def __init__(self, health, power, bounty=2):
        super().__init__(health, power, bounty)
        
        
class Shadow(Character):
    def __init__(self, health, power, bounty=2):
        super().__init__(health, power, bounty)
        

class Zombie(Character):
    def __init__(self, health, power, bounty=2):
        super().__init__(health, power, bounty)
        
        
class Goblin(Character):
    def __init__(self, health, power, bounty=5):
        super().__init__(health, power, bounty)
        

class Wizard(Character):
    def __init__(self, health, power, bounty=6):
        super().__init__(health, power, bounty)