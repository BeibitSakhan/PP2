class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        return self.salary * 0.1  # Стандартный бонус 10%

class Manager(Employee):
    def get_bonus(self): # Переопределение
        return self.salary * 0.2  # У менеджеров бонус 20%

# Менеджер получит больше, хотя метод называется так же
m = Manager("Иван", 100000)
print(m.get_bonus()) # 20000