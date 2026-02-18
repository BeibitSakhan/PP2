class Device:
    def power_on(self):
        print("Питание включено")

class Computer(Device):
    def boot(self):
        print("Загрузка системы...")

class Laptop(Computer):
    def fold(self):
        print("Ноутбук сложен")

# Laptop имеет доступ к методам всех классов выше по цепочке
macbook = Laptop()
macbook.power_on() # Из Device
macbook.boot()     # Из Computer
macbook.fold()     # Свой собственныйs