words = ["hi", "hello", "a", "python", "it"]
for word in words:
    if len(word) < 3:
        continue
    print("Long word:", word)