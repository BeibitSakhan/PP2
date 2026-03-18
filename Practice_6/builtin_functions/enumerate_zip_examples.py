names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 1
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# 2
odd_names = [name for i, name in enumerate(names) if i % 2 != 0]

# 3
pairs = list(zip(names, scores))

# 4
score_dict = dict(zip(names, scores))

# 5
names_back, scores_back = zip(*pairs)