class Robot:
    def move(self):
        print("Робот начал движение.")

class CleaningRobot(Robot):
    def move(self):
        super().move() # Сначала выполняем общую логику движения
        print("Включен режим всасывания пыли.")

cleaner = CleaningRobot()
cleaner.move()