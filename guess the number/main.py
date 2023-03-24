#number guessing game
import random
import art
print(art.logo)
#Add welcome text
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")
choice = random.randint(1, 100)
easy_turns = 10
hard_turns = 5

def check_answer(guess, choice, turns):
    if guess < choice:
        print("Too Low.")
        return turns -1
    elif guess > choice:
        print("Too high.")
        return turns - 1
    else:
        print(f"That's correct, good Job!The correct answer was {choice}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_turns
    if level == "hard":
        return hard_turns

def play_game():

    turns = set_difficulty()

    guess = 0
    while guess != choice:
        print(f"You have {turns} remaining.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, choice, turns)
        if turns == 0:
            print(f"You are out of guesses you lose. The correct number was {choice}.")
            return




play_game()
#We need to compare the computer selection and the user collection

