# rock, scissors, paper
import random


def check_match(decision, computer_choice):
    if decision == computer_choice:
        print(f"""
        !!! IT'S A TIE !!!
{show_gestures}
        """)
    else:
        check_winner(decision, computer_choice)


def check_winner(decision, computer_choice):
    if (decision == 0 and computer_choice == 2) or\
       (decision == 1 and computer_choice == 0) or \
       (decision == 2 and computer_choice == 1):
        print(f"""
        !!!YOU WIN!!!
{show_gestures}
        """)
    else:
        print(f"""
        !!!YOU LOSE!!!
{show_gestures}
        """)


def will_next(game):
    next_game = input("Will you continue? y or n? ")
    if next_game.lower() == "n":
        return False
    return game


rock = """Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
paper = """Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
rules = """Here the WIN conditions:
Rock brakes the Scissors
Paper covers the Rock
Scissors cut the Paper
"""

# Starting sentence
print("Welcome to the Rock, Paper, Scissors game\n"
      "type: help for instructions\n"
      "or type 0 for Rock, 1 for Paper, and 2 for Scissors")

conditions = [rock, paper, scissors]
is_game = True

while is_game:
    user_choice = input("Your decision: ")
    computer_choice = random.randint(0, 2)
    decision = computer_choice
    if user_choice == "help":
        print(f"{rock}\n{paper}\n{scissors}\n{rules}")
        user_choice = input("So you know the rules. Make a decision: ")
    if user_choice.lower() == "rock" or user_choice == "0":
        decision = 0
    elif user_choice.lower() == "paper" or user_choice == "1":
        decision = 1
    elif user_choice.lower() == "scissors" or user_choice == "2":
        decision = 2
    else:
        print("\n\nCarefully, that way you can't win computer\n")
    show_gestures = f"""
        Your choice is {conditions[decision]}
        The computer choice is {conditions[computer_choice]}
        """
    check_match(decision, computer_choice)
    is_game = will_next(is_game)
quit()
