import os
from data import MENU


# formula for clearing the console
def clear():
    os.system('cls')


def user_input():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while order not in MENU.keys() and order not in ['off', 'report']:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return order


def next_action(order):
    if order == 'off':
        return False
    elif order == 'report':
        report(resources)
        return True
    else:
        if check_resources(order):
            if add_coins(order):
                make_coffee(order)
                return True
            else:
                return True
        else:
            return True


def check_resources(order):
    global MENU, resources
    for key in MENU[order]["ingredients"].keys():
        if resources[key] - MENU[order]["ingredients"][key] < 0:
            print(f"Sorry, not enough {key}!")
            return False
    return True


def report(res):
    print(f"Water: {res['water']}ml")
    print(f"Milk: {res['milk']}ml")
    print(f"Coffee: {res['coffee']}gr")
    print(f"Money: ${res['money']}")


def add_coins(order):
    global MENU, COINS, resources
    print(f"The price of the order is ${MENU[order]['cost']}")
    user_coins = {"quarters": input("How many quarters?: "), "dimes": input("How many dimes?: "),
                  "nickles": input("How many nickles?: "), "pennies": input("How many pennies?: ")}
    money_added = 0
    for key in user_coins.keys():
        if user_coins[key] == "":
            continue
        else:
            money_added += int(user_coins[key]) * COINS[key]
    if money_added < MENU[order]['cost']:
        print(f"You added ${money_added}")
        print("Sorry, that's not enough money. Money refunded!")
        return False
    elif money_added == MENU[order]['cost']:
        resources['money'] += MENU[order]['cost']
        return True
    else:
        resources['money'] += MENU[order]['cost']
        change = money_added - MENU[order]['cost']
        print(f"Here is ${change} in change")
        return True


def make_coffee(order):
    global MENU, resources
    for ingredient in MENU[order]['ingredients'].keys():
        resources[ingredient] -= MENU[order]['ingredients'][ingredient]
    print(f"Here is your {order}. Enjoy!")


def main():
    is_on = True
    while is_on:
        order = user_input()
        is_on = next_action(order)


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
COINS = {"quarters": 0.25,
         "dimes": 0.10,
         "nickles": 0.05,
         "pennies": 0.01
         }
main()
