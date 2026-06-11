recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.50,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24  # ounces
}


class SandwichMaker:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True if there are enough resources, otherwise False."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total amount of money inserted."""
        print("Please insert coins.")

        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (
            large_dollars * 1.00
            + half_dollars * 0.50
            + quarters * 0.25
            + nickels * 0.05
        )

        return total

    def transaction_result(self, coins, cost):
        """Returns True if payment is accepted, otherwise False."""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deducts ingredients from resources and makes the sandwich."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        """Prints current machine resources."""
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} pound(s)")


machine = SandwichMaker(resources)

is_on = True

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        machine.report()

    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients_needed = sandwich["ingredients"]

        if machine.check_resources(ingredients_needed):
            payment = machine.process_coins()

            if machine.transaction_result(payment, sandwich["cost"]):
                machine.make_sandwich(choice, ingredients_needed)

    else:
        print("Invalid choice. Please choose small, medium, large, report, or off.")