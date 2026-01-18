import math

from data import coffee_flavors, resources


def check_resources(actual_resources, flavor):
    resources_needed = coffee_flavors[flavor].get("ingredients")
    depleted_resources = []

    can_make_order = True

    for ingredients, value in resources_needed.items():
        if actual_resources[ingredients] < value:
            depleted_resources.append(ingredients)
            can_make_order = False
    
    return {"can_make_order": can_make_order, "depleted_resources": depleted_resources}

def menu():
    print(f"{"*" * 20}Mandalorian Coffee{"*" * 20}")
    print(f"{"*" * 20}MENU{"*" * 20}")

    for idx, flavor in enumerate(coffee_flavors.keys()):
        print(f"{idx + 1}. {flavor}")

def get_specific_flavor(user_choice):
    all_the_flavors = list(coffee_flavors.keys())
    specific_flavor = all_the_flavors[user_choice - 1]

    return specific_flavor

def get_report(actual_resources):
    print(f"{"*" * 20}Actual resources{"*" * 20}")
    
    for ingredients, value in actual_resources.items():

        print(f"{ingredients.capitalize()}: {value}{"mL" if ingredients in ["water", "milk"] else "g"}")

def show_depleted_resources(depleted_resources):
    print(f"Sorry there is not enough {", ".join(depleted_resources)}.")

def get_coins():
    coins_accepted = ["quarters", "dimes", "nickles", "pennies"]

    coins_entered = {}

    for coin in coins_accepted:
        money = int(input(f"How many {coin}?: "))
        coins_entered[coin] = money

    return coins_entered

def process_coins(coins):
    # coins_accepted = ["quarters", "dimes", "nickles", "pennies"]

    total = 0
    dollar_value = 0

    for coin_name, coin_value in coins.items():
        if coin_name == "quarters":
            dollar_value = coin_value * 0.25
        elif coin_name == "dimes":
            dollar_value = coin_value * 0.10
        elif coin_name == "nickles":
            dollar_value = coin_value * 0.05
        elif coin_name == "pennies":
            dollar_value = coin_value * 0.01
        
        total += dollar_value

    return total


def main():

    while True:
        menu()

        choice = input("What you would like today? ")

        if choice == "report":
            get_report(resources)
            continue

        choice = int(choice)

        chosen_flavor = get_specific_flavor(choice)

        internal_report = check_resources(resources, chosen_flavor)


        if not internal_report["can_make_order"]:
            show_depleted_resources(internal_report["depleted_resources"])
            continue

        # TODO: Process coins, coins will be equal to x amount of dollars
        coffee_cost = coffee_flavors[chosen_flavor].get("cost")

        customer_coins = get_coins()

        money_entered = process_coins(customer_coins)
        
        # TODO: Check if coins amount can buy the flavor selected
        if money_entered < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
            continue


        # TODO: Process change, if there is change
        # change = money_entered - coffee_cost
        # if change > 0:
        #     print(f"Here is ${math.round(change)} in change.")
        # else:
        #     print(f"No change.")

        # TODO: Add the money to the system

        # TODO: Update resources

        # TODO: Present order
  
            
    


if __name__ == "__main__":
    main()