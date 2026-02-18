class Store:
    exchange_rate = 90.0 # Курс доллара

    @staticmethod
    def to_rubles(dollars):
        # Чистая математика: не нужен ни self, ни cls
        return dollars * 90.0

# Мы можем вызвать это, даже не создавая магазин
price_in_rub = Store.to_rubles(100)
print(f"Цена в рублях: {price_in_rub}") # 9000.0