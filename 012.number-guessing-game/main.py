from art import logo
import random
import os


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def create_number():
    """Returns a random number between 1-100."""
    random_num = random.randint(1,100)
    return random_num

def check_answer(guess,answer,turns):
    """Check the value entered by the user is correct"""

    if guess > answer:
        print ("Too high.")
        return turns - 1
    elif guess < answer:
        print ("Too low.")
        return turns - 1
    else:
        print (f"You got it! The answer was {answer}.")

def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Plase type 'easy or 'hard'")

def play_game():

    print(logo)

    answer = create_number()
    is_game_over = False

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    turns = set_level()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
          print("Guess again.")

while input("Do you want to play a Number Guessing Game? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()

