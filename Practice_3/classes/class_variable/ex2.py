class Item:
    tax_rate = 0.05  # Налог 5% для всех товаров

    def __init__(self, price):
        self.price = price

    def get_total_price(self):
        return self.price * (1 + Item.tax_rate)

# Если государство подняло налог:
Item.tax_rate = 0.10  # Теперь у ВСЕХ товаров налог 10%