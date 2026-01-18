from data import coffee_flavors, resources


def check_resources(actual_resources, flavor):
    resources_needed = coffee_flavors[flavor].get("ingredients")

    can_make_order = True

    for ingredients, value in resources_needed.items():
        if actual_resources[ingredients] < value:
            can_make_order = False

    return can_make_order

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
        

def main():

    while True:
        menu()

        choice = input("What you would like today?")

        if choice == "report":
            get_report(resources)
            continue


        chosen_flavor = get_specific_flavor(choice)

        have_resources = check_resources(resources, chosen_flavor)
    

    

if __name__ == "__main__":
    main()