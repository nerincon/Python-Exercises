class Character():
    def __init__(self, health, power):
        self.health = 10
        self.power = 5

    def attack(self, character):
        character.health -= self.power
        print("gngnskbn")
        
    def print_status(self):
        print(" %s Health: %d\n %s Power: %d"%(self.name, self.health, self.name, self.power))
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


