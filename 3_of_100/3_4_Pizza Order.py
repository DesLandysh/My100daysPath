# Pizza order

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size Pizza: +$1
#
# size = S, M, L
# add_pepperoni = "Y/N"
# extra_cheese = "Y/N"
#
# output: "Your final bill is: $SUM"


print("Welcome to Python Pizza Delivery!")
size = "l" # input("What size pizza do you want? s, m, l? ")
add_pepperoni = "y" # input("Do you want pepperoni? y/n? ")
extra_cheese = "n" # input("Do you want extra cheese? y/n? ")


def print_size(size):
    printed_size = ""
    if size == 's':
        return "small"
    elif size == 'm':
        return "medium"
    elif size == 'l':
        return "large"
    return


def print_addons(add_pepperoni, extra_cheese):
    addons = " without "
    if add_pepperoni == "y" and extra_cheese == "y":
        return " with pepperoni and extra cheese "
    elif add_pepperoni == "y" and extra_cheese == "n":
        return " with pepperoni "
    elif add_pepperoni == "n" and extra_cheese == "y":
        return " with extra cheese "
    else:
        return addons


printed_size = print_size(size)
additives = print_addons(add_pepperoni, extra_cheese)

bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill =+ 20
elif size == "l":
    bill += 25
else:
    print("Custom shape is not available")
if add_pepperoni == "y":
    if size == "s":
        bill += 2
    elif size == "l" or size == "m":
        bill += 3
if extra_cheese == "y":
    bill += 1
print(f"Your ordered {printed_size} pizza{additives}additives, and your bill is ${bill}")
