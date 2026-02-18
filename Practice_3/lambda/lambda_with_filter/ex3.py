users = [
    {"name": "Ivan", "age": 17},
    {"name": "Anna", "age": 22},
    {"name": "Oleg", "age": 15},
    {"name": "Maria", "age": 30}
]

# Оставляем пользователей, чей возраст >= 18
adults = list(filter(lambda u: u['age'] >= 18, users))

print(adults)  # [{'name': 'Anna', 'age': 22}, {'name': 'Maria', 'age': 30}]