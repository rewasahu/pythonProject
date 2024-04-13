MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "coffee": 100,
    "water": 300,
    "milk": 200,
}
sales = 0


def is_resource_sufficient(order_ingredients):
    for ing in order_ingredients:
        if order_ingredients[ing] > resources[ing]:
            print(f"Sorry there is not enough {ing}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    coins = {
        "Quarters": 0.25,
        "Dimes": 0.10,
        "Nickles": 0.05,
        "Pennies": 0.01
    }
    value = 0
    for coin in coins:
        inp = int(input(f"How many {coin}?: "))
        value += round(inp * coins[coin], 2)
    return value


def check_transaction(value, order_cost):
    if value < order_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:

        change = round((value - order_cost),2)
        print(f"Hee is ${change} dollars in change.")
        global sales
        sales += order_cost
        return True


def make_coffee(order, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"“Here is your {order}. Enjoy your ☕")


machine_ON = True
while machine_ON:
    order = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        machine_ON = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}"
              f"\nMoney:${sales}")
    else:
        drink = MENU[order]
        order_ingredients = drink["ingredients"]
        order_cost = drink["cost"]
        if is_resource_sufficient(order_ingredients):
            if check_transaction(process_coins(), order_cost):
                make_coffee(order, order_ingredients)
