numbers = [1, 2, 3, 4, 5]

# Применяем lambda x: x**2 к каждому элементу
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # [1, 4, 9, 16, 25]