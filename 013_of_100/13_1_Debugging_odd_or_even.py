# Debugging Odd or Even
number = int(input("Which number do you want to check? "))

# if number % 2 = 0: - Bug: SyntaxError
if number % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")
