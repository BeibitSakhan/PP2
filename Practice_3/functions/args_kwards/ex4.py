def logger(func, *args, **kwargs):
    print(f"Запускаю функцию {func.__name__}...")
    return func(*args, **kwargs)

def say_hello(name, greeting="Привет"):
    return f"{greeting}, {name}!"

# Передаем аргументы через посредника
print(logger(say_hello, "Алексей", greeting="Добрый день"))