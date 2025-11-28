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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def is_sufficient(coffee):
    for ingredients in MENU[coffee]["ingredients"]:
        if not resources[ingredients] >= MENU[coffee]["ingredients"][ingredients] :
            print(f"Sorry there is not enough {ingredients}.")
            return False
    return True

def check_money(coffee):
    print("Please enter coins.")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))

    inserted_coin = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if inserted_coin >= MENU[coffee]["cost"]:
        print(f"Here is ${round(inserted_coin - MENU[coffee]["cost"], 2)} in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
        resources["money"] += MENU[coffee]["cost"]

        for ingredients in MENU[coffee]["ingredients"]:
            resources[ingredients] -= MENU[coffee]["ingredients"][ingredients]
            print(f"{resources[ingredients]} , {MENU[coffee]["ingredients"][ingredients]}")
    else:
        print("Sorry that's not enough money. Money refunded.")

def work():
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "off" :
        return 0
    elif prompt == "report":
        report()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        if is_sufficient(prompt):
            check_money(prompt)
    else:
        print("Invalid input, try again.")
    work()

work()
