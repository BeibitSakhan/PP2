class Flyer:
    def fly(self):
        print("Я лечу!")

class Swimmer:
    def swim(self):
        print("Я плыву!")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Кря-кря!")

# Утка умеет всё сразу
donald = Duck()
donald.fly()
donald.swim()