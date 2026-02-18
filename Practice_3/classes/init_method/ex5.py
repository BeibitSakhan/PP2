class Player:
    def __init__(self, name, age):
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным!")
            self.age = 0
        else:
            self.age = age
        self.name = name

# Попытка создать игрока с ошибкой
p1 = Player("Max", -5) # Выведет ошибку и поставит 0