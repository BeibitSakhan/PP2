from functools import reduce

nums = [1, 2, 3, 4, 5]

# 1
squares = list(map(lambda x: x**2, nums))

# 2
prices = list(map(int, ["10", "20", "30"]))

# 3
evens = list(filter(lambda x: x % 2 == 0, nums))

# 4
words = ["hi", "python", "ai", "generator"]
long_words = list(filter(lambda w: len(w) > 3, words))

# 5
total = reduce(lambda x, y: x + y, nums)