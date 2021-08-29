# Coffee Machine Program emulator

# + 1. Dict of recipies of ingridients
# + 2. Dict of coins
# + 3. List of commands (report, help, order of coffee by name)
# 4. Coin operations (counting inserted sum and then change after the order)
# 5. Check if resources are enough to make a coffee
# 6. Print out info


def p_help():
    print(f"""
Type 'report' to get info about resources.
Type 'cappuccino' to order cappuccino (250ml Water, 24g Coffee, 100ml Milk)
Type 'espresso' to order espresso (50ml Water, 18g Coffee)
Type 'latte' to order latte (200ml Water, 24g Coffee, 150ml Milk)
Type 'change' to refund. 
""")


def report(res):
    money_2decimal = round(res.get("money"), 2)
    print(f"""
Water: {res.get("water")}ml
Milk: {res.get("milk")}ml
Coffee: {res.get("coffee")}g
Money: ${money_2decimal}
""")


def make_coffee(of_receipt):
    print(f"Here is your {of_receipt}. Enjoy!")


def change(resources_, coins_nominal):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    cons = [quarters, dimes, nickles, pennies]
    index = 0
    money = 0.0
    for key in resources_:
        money += coins_nominal.get(key) + cons[index]
        index += 1
    resources_.update({"money": money})
    return resources_


resources = {
    "water": 450,
    "milk": 250,
    "coffee": 50,
    "money": 0.00,
}
receipt = {
    "cap": ["cappuccino", 250, 100, 24, 3.00],
    "esp": ["espresso", 50, 0, 18, 1.50],
    "lat": ["latte", 200, 150, 24, 2.50]
}
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}
operations = {
    "help": p_help(),
    "report": report(resources),
    "latte": make_coffee(receipt.get("lat")),
    "cappuccino": make_coffee(receipt.get("cap")),
    "espresso": make_coffee(receipt.get("esp")),
}


