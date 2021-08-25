# Number Guessing Game
# from 1 to 100 randint
# 2 modes easy = 10 attempts, hard = 5
# if too high - print it
# if too low - print it
# You got it! the answer was {num} or guess again
# count attempts remaining to guess the number
# no re_game
# Create todo-list
# Create an art logo
# an hour to realization

# 20:56 start
import random
from art import logo

attempts = 0
hidden_number = random.randint(1, 100)
print(logo)
mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if mode == "easy":
    attempts = 10
else:
    attempts = 5
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > hidden_number:
        print("Too high.\nGuess again")
    elif guess < hidden_number:
        print("Too low.\nGuess again")
    else:
        print(f"You got it! The answer was {hidden_number}")
        break
    attempts -= 1
if attempts != 0:
    if mode == 'hard':
        print(f"You've made it for {5 - attempts} attempts")
    else:
        print(f"You've made it for {10 - attempts} attempts")
else:
    print("Game over! You have no attempts to continue")

# 21:11 finish