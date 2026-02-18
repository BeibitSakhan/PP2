numbers = [2, 15, 8, 22, 5, 30]

# filter(условие, список)
large_numbers = list(filter(lambda x: x > 10, numbers))

print(large_numbers) # [15, 22, 30]