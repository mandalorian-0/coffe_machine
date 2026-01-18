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

def main():

    while True:
        menu()

        choice = input("What you would like today?")

        if choice == "report":
            get_report(resources)
            continue

        choice = int(choice)

        chosen_flavor = get_specific_flavor(choice)

        internal_report = check_resources(resources, chosen_flavor)


        if not internal_report["can_make_order"]:
            show_depleted_resources(internal_report["depleted_resources"])
            continue
            
    


if __name__ == "__main__":
    main()