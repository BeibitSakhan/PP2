words = ["яблоко", "аист", "питон", "код"]

# Сортируем по длине (len)
short_to_long = sorted(words, key=lambda s: len(s))

print(short_to_long)  # ['код', 'аист', 'питон', 'яблоко']