class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal): # В скобках указываем родителя
    def speak(self):
        return f"{self.name} говорит Гав!"

# Использование
my_dog = Dog("Шарик")
print(my_dog.speak()) # Доступ к имени из родительского класса