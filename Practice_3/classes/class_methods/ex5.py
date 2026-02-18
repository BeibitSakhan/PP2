class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @classmethod
    def from_dict(cls, data):
        # Если в словаре есть данные, создаем объект
        return cls(data['brand'], data['model'], data['price'])

# Данные, которые мы получили (например, из API)
api_data = {"brand": "Apple", "model": "iPhone 15", "price": 999}

# Создаем объект одной командой
phone = Smartphone.from_dict(api_data)
print(phone.model) # iPhone 15