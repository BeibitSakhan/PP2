class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Сразу считаем площадь при создании
        self.area = width * height

# Нам не нужно вызывать метод для расчета, площадь уже готова
rect = Rectangle(10, 5)
print(rect.area) # 50