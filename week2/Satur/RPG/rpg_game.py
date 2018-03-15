from random import randint
class Character():
    def __init__(self, health, power, bounty=0):
        self.health = health
        self.power = power
        
        
        
    def attack(self, character):
        prob = randint(1,100)
        prob2 = randint(1,100)
        prob3 = randint(1,100)
        more_power = self.power*2
        power = self.power
        if prob <= 20 and type(character).__name__.lower() == "medic" and prob2 <= 20:
            character.health -= more_power
            character.health += 2
            print("%s has lost %d health points"%(type(character).__name__.lower(),more_power))
            print("The %s has re-gained %s health points"%(type(character).__name__.lower(), 2))
        elif prob > 20 and type(character).__name__.lower() == "medic" and prob2 <= 20:
            character.health -= power
            character.health += 2
            print("%s has lost %d health points"%(type(character).__name__.lower(),power))
            print("The %s has re-gained %s health points"%(type(character).__name__.lower(), 2))
        elif type(character).__name__.lower() == "shadow" and prob3 <= 10:
            print("The %s deflected your attack!"%(type(character).__name__.lower()))
        elif prob <= 20:
            character.health -= more_power
            print("%s has lost %d health points"%(type(character).__name__.lower(),more_power))
        else:
            character.health -= power
            print("%s has lost %d health points"%(type(character).__name__.lower(),power))
        
        
        
    def print_status(self):
        print("Health: %d\nPower: %d"%(self.health, self.power))
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False