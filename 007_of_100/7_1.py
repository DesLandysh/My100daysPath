# Hangman logic

# Step 1
import random

word_list = ["Python", "Godzilla", "Revolver"]

# TODO-1 Randomly choose a word from the word_list and assign it to a var called chosen_word.
# TODO-2 Ask the user to guess a letter and assign their answer to a var called guess.lower().
# TODO-3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
guess = input("Give a letter: ").lower()
for letter in chosen_word:
    if letter != guess:
        print("Wrong")
    else:
        print("Right")

# easy