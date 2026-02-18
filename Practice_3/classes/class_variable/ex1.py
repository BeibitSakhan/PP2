class Robot:
    population = 0  # Переменная класса

    def __init__(self, name):
        self.name = name
        Robot.population += 1  # Увеличиваем общий счетчик

# Создаем роботов
r1 = Robot("R2D2")
r2 = Robot("C3PO")

print(Robot.population)  # Выведет: 2