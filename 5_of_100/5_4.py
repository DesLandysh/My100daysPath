# fizzbuzz
# print 1 to 100
# if it divs by 3 - fizz instead of number
# if ... 5 - buzz
# if 3 and 5 - fizzbuzz

# General solution
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Specific solution
