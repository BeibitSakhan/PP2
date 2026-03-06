products = ["iPhone", "iPad", "MacBook", "iMac", "Apple Watch"]

# Оставляем только те, что начинаются на "i"
apple_gadgets = list(filter(lambda p: p.startswith("i"), products))

print(apple_gadgets)  # ['iPhone', 'iPad', 'iMac']s