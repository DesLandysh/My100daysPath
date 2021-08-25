# 100dayofcode ver
from random import randint
from art import logo


HARD_MODE = 5
EASY_MODE = 10


def check_answer(guess, answer, turns):
    """
    Checks answer against guess. Returns turns ramaining
    :param guess:
    :param answer:
    :param turns:
    :return:
    """
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! the Answer was {answer}")


def set_difficulty():
    lvl = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if lvl == "easy":
        return EASY_MODE
    else:
        return HARD_MODE


def game():
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You lose!")
            return None
        elif guess != answer:
            print("Guess again")

game()
