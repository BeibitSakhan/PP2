def order_pizza(size, *toppings, **details):
    print(f"Заказана {size} пицца со следующими топпингами:")
    for topping in toppings:
        print(f"- {topping}")
    
    if "address" in details:
        print(f"Доставка по адресу: {details['address']}")

# Использование
order_pizza("Большая", "пепперони", "грибы", address="ул. Пушкина, 10", phone="123-456")