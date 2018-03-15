word = []
def hello():
    x = input("...")
    if x == "hello":
        word.append("hello")
    elif x == "world":
        word.append("world")
       
        
def let():
    global word
    hello()
    print(word)
    if word[0] == "hello":
        print("YESSSS")
        word.pop()
        print(word)
    elif word[0] == "world":
        print("That's Right!")
        

let()



armor = 1
power = 7
health = 8

if armor == 0:
    health -= power
elif armor < power:
    armor -= armor
    power_left = power
    power_left -= armor
    health -= power_left
elif armor >= power:
    armor -= armor



# if armor == 0:
#     if power < health:
#         old_power = power
#         power -= power
#         health -= old_power
#         print(power)
#         print(health)
#     else:
#         power -= health
#         health -= health
#         print(power)
#         print(health)
# elif armor < power and health-armor < power:
#     old_armor = armor
#     armor -= armor
#     print(armor)
#     power -= old_armor
#     print(power)
#     old_power = power
#     power -= power
#     print(power)
#     health -= old_power
#     print(health)
# elif armor < power and health-armor >= power:
#     old_armor = armor
#     armor -= armor
#     print(armor)
#     power -= old_armor
#     print(power)
#     health -= power
#     print(health)
#     power -= power
#     print(power)
# elif armor > power:
#     old_armor = armor
#     armor -= power
#     print(armor)
#     power -= power
#     print(power)

