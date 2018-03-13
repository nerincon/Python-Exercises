from rpg_game import Character
from goblin import Goblin

class Hero(Character):
    def attack(self):
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
                quit()
            else:
                print("Invalid input {}".format(raw_input))