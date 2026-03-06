class Vehicle:
    def move(self):
        print("Транспорт движется")

class Plane(Vehicle):
    def move(self): # Переопределяем метод
        print("Самолет летит по небу")

# Использование
v = Vehicle()
p = Plane()
v.move() # Транспорт движется
p.move() # Самолет летит по небу