# 100 days of code version and a little modified with dividing on zero and quit
from day_10_art import logo, clear


def do_add(n1, n2):
    return n1 + n2


def do_sub(n1, n2):
    return n1 - n2


def do_mul(n1, n2):
    return n1 * n2


def do_div(n1, n2):
    try:  # Translated from my v1 version.
        return n1 / n2
    except ZeroDivisionError:
        return 0


operations = {
    "+": do_add,
    "-": do_sub,
    "*": do_mul,
    "/": do_div,
    }


def calculations():
    clear()
    print(logo, "\n")

    num1 = float(input("Enter the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operator = input("pick an operation: ")
        num2 = float(input("Enter the next number?: "))
        calc_function = operations[operator]
        answer = round(calc_function(num1, num2), 1)

        print(f"{num1} {operator} {num2} = {answer}")
        """
        we set dictionary as a switcher key=operator, and value=function
        calc_function return do_math function by key == operator
        then answer = we call calc_function which store the value = func from the dictionary by key=operator
        that's reduces the if/else statements
        
        hmm, such clever.
        """
        flag = input(f"Type 'y' for continue calculating with {answer},\nor type 'n' for a new calculations,\nor type 'q' for exit: ")
        if flag == "y":
            num1 = answer
        elif flag == 'n':
            should_continue = False
            calculations()
        else:  # Any other letter ('q') for exit from program (100 days of code didn't do this option)
            return None


calculations()
