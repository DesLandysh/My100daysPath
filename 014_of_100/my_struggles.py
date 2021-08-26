# Higher/Lower game

# Game compares numeric values ({'follower_count'} of each name previous stat vs new info
# Game checks, and if it's false = game over - "Sorry, that's wrong. Final score: 0",
#   else it count score +1 - "You're right! Current score: 1
# Name consists from game_data keys: Compare A: {"name"}, {"description"}, from {"country"}
# Game asks Who has more followers? Type 'A' or 'B': _

# 3 So, game_data is a list of dicts, and it can be indexed from 0 to len(list)
# 1 Import art, game_data and random
# 2 game_data must be protected and copied to new list, because it will need to pop/delete the used element
# 4 randomization choice from data
# 5 compare logic

from art import logo, vs
from game_data import data
from random import randint

ndata = data
A, B = "A", "B"
score = 0  # global
# print(ndata[3]["follower_count"])  # test line
# print(ndata[3]["follower_count"] + 7)  # test line
# next_quiz = randint(0, len(ndata))  # func-relaced
# print(next_quiz)  # debug line


def next_item():
    return randint(0, len(ndata) - 1)


def printf(item_index, letter):
    print(f'Compare {letter}: {ndata[item_index]["name"]} {ndata[item_index]["description"]}, from {ndata[item_index]["country"]}')


# print_description(3, "A")  # test line
# print_description(next_item(), "B")  # test line
# index = next_item()
# print_description(index, "B")
# ndata.pop(index)  # remove element from the list after use

# def print_to(index, letter):
#    printf(index, [letter])
#    # ndata.pop(index)  # remove element from the list after use


def compare(index_A, index_B):
    global score
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A' and ndata[index_A]["follower_count"] > ndata[index_B]["follower_count"]:
        score += 1
        print(f"You got it! Current score is: {score}")
        return False
    elif choice == 'B' and ndata[index_A]["follower_count"] < ndata[index_B]["follower_count"]:
        score += 1
        print(f"You got it! Current score is: {score}")
        return False
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        return True


def next_and_check_unique(index_A, used):
    index_B = next_item()
    stopper = len(ndata)
    if index_B == index_A or index_B in used:
        if stopper == len(used):
            return None
        else:
            return next_and_check_unique(index_A, used)  # requires return to prevent None-type output
    else:
        return index_B


last_index = next_item()
finish = False
print(logo)
used = []
while not finish:
    start_index = last_index
    print(start_index, "st ind")
    try:
        last_index = next_and_check_unique(start_index, used)
        print(last_index, "lt ind")
        printf(start_index, A)
        print(vs)
        printf(last_index, B)
        finish = compare(start_index, last_index)
        used.append(start_index)
        print(used)
    except TypeError:
        print(f"Congratulations! You finished! Your score: {score}")
        finish = True
