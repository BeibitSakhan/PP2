def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Использование
print_profile(name="Иван", age=25, city="Москва")
# Выведет:
# name: Иван
# age: 25
# city: Москва