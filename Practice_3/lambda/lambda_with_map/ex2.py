cities = ["moscow", "london", "PARIS", "tokyo"]

# Делаем каждое слово с большой буквы
capitalized = list(map(lambda c: c.capitalize(), cities))

print(capitalized)  # ['Moscow', 'London', 'Paris', 'Tokyo']