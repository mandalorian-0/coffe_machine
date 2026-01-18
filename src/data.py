coffee_flavors = {
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100, 
    "money": 0
}

if __name__ == "__main__":

    print(coffee_flavors)
    print(resources)
