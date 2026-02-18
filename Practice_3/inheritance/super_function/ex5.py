class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Cube(Square):
    def area(self):
        # Вместо Square.area(self) используем super()
        return super().area() * 6 # Площадь поверхности куба

c = Cube(3)
print(c.area()) # 54