class Item:
    discount = 0.1  # Скидка 10% для всех товаров

    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount

# Теперь, если вызвать Item.set_discount(0.2), 
# у всех товаров скидка станет 20% одновременно.