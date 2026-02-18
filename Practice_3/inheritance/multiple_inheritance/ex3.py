class Employee:
    def get_salary(self):
        print("Получение зарплаты")

class Customer:
    def get_discount(self):
        print("Применение скидки клиента")

class StaffCustomer(Employee, Customer):
    pass

# Объект имеет доступ к методам обоих классов
user = StaffCustomer()
user.get_salary()
user.get_discount()