class ShoppingCart:
    def __init__(self, customer_name):
        self.customer = customer_name
        self.items = [] # Создаем пустую корзину для каждого клиента

    def add_item(self, item):
        self.items.append(item)

# У каждого покупателя будет свой личный список items
my_cart = ShoppingCart("Alex")
my_cart.add_item("Apple")