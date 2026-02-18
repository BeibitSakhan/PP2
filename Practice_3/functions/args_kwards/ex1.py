def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Использование
print(multiply_all(2, 3))       # 6
print(multiply_all(2, 3, 4, 5)) # 120