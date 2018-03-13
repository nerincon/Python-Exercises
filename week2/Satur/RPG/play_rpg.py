from zombie import Zombie
from goblin import Goblin
from hero import Hero

def main ():
    
    player = Hero()
    enemy = Goblin()
    # enemy = Zombie()
    
    while enemy.alive() and player.alive():
        print("You have {} health and {} power.".format(player.health, player.power))
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            player.attack(enemy)
            print("You do {} damage to the .".format(player.power, type(enemy).__name__.lower()))
            if player.health <= 0:
                print("The %s is dead."%(type(enemy).__name__.lower()))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            quit()
        else:
            print("Invalid input {}".format(raw_input))
            
        if enemy.alive() > 0:
            # Goblin attacks hero
            player.health -= enemy.power
            print("The goblin does {} damage to you.".format(enemy.power))
            if player.health <= 0:
                print("You are dead.")


main()

# c = Character("Hero")
# c.print_status()
