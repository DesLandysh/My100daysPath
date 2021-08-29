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


def report(resources_):
    money_2decimal = round(resources_.get("money"), 2)
    print(f"""
Water: {resources_.get("water")}ml
Milk: {resources_.get("milk")}ml
Coffee: {resources_.get("coffee")}g
Money: ${money_2decimal}
""")


def make_coffee(of_receipt, resources_):
    add_coins(resources_)
    # print(resources_)
    # checked = False
    # for i in range(len(of_receipt) - 1):
    #     print(i)
    #     if i == 0:
    #         continue
    #     for k in resources_:
    #         print(resources_.get(f"{k}") - of_receipt[i])
    #         if resources_.get(f"{k}") - of_receipt[i] > 0:
    #             checked = True
    #             continue
    #         else:
    #             printer(k)
    #             checked = False
    # if checked:
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
    # print(key, of_receipt[f"{key}"])
    operations = {
        "latte": make_coffee,
        "cappuccino": make_coffee,
        "espresso": make_coffee,
    }
    execute_function = operations[f"{key}"]
    resources_ = execute_function(of_receipt[f"{key}"], resources_)
    return resources_


def asker():
    keys = ["latte", "cappuccino", "espresso"]
    key = input("What would you like? 'cappuccino'/'latte'/'espresso' or type 'help': ")
    if key == "help":
        p_help()
        asker()
    elif key == "report":
        report(resources)
        asker()
    elif key in keys:
        # print(key)
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


oper_key = asker()
resources = event_listener(oper_key, receipt, resources)
