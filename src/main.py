from data import coffee_flavors, resources

from coffee_operations import *

def main():
    modified_resources = get_resources_without_money(resources)

    while True:
        menu(coffee_flavors)

        choice = input("What you would like today? ")

        if choice == "report":
            get_report(resources)
            continue

        choice = int(choice)

        chosen_flavor = get_specific_flavor(choice, coffee_flavors=coffee_flavors)

        internal_report = check_resources(resources, chosen_flavor, coffee_flavors)

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
        change = money_entered - coffee_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        else:
            print(f"No change.")

        # TODO: Add the money to the system
        elements = coffee_flavors[chosen_flavor].get("ingredients")
        elements["money"] = coffee_flavors[chosen_flavor].get("cost")
        resources_to_remove = elements

        # TODO: Update resources
        update_resources(resources, resources_to_remove)

        # TODO: Present order
        print(f"Here is your {chosen_flavor} 🍵")
  
            
    


if __name__ == "__main__":
    main()