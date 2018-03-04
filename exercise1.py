# # Python Part 1 Exercises

# name = input("What is your name? ")
# print("Hello {}".format(name))

# # HELLO, YOU!

# name2 = input("What is your name? ")
# length = len(name2)
# print("Hello {}". format(name2))
# print("YOUR NAME HAS", length ,"LETTERS IN IT! AWESOME!")

# # Madlib
# print("Please fill in the blanks below:")
# print("___(sport)____ is my favorite sport, and __(color)__ is my favorite color.")
# fillin = input("What's your favorite sport? ")
# fillin2 = input("What's your favorite color? ")
# print("Your favorite sport is {} and your favorite color is {}. Awesome!".format(fillin, fillin2))


#Day of the Week


# days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5:"Friday", 6: "Saturday", 7:"Sunday"}

# def go():
#     day = int(input("Day (1-7)? "))
#     if day in days.keys():
#         print(days.get(day))
#     else:
#         print("Please pick a number from 1-7")
#         go()
# go()



# Work or Sleep In?

# def go2():
#     day2 = int(input("Day (1-7)? "))
#     if day2 > 0 and day2 < 6:
#         print("Go to Work")
#     elif day2 == 6 or day2 == 7:
#         print("Sleep in")
#     else:
#         print("Please pick a number from 1-7")
#         go2()
# go2()

# Celsius to Fahrenheit

# temp = int(input("Temperature in C? "))
# faren = temp * 1.8 + 32
# print("{} F".format(faren))


# Tip Calculator

# bill = int(input("Total bill amount? "))
# service = input("Level of service (good, fair or bad)? ")
# if service == "good":
#     print("Tip Amount: ${:.2f}".format(bill * 0.2))
#     print("Total Amount: ${:.2f}".format(bill * 1.2))
# elif service == "fair":
#     print("Tip Amount: ${:.2f}".format(bill * 0.15))
#     print("Total Amount: ${:.2f}".format(bill * 1.15))
# else:
#     print("Tip Amount: ${:.2f}".format(bill * 1.1))
#     print("Total Amount: ${:.2f}".format(bill * 1.1))


# Tip Calculator 2 --> Longer but better if want to change percentage

# bill = int(input("Total bill amount? "))
# service = input("Level of service (good, fair or bad)? ")
# split = int(input("Split how many ways? "))
# good = 0.20
# fair = 0.15
# bad = 0.10
# if service == "good":
#     print("Tip Amount: ${:.2f}".format(bill * good))
#     print("Total Amount: ${:.2f}".format(bill * (1+good)))
#     print("Amount per person:: ${:.2f}".format((bill * (1+good))/split))
# elif service == "fair":
#     print("Tip Amount: ${:.2f}".format(bill * fair))
#     print("Total Amount: ${:.2f}".format(bill * (1+fair)))
#     print("Amount per person:: ${:.2f}".format((bill * (1+fair))/split))
# else:
#     print("Tip Amount: ${:.2f}".format(bill * bad))
#     print("Total Amount: ${:.2f}".format(bill * (1+bad)))
#     print("Amount per person:: ${:.2f}".format((bill * (1+bad))/split))


# def numbers():
#     count = 1
#     while count < 11:
#         print(count)
#         count += 1
# numbers()

# def more_coins():
#     coins = 0
#     get_coin = input("Do you want a coin? ")
#     while get_coin == "yes":
#         coins += 1
#         print(coins)
#         get_coin = input("Do you want a coin? ")
#     print("Bye")


# more_coins()



        




