# Prime number checker up to 100
# 2 is the prime number (2, 1)
# is not a prime number (4, 2, 1)
# It's a prime number / It's not a prime number

def prime_checker(number):
    """if (number % 2 == 0 and number != 2) or\
       (number % 3 == 0 and number != 3) or\
       (number % 5 == 0 and number != 5) or\
       (number % 7 == 0 and number != 7):
        print("It's not a prime number")
    else:
        print("It's a prime number")"""
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
