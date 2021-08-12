# Step 3
import random

word_list = ["python", "godzilla", "revolver"]

chosen_word = random.choice(word_list)
length = len(chosen_word)

print(chosen_word)  # Debug-line

display = []
for _ in range(length):
    display += "_"

# TODO-1: Use a while loop to let the user guess again.
#   Loop should only stop once the user has guessed all the letters in the chosen_word
#   and 'display' has no more blanks ("_"). Then you can tell the user they've won.
is_game = True
while is_game:
    guess = input("Give a letter: ").lower()
    for pos in range(length):
        if chosen_word[pos] == guess:
            display[pos] = chosen_word[pos]
    print(display)
    if "_" in display:
        print("You win!")
        is_game = False

# official code
"""end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

print(display)

if "_" not in display:
    end_of_game = True
    print("You win.")"""