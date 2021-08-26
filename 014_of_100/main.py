# Higher/Lower game

from art import logo, vs
from days_game_data import data
from random import randint

ndata = data  # prevent sudden changes in a side-file content
score = 0  # global


def clear():
    print("\n" * 30)


def next_item_from_game_data():
    return randint(0, len(ndata) - 1)


def printf(index, letter):
    print(f'Compare {letter}: {ndata[index]["name"]}, a {ndata[index]["description"]}, from {ndata[index]["country"]}')


def next_and_check_unique(index_a, used):
    index_b = next_item_from_game_data()
    if index_b == index_a or index_b in used:
        return next_and_check_unique(index_b, used)  # requires return to prevent None-type output
    else:
        return index_b


def decorated_print(line_a, line_b):
    print(logo)
    printf(line_a, "A")
    print(vs)
    printf(line_b, "B")


def compare(index_a, index_b):
    a_value = ndata[index_a]["follower_count"]
    b_value = ndata[index_b]["follower_count"]
    global score
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A' and a_value > b_value:
        score += 1
        print(f"You got it! Current score: {score}\n")
    elif choice == 'B' and a_value < b_value:
        score += 1
        print(f"You got it! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong! Final score: {score}\n")


def main():
    print(logo)
    used = []
    last_index = next_item_from_game_data()

    while len(used) != len(ndata) - 1:
        start_index = last_index
        used.append(start_index)  # Stopper
        last_index = next_and_check_unique(start_index, used)
        decorated_print(start_index, last_index)
        compare(start_index, last_index)
        clear()
    print(f"Congratulations! You finished! Your score: {score}")


if __name__ == "__main__":
    main()
