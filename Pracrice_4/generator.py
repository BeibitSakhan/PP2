# 1
def infinite_ids(start=0):
    while True:
        yield start
        start += 1

# 2
def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# 3
def read_huge_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()

# 4
squares = (x*x for x in range(10))

# 5
def only_evens(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n