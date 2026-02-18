users = [
    {"id": 1, "name": "Иван"},
    {"id": 2, "name": "Мария"},
    {"id": 3, "name": "Олег"}
]

# Извлекаем только значения по ключу 'name'
names = list(map(lambda u: u['name'], users))

print(names)  # ['Иван', 'Мария', 'Олег']