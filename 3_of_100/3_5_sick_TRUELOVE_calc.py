# Love Calculator
"""
    Take both people's name and check for the number of times the letter in the word TRUE occurs.
    Then check for the number of times the letters in the word LOVE occurs.
    Then combine these numbers to make a 2 digit number.

    for Love Score less than 10 or greater than 90, the message should be:
        "Your score is x, you go together like coke and mentos."
    for Love Score between 40 and 50, the message should be:
        "your score is y, you are alright together."
    otherwise, the message will inst be their score, e.g.:
        "your score is z"
"""
# starter block
print("Добро пожаловать в ВЦИОМ!")
name1 = "Vladimir Putin"  # input("What's your name? \n")
name2 = "Russian people"  # input("What is their name? \n")
# starter block

# Solution
combined_name = (name1 + name2).lower()
true_checkblock = ("t", "r", "u", "e")
love_checkblock = ("l", "o", "v", "e")


def count_letter(name: str, checkblock) -> str:
    sum_letters = 0
    for i in checkblock:
        if i in name:
            sum_letters += name.count(i)
    cont = str(sum_letters)
    return cont


# Getting result of counting and make 1st as tens and 2nd as nums through concatenation,
# and turn it in 2-digit number
x = int(count_letter(combined_name, true_checkblock) + count_letter(combined_name, love_checkblock))

if x < 10 or x > 90:
    print(f"Your score is {x}%, you go together like coke and mentos")
elif 40 < x < 50:
    print(f"Your score is {x}%, you are alright together")
else:
    print(f"{x}% of {name2} loves you, {name1.title()}!")

# done!
# I guess I know ВЦИОМ algorithms
