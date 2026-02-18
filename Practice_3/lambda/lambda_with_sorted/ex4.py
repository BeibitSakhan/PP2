users = [
    {"name": "Иван", "age": 30},
    {"name": "Анна", "age": 20},
    {"name": "Олег", "age": 25}
]

# Сортируем по значению ключа 'age'
young_to_old = sorted(users, key=lambda u: u['age'])

print(young_to_old)
# [{'name': 'Анна', 'age': 20}, {'name': 'Олег', 'age': 25}, {'name': 'Иван', 'age': 30}]