import random 
from art import logo
from os import system

def random_number():
    number = random.randint(1,100)
    return number

def play_game(random_number):
    number = random_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = 0
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_level == "hard":
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif game_level == "easy":
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("Wrong choise")
        return

    while attempts > 0:
        guess_num = int(input("Make a gues: "))

        if guess_num == number:
            print(f"You got it! Answer is {number}")
            return
        elif guess_num > number:
            attempts -= 1
            print("Too high")

        else:
            attempts -= 1
            print("Too low")
        print("Guess again.")
        print(f"You have {attempts} attempts reamining to guess the number.")
    if attempts == 0:
        print("You have run out of guesses, you lose.")
        return


end_game = False

while not end_game:
    system('clear')
    print(logo)
    play_game(random_number)

    ask_to_play = input("Do you want to play again? 'y' or 'n' : ")
    if ask_to_play == "y":
        continue
    else: 
        end_game = True
