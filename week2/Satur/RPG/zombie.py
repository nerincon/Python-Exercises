from rpg_game import Character

class Zombie(Character):
    def attack(self):
        if self.zombie_health > 0:
            # Zombie attacks hero
            self.hero_health -= self.zombie_power
            print("The zombie does {} damage to you.".format(self.zombie_power))
        if self.hero_health <= 0:
            print("You are dead.")