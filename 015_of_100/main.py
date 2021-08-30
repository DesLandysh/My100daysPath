# Coffee Machine Program emulator

def p_help():
    print(f"""
Type 'report' to get info about resources.
Type 'cappuccino' to order cappuccino (250ml Water, 24g Coffee, 100ml Milk, $3.00)
Type 'espresso' to order espresso (50ml Water, 18g Coffee, $1.50)
Type 'latte' to order latte (200ml Water, 24g Coffee, 150ml Milk, $2.50)
""")


def report(resources_):
    money_2decimal = round(resources_.get("money"), 2)
    print(f"""
Water: {resources_.get("water")}ml
Milk: {resources_.get("milk")}ml
Coffee: {resources_.get("coffee")}g
Money: ${money_2decimal}
""")


def check_resources(of_receipt, resources_):
    if resources_.get("water") - of_receipt[1] > 0:
        if resources_.get("milk") - of_receipt[2] > 0:
            if resources_.get("coffee") - of_receipt[3] > 0:
                if resources_.get("money") - of_receipt[4] > 0:
                    return True
                else:
                    printer("money")
            else:
                printer("coffee")
        else:
            printer("milk")
    else:
        printer("water")
    return False


def make_coffee(of_receipt, resources_):
    resources_ = add_coins(resources_)
    checked = check_resources(of_receipt, resources_)
    if checked:
        water = resources_.get("water") - of_receipt[1]
        milk = resources_.get("milk") - of_receipt[2]
        coffee = resources_.get("coffee") - of_receipt[3]
        money = resources_.get('money') - of_receipt[4]
        resources_.update({"water": water, "milk": milk, "coffee": coffee, "money": money})
        print(f"Here's your {of_receipt[0]}. Enjoy")
        print(f'Here is ${round(resources_.get("money"),2)} in change')
        return resources_


def add_coins(resources_):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    cons = [quarters, dimes, nickles, pennies]
    index = 0
    money = 0.0
    for key in coins:
        money += coins.get(f"{key}") * cons[index]
        money = round(money, 2)
        index += 1
    resources_.update({"money": money})
    return resources_


def event_listener(key, of_receipt, resources_):
    resources_ = make_coffee(of_receipt[f"{key}"], resources_)
    return resources_


def asker():
    keys = ["latte", "cappuccino", "espresso", "off"]
    key = input("What would you like? 'cappuccino'/'latte'/'espresso' or type 'help': ").lower()
    if key == "help":
        p_help()
        asker()
    elif key == "report":
        report(resources)
        asker()
    elif key in keys:
        return key
    else:
        asker()


def printer(key):
    if key == "money":
        print("Sorry that's not enough money. Money refunded. ")
    else:
        print(f"Sorry there in not enough {key}.")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 50,
    "money": 0.00,
}
receipt = {
    "cappuccino": ["cappuccino", 250, 100, 24, 3.00],
    "espresso": ["espresso", 50, 0, 18, 1.50],
    "latte": ["latte", 200, 150, 24, 2.50]
}
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

off = False
while not off:
    oper_key = asker()
    if oper_key == "off":
        off = True
    else:
        resources = event_listener(oper_key, receipt, resources)
