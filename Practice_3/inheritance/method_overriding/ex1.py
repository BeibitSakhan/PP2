class Animal:
    def make_sound(self):
        return "Издает какой-то звук"

class Dog(Animal):
    def make_sound(self): # Переопределение
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self): # Переопределение
        return "Мяу!"

# Каждый объект использует свою версию метода
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())