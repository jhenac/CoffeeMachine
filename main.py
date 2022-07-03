def calculate_funds(no_quarter, no_dimes, no_nickels, no_pennies):
    total_quarter = no_quarter * 0.25
    total_dimes = no_dimes * 0.10
    total_nickels = no_nickels * 0.05
    total_pennies = no_pennies * 0.01
    return total_quarter + total_dimes + total_nickels + total_pennies


def calculate_water(choice):
    remaining_water = resources["water"] - MENU[choice]["ingredients"]["water"]
    resources["water"] = remaining_water


def calculate_milk(choice):
    remaining_milk = resources["milk"] - MENU[choice]["ingredients"]["milk"]
    resources["milk"] = remaining_milk


def calculate_coffee(choice):
    remaining_coffee = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    resources["coffee"] = remaining_coffee


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

MENU["espresso"]["ingredients"]["milk"] = 0
total_sales = 0
continue_dispense = True

while continue_dispense:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')
    if user_choice in ("espresso", "latte", "cappuccino"):
        if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
        elif resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
        elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_funds = calculate_funds(quarter, dimes, nickels, pennies)
            refund = total_funds - MENU[user_choice]["cost"]
            if refund >= 0:
                if refund > 0:
                    print(f"Here is ${refund:.2f} in change.")
                print(f"Here is your {user_choice} ☕. Enjoy!")
                total_sales += MENU[user_choice]["cost"]
                calculate_water(user_choice)
                calculate_milk(user_choice)
                calculate_coffee(user_choice)
            else:
                print("Sorry, that's not enough money. Money refunded.")

    elif user_choice == "report":
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f"Total sales: ${total_sales}")
    elif user_choice == "off":
        continue_dispense = False

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#          a. Check the user’s input to decide what to do next.
#          b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
#             The prompt should show again to serve the next customer.
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
#          a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#            the machine. Your code should end execution when this happens.
# TODO: 3. Print report.
#          a. When the user enters “report” to the prompt, a report should be generated that shows
#             the current resource values. e.g.
#             Water: 100ml
#             Milk: 50ml
#             Coffee: 76g
#             Money: $2.5
# TODO: 4. Check resources sufficient?
#          a. When the user chooses a drink, the program should check if there are enough
#             resources to make that drink.
#          b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#             not continue to make the drink but print: “Sorry there is not enough water.”
#          c. The same should happen if another resource is depleted, e.g. milk or coffee.
# TODO: 5. Process coins.
#          a. If there are sufficient resources to make the drink selected, then the program should
#             prompt the user to insert coins.
#          b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#          c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#             pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# TODO: 6. Check transaction successful?
#          a. Check that the user has inserted enough money to purchase the drink they selected.
#             E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#             program should say “Sorry that's not enough money. Money refunded.”.
#          b. But if the user has inserted enough money, then the cost of the drink gets added to the
#             machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#             Water: 100ml
#             Milk: 50ml
#             Coffee: 76g
#             Money: $2.5
#          c. If the user has inserted too much money, the machine should offer change.
#             E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
# TODO: 7. Make Coffee.
#          a. If the transaction is successful and there are enough resources to make the drink the
#             user selected, then the ingredients to make the drink should be deducted from the
#             coffee machine resources.
#             E.g. report before purchasing latte:
#             Water: 300ml
#             Milk: 200ml
#             Coffee: 100g
#             Money: $0
