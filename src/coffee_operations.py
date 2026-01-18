def show_depleted_resources(depleted_resources):
    print(f"Sorry there is not enough {", ".join(depleted_resources)}.")

def get_specific_flavor(user_choice, coffee_flavors):
    all_the_flavors = list(coffee_flavors.keys())
    specific_flavor = all_the_flavors[user_choice - 1]

    return specific_flavor

def menu(coffee_flavors):
    print(f"{"*" * 20}MENU{"*" * 20}")

    for idx, flavor in enumerate(coffee_flavors.keys()):
        print(f"{idx + 1}. {flavor}")

def update_resources(all_resources, order_resources):
    for resources, value in order_resources.items():
        if resources == "money":
            all_resources[resources] += value
            continue
        all_resources[resources] -= value

def get_report(actual_resources):
    print(f"{"*" * 20}Actual resources{"*" * 20}")
    
    for element, value in actual_resources.items():
        print(f"{element.capitalize()}: ", end="")
        
        if element in ["water", "milk"]:
            print(f"{value} mL")
        elif element == "coffee":
            print(f"{value}g")
        else:
            print(f"${value}")

def get_resources_without_money(modified_resources):
    new_resources = {}

    for resource, value in modified_resources.items():
        if resource == "money":
            continue
        new_resources[resource] = value
    
    return new_resources

def get_coins():
    coins_accepted = ["quarters", "dimes", "nickles", "pennies"]

    coins_entered = {}

    print("Please insert coins.")

    for coin in coins_accepted:
        money = int(input(f"How many {coin}?: "))
        coins_entered[coin] = money

    return coins_entered

def refill_machine(old_resources):
    for resource, value in old_resources.items():
        if resource == "money":
            continue
        old_resources[resource] += 300


def check_resources(actual_resources, flavor, coffee_flavors):
    resources_needed = coffee_flavors[flavor].get("ingredients")
    depleted_resources = []

    can_make_order = True

    for element, value in resources_needed.items():
        if element == "money":
            continue
        if actual_resources[element] < value:
            depleted_resources.append(element)
            can_make_order = False
    
    return {"can_make_order": can_make_order, "depleted_resources": depleted_resources}

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