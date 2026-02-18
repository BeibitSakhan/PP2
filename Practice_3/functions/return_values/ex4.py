def safe_divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

print(safe_divide(10, 0)) # Функция остановится на ошибке
print(safe_divide(10, 2)) # Функция дойдет до конца и вернет 5.0