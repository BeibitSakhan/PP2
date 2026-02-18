numbers = [10, -5, 20, -30, 5]

# Сортируем по абсолютному значению (без учета минуса) от большего к меньшему
abs_sorted = sorted(numbers, key=lambda x: abs(x), reverse=True)

print(abs_sorted)  # [-30, 20, 10, -5, 5]