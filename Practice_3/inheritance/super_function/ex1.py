class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, language):
        # Вызываем конструктор родителя для name и salary
        super().__init__(name, salary)
        self.language = language

dev = Developer("Макс", 100000, "Python")
print(f"{dev.name} пишет на {dev.language}")