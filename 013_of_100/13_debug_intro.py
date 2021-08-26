# Describe Problem
def my_function():
    for i in range(1, 21):
    # for i in range(1, 20): - Bug
        if i == 20:
            print("You got it")


my_function()
# Easy. 20 is out of range because syntax (1, 20) not include 20.

# Reproduce the bug
from random import randint

dice_img = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
# or dice_num = randint(0, 5)
print(dice_img[dice_num - 1])
# print(dice_img[dice_num]) - Bug
# Easy. list start with index 0 but dice_num takes values from 1 to 6. IndexError

# Play Computer
year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994: - Refactor requires
if 1980 < year < 1994:
    print("You are a millennial.")
# elif year > 1994: - Bug
elif year >= 1994:
    print("You are a Gen Z.")
else:
    print("Grace Hopper found a moth in relay")
# easy, but not too obvious. Else statement is missed, and 1994 year is missed

# Fix the Errors
# age = input("How old are you? ")
age = int(input("How old are you? "))
if age > 18:
    # print("You can drire at age {age}")
    print(f"You can drive at age {age}")
# Easy. TypeError. input: str, but if statement requires int
# print wasn't indented, and not formatted

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number od words per page: ")) - Bug
word_per_page = int(input("Number od words per page: "))
total_words = pages * word_per_page
print(total_words)
# Easy. word_per_page isn't assign, it tries to equal values.

# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    # b_list.append(new_item) - Bug
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
# easy. indent error, b_list takes only last item to square it.
