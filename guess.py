# GUESS A NUMBER ------>
from random import randint

print("I am thinking of a number betwwen 1 and 10")
random_number = randint(1,10)
count = 5

while True:
    if count > 0:
        guess = int(input("What's the number? "))
        count -= 1
        if guess > random_number:
            print("{} is too high".format(guess))
            if count >0:
                print("You have {} guesses left".format(count))
        elif guess < random_number:
            print("{} is too low".format(guess))
            if count > 0:
                print("You have {} guesses left".format(count))
        else:
            print("You are correct!! You Won!")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == "y":
                random_number = randint(1,10)
                count = 5
            else:
                print("Thank you for playing!")
                break
    else:
        print("You ran out of guesses!")
        break
