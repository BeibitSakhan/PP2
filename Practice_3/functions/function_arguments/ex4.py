def sum_numbers(*args):
    total = sum(args)
    return f"Сумма {len(args)} чисел: {total}"

print(sum_numbers(10, 20, 30, 40)) # Передали 4 числа