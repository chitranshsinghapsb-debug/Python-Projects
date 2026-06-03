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
}

money = 0.00
def transaction():
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickels = float(input("how many nickels?: "))
    pennies = float(input("how many pennies?: "))
    total_paid = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    return total_paid

def Report():
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}gm")
        print(f"Money : ${money}")
           
def coffee_machine(choice):
    global money 
    
    for key in MENU[choice]["ingredients"]:
        if resources[key] >= MENU[choice]["ingredients"][key]:
            resources[key] -= MENU[choice]["ingredients"][key]
        else:
            print(f"Sorry there is not enough {key}.​")
            return
        
    print("Please insert coins.")
    payment = transaction()
    if payment > MENU[choice]["cost"]:
        payment -= MENU[choice]["cost"]
        money +=  MENU[choice]["cost"]
        print( f"Here is your {choice}. Enjoy!")
        print(f"Here is ${payment} dollars in change.")
    elif payment < MENU[choice]["cost"]:
        print("​Sorry that's not enough money. Money refunded.")
    else:
        money +=  MENU[choice]["cost"]
        print( f"Here is your {choice}. Enjoy!")

is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_on = False  # This stops the loop safely
    elif user_choice == "report":
        Report()
    elif user_choice in MENU:
        coffee_machine(user_choice)
    else:
        print("Invalid choice. Please pick a drink or type 'off'.")