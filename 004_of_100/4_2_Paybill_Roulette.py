# Banker Roulette - who will pay the bill

# Select a random name from a list of names. The person selected will have to pay for everybody's food bill
# Don't use choice() function
# Example input [Angela, Ben, Jenny, Michael, Chloe]
# Example output: "Michael is going to buy the meal today!"
import random


# Code
name_string = "Angela, Ben, Jenny, Michael, Chloe"  # input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")

# Solution
print(f"{name_string}, welcome to the Brittish Roulette! Bankrupt each other!")
chosen_one = names[random.randint(0, len(names)-1)]
print(f"{chosen_one} is going to buy the meal today!")
