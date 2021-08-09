# Step 4

import random
from day_7_art import stages, logo
from dictionary import word_list

cur_word_list = word_list
chosen_word = random.choice(cur_word_list)
length = len(chosen_word)
lives = 6
used_letters = []

# Create slots for guessing letters
display = []
for _ in range(length):
    display += "_"

print(logo)
print(f"\nHidden word consist of {length} letters\n")
is_game = True
while is_game:
    guess = input("Give a letter: ").lower()

    if guess in used_letters:
        guess = input("This letter is already used\nGive another letter: ").lower()
    else:
        used_letters += guess

    for pos in range(length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} isn't in the word")
        if lives == 0:
            print("""
            !!! YOU LOSE !!!
            """)
            is_game = False

# Join all the elements in list and turn in into a String.
    print(f"{' '.join(display)}")

    print(stages[lives])

    if not "_" in display:
        print("""
        !!! YOU WIN !!!
        """)
        is_game = False

quit()
