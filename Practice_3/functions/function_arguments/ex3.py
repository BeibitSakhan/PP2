def make_coffee(size="средний", sugar=True):
    sweet = "с сахаром" if sugar else "без сахара"
    print(f"Ваш {size} кофе {sweet} готов!")

make_coffee()               # Использует оба значения по умолчанию
make_coffee("большой")      # Изменит размер, сахар оставит True
make_coffee("малый", False) # Изменит оба параметра