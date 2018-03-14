from rpg_game import Character
from random import randint

class Hero(Character):
    def __init__(self):
        # super()__init__():
        self.health = 2000
        self.power = 5
      
        
    def attack(self, character):
        prob = randint(1,100)
        prob2 = randint(1,100)
        power = self.power*2
        if prob > 20:
            power = self.power
        elif type(character).__name__.lower() == "medic" and prob2 > 20:
            if prob > 20:
                power = self.power
                character.health -= power
                character.health += 2
            elif prob <= 20:
                power = self.power * 2
                character.health -= power
                character.health += 2
        else:
            power = self.power*2
        character.health -= power
        print("%s has lost %d health points"%(type(character).__name__.lower(),power))