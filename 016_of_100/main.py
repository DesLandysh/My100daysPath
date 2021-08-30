# Coffee Machine OOP ver

# Pre-req code
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# End pre-req code

# 100days of code has a Terrible documentation and tech writing skill
# MenuItem is not used...


def main():
    options = Menu()
    coffee_maker = CoffeeMaker()
    money_changer = MoneyMachine()
    off = False

    while not off:
        asker = input("Welcome to the Coffee Machine, type 'order' or 'report': ")
        if asker == "report":
            coffee_maker.report()
            money_changer.report()
        elif asker == "off":
            off = True
            continue
        order = input(f"Type for make an order {options.get_items()}?: ").lower()
        drink = options.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_changer.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()

