from coffee_operations import *
from art import logo
from data import coffee_flavors, resources

def main():
    able_to_operate = True
    modified_resources = get_resources_without_money(resources)

    while able_to_operate:
        print(logo)
        menu(coffee_flavors)

        choice = input("What would you like today? ")

        if choice == "report":
            get_report(resources)
            continue

        if choice == "off":
            able_to_operate = False
            print("System has been put under maintenance 🚧")
            continue

        if choice == "refill":
            print("System resources has been refilled.")
            refill_machine(resources)
            continue

        choice = int(choice)

        chosen_flavor = get_specific_flavor(choice, coffee_flavors=coffee_flavors)

        internal_report = check_resources(resources, chosen_flavor, coffee_flavors)

        if not internal_report["can_make_order"]:
            show_depleted_resources(internal_report["depleted_resources"])
            continue

        # Process coins, coins will be equal to x amount of dollars
        print(f"{"*" * 20}Processing{"*" * 20}")
        coffee_cost = coffee_flavors[chosen_flavor].get("cost")

        customer_coins = get_coins()

        money_entered = process_coins(customer_coins)
        
        # Check if coins amount can buy the flavor selected
        if money_entered < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
            continue


        # Process change, if there is change
        change = money_entered - coffee_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        else:
            print(f"No change.")

        # Add the money to the system and update resources
        elements = coffee_flavors[chosen_flavor].get("ingredients")
        elements["money"] = coffee_flavors[chosen_flavor].get("cost")
        resources_to_remove = elements

        update_resources(resources, resources_to_remove)

        # Present order
        print(f"\nHere is your {chosen_flavor} 🍵 Enjoy!")
        input("Press enter to continue... ")
  

if __name__ == "__main__":
    main()