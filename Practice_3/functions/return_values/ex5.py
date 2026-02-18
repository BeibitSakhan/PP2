def get_even_numbers(limit):
    evens = [i for i in range(limit) if i % 2 == 0]
    return evens

numbers = get_even_numbers(10)
print(numbers) # [0, 2, 4, 6, 8]