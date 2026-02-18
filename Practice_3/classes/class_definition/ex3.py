class CoffeeCup:
    def __init__(self, capacity):
        self.amount = capacity # e.g., 12 oz

    def drink(self, sip_size):
        self.amount -= sip_size
        print(f"Remaining coffee: {self.amount} oz")

# Usage
my_latte = CoffeeCup(12)
my_latte.drink(4) # Remaining coffee: 8 oz