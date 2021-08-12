# Password generator project


import random


letters = ("a b c d e f g h i j k l m n o p q r s t u v w x y z "
           + "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper()).split()
numbers = "0 1 2 3 4 5 6 7 8 9".split()
symbols = "! # $ % & ( ) * +".split()

print("welcome to the PyPassword Generator!")
nr_letters = 10  # int(input("How many letters would ou like in your password?\n "))
nr_symbols = 2  # int(input("How many symbols would you like?\n "))
nr_numbers = 3  # int(input("How many numbers would you like?\n "))

# solution
# Easy lvl = asd#$123
# Hard lvl = a%33G##a2
password = ""
pass_length = nr_numbers + nr_letters + nr_symbols

"""
while len(password) < pass_length:
    random_choice = random.randint(0, 2)
    if random_choice == 0:
        if nr_symbols > 0:
            password += random.choice(symbols)
            nr_symbols -= 1
    elif random_choice == 2:
        if nr_numbers > 0:
            password += random.choice(numbers)
            nr_numbers -= 1
    else:
        password += random.choice(letters)
print(password)
"""
# Official 100dayofCode solution
word = []
for char in range(1, nr_letters + 1):
    word.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    word.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    word.append(random.choice(numbers))
random.shuffle(word)
for char in word:
    password += char
print(password)

