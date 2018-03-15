from hero import Hero
from monsters import *



def main ():
    people = ["Goblin", "Zombie", "Medic", "Wizard", "Shadow", "Hero"]
    for p in people:
        print(p)
    pick_player = input("Who do you want to be? (pick player from above list) > ").capitalize()
    pick_enemy = input("Who do you want as your enemy? (pick player from above list) > ").capitalize()

    
    h_player = int(input("Pick health for player (0-infinity)? "))
    p_player = int(input("Pick power for player (0-infinity)? "))
    h_enemy = int(input("Pick health for enemy (0-infinity)? "))
    p_enemy = int(input("Pick power for enemy (0-infinity)? "))
    
        
    if pick_player == "Goblin":
        player = Goblin(h_player, p_player)
    elif pick_player == "Zombie":
        player = Zombie(h_player, p_player)
    elif pick_player == "Medic":
        player = Medic(h_player, p_player)
    elif pick_player == "Wizard":
        player = Wizard(h_player, p_player)
    elif pick_player == "Shadow":
        player = Shadow(h_player, p_player)
    elif pick_player == "Hero":
        player = Hero(h_player, p_player)
        
        
        
    if pick_enemy == "Hero":
        enemy = Hero(h_enemy, p_enemy)
    elif pick_enemy == "Zombie":
        enemy = Zombie(h_enemy, p_enemy)
    elif pick_enemy == "Medic":
        enemy = Medic(h_enemy, p_enemy)
    elif pick_enemy == "Wizard":
        enemy = Wizard(h_enemy, p_enemy)
    elif pick_enemy == "Shadow":
        enemy = Shadow(h_enemy, p_enemy)
    elif pick_enemy == "Goblin":
        enemy = Goblin(h_enemy, p_enemy)
        
    # player.print_status()
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
            # print("You do {} damage to the {}".format(player.power, type(enemy).__name__.lower()))
            if player.health <= 0:
                print("The %s is dead."%(type(player).__name__.lower()))
            elif enemy.health <= 0:
                print("The %s is dead."%(type(enemy).__name__.lower()))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            quit()
        else:
            print("Invalid input {}".format(raw_input))
            
        if enemy.alive() > 0:
            # Enemy attacks Player
            player.health -= enemy.power
            print("The %s does %d damage to you."%(type(enemy).__name__.lower(), enemy.power))
            print("The %s has %d health"%(type(enemy).__name__.lower(), enemy.health))
            if player.health <= 0:
                print("You are dead.")


main()


