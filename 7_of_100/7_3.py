# Step 3
import random

word_list = ["python", "godzilla", "revolver"]

chosen_word = random.choice(word_list)
length = len(chosen_word)
print(chosen_word)  # Debug-line

display = []
for _ in range(length):
    display += "_"

guess = input("Give a letter: ").lower()

for pos in range(length):
    if chosen_word[pos] == guess:
        display[pos] = chosen_word[pos]

print(display)