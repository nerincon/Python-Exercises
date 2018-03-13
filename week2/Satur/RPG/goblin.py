from rpg_game import Character

class Goblin(Character):
    def attack(self):
        if self.goblin_health > 0:
            # Goblin attacks hero
            self.hero_health -= self.goblin_power
            print("The goblin does {} damage to you.".format(self.goblin_power))
        if self.hero_health <= 0:
            print("You are dead.")