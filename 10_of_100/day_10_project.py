# Calculator
from day_10_art import logo, clear


def do_add(n1, n2):
    return n1 + n2


def do_sub(n1, n2):
    return n1 - n2


def do_mul(n1, n2):
    return n1 * n2


def do_div(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 0


print(logo)
operators = ["+", "-", "*", "/"]
program = True

while program:
    next_op = True
    result = int(input("Enter the number: "))
    while next_op:
        print("Example of operators:")
        for op in operators:
            print(f"    {op}")
        operation = input("Choose an operator: ")
        number_2 = int(input("Enter the second number: "))
        if operators[0] == operation:
            tmp = do_add(result, number_2)
            print(f"{round(result, 1)} {operation} {number_2} = {round(tmp, 1)}")
            result = tmp
        elif operators[1] == operation:
            tmp = do_sub(result, number_2)
            print(f"{round(result, 1)} {operation} {number_2} = {round(tmp, 1)}")
            result = tmp
        elif operators[2] == operation:
            tmp = do_mul(result, number_2)
            print(f"{round(result, 1)} {operation} {number_2} = {round(tmp, 1)}")
            result = tmp
        elif operators[3] == operation:
            tmp = do_div(result, number_2)
            print(f"{round(result, 1)} {operation} {number_2} = {round(tmp, 1)}")
            result = tmp
        else:
            print("Not allowed operation")
            continue
        if input("Will you want to continue math? y/n :").lower() == "n":
            print(f"\nFinal result of your calculation is {result}\n")
            next_op = False
    if input("will you want for a new calculations? y/n :").lower() == "n":
        program = False
    clear()

quit()
