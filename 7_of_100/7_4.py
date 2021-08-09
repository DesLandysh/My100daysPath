# Step 4
import random

word_list = ["python", "godzilla", "revolver"]

stages = {6: """
 +---+
 |   |
     |
     |
     |
     |
=======
""", 5: """
 +---+
 |   |
 o   |
     |
     |
     |
=======
""", 4: """
 +---+
 |   |
 o   |
 O   |
     |
     |
=======
""", 3: """
 +---+
 |   |
 o   |
/O   |
     |
     |
=======
""", 2: """
 +---+
 |   |
 o   |
/O\\  |
     |
     |
=======
""", 1: """
 +---+
 |   |
 o   |
/O\\  |
/    |
     |
=======
""", 0: """
 +---+
 |   |
 o   |
/O\\  |
/ \\  |
     |
=======
"""}


chosen_word = random.choice(word_list)
length = len(chosen_word)
lives = 6
# TODO-1: Create a var called 'lives' to keep track of number of lives left.
#   set 'lives' to equal 6

# print(chosen_word)  # Debug-line

display = []
for _ in range(length):
    display += "_"


is_game = True
while is_game:
    guess = input("Give a letter: ").lower()
    for pos in range(length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose!")
            is_game = False
# TODO-2: if guess is not a letter in the chosen_word,
#   then reduce 'lives' by 1.
#   If lives goes down to 0 then
#   the game should stop and it should print "You lose."

#Join all the elements in list and turn in into a String.
    print(f"{' '.join(display)}")

    print(stages[lives])

    if not "_" in display:
        print("You win!")
        is_game = False


# TODO-3: print the ASCII art from 'stages' that corresponds
#   to the curent number of 'lives' the user has remaining.


