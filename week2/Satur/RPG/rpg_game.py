class Character():
    def __init__(self):
        self.hero_health = 10
        self.hero_power = 5
        self.goblin_health = 10
        self.goblin_power = 2
        self.zombie_health = 1000
        self.zombie_power = 2
        
        
    def print_status(self):
        print(" Hero Health: %d\n Hero Power: %d\n Goblin Health: %d\n Goblin Power: %d\n Zombie Health: %d\n Zombie Power: %d"
        %(self.hero_health, self.hero_power, self.goblin_health, self.goblin_power, self.zombie_health, self.zombie_power))
        
    def alive(self):
        if self.hero_health > 0:
            return True
        else:
            return False
        if self.goblin_health > 0:
            return True
        else:
            return False
        if self.zombie_health > 0:
            return True
        else:
            return False




