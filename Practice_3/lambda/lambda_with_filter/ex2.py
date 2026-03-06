words = ["apple", "it", "python", "hi", "code", "ai"]

# Оставляем слова длиннее 3 символов
long_words = list(filter(lambda s: len(s) > 3, words))

print(long_words)  # ['apple', 'python', 'code']s