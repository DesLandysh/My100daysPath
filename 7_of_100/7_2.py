import random

word_list = ["python", "godzilla", "revolver"]

chosen_word = random.choice(word_list)

print(chosen_word)  # Debug-line


# step 2
# TODO-1 Create an empty list called display.
# for each letter in the choosen_word, add a "_" to 'display'
display = []

guess = input("Give a letter: ").lower()

# TODO-2 Loop through each position in the chosen_word;
# if the letter at that position matches "guess"
#   then reveal that letter in 'display' at that position

for letter in chosen_word:
    if letter == guess:
        display.append(letter)
    else:
        display.append("_")

# TODO-3 Print 'display' and you should see the guessed letter in the correct position
# and every other letter replace with "_"
# Just for 1 letter, multichoice is next lesson

print(display)