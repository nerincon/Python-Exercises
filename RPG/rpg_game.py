from random import randint

class Character():
    def __init__(self):
        self.hero_health = randint(1,25)
        self.hero_power = randint(1,25)
        self.goblin_health = randint(1,25)
        self.goblin_power = randint(1,25)
        
    def print_status(self):
        print(" Hero Health: %d\n Hero Power: %d\n Goblin Health: %d\n Goblin Power: %d" %(self.hero_health, self.hero_power, self.goblin_health, self.goblin_power))
        

class Hero(Character):
    def __init__(self):
        Character.__init__(self)
        
    def attack(self):
        while self.goblin_health > 0 and self.hero_health > 0:
            print("You have {} health and {} power.".format(self.hero_health, self.hero_power))
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin
                self.goblin_health -= self.hero_power
                print("You do {} damage to the goblin.".format(self.hero_power))
                if self.goblin_health <= 0:
                    print("The goblin is dead.")
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))
        

class Goblin(Character):
    def __init__(self):
        Character.__init__(self)

    def attack(self):
        if self.goblin_health > 0:
            # Goblin attacks hero
            self.hero_health -= self.goblin_power
            print("The goblin does {} damage to you.".format(self.goblin_power))
        if self.hero_health <= 0:
            print("You are dead.")



c = Character()
c.print_status()
h = Hero()
h.attack()
g = Goblin()
g.attack()
