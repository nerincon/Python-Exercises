# GUESS A NUMBER ------> Better with OOP
from random import randint

def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = randint(1,10)
            count = 5
            play_game()
        else:
            print("Thank you for playing!")
            quit()



def play_game():
    print("I am thinking of a number betwwen 1 and 10")
    random_number = randint(1,10)
    count = 5
    while True:
        if count > 0:
            try:
                guess = int(input("What's the number? "))
            except ValueError:
                print("That is not a number!")
                play_again()
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
                play_again()
    
        else:
            print("You ran out of guesses!")
            play_again()

play_game()