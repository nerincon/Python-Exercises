from random import randint
class Character():
    def __init__(self, health, power, bounty=1):
        self.health = health
        self.power = power

    def attack(self, character):
        prob = randint(1,100)
        if type(character).__name__.lower() == "medic" and prob > 20:
            character.health -= self.power
            character.health += 2
        else:
            character.health -= self.power
        print("%s has lost %d health points"%(type(character).__name__.lower(), self.power))
        
    def print_status(self):
        print("Health: %d\nPower: %d"%(self.health, self.power))
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


