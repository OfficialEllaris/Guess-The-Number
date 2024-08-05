#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    correct_answer = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {correct_answer}")

    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if game_difficulty == "easy":
        guess_attempts = 10
    elif game_difficulty == "hard":
        guess_attempts = 5
    else:
        print("Invalid difficulty choice. Please restart the game and choose 'easy' or 'hard'.")
        return

    while guess_attempts > 0:
        print(f"You have {guess_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}.")
            return
        elif guess < correct_answer:
            print("Too low. \nGuess again.")
        else:
            print("Too high. \nGuess again.")

        guess_attempts -= 1

        if guess_attempts == 0:
            print(f"You've run out of guesses. The correct answer was {correct_answer}.")
            return

play_game()