item = []

def shop():
    print("==============================")
    print("Welcome to the shop!")
    print("==============================")
    print("Below are the available items")
    print("==============================")
    items = ["Supertonic: 10 point health increase", "Armor"]
    for i in items:
        print("item: " + i)

    buy_item = input("What would you like to buy? > ").capitalize()
    if buy_item == "Supertonic":
        item.append("Supertonic")
    elif buy_item == "Armor":
        item.append("Armor")
    else:
        print("We currently don't have that item in our inventory, sorry")
    