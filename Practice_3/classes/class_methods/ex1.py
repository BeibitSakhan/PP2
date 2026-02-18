class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        # Допустим, строка приходит в формате "Иван-25"
        name, age = data_str.split("-")
        return cls(name, int(age)) # Создает и возвращает новый объект

# Использование
user = User.from_string("Алексей-30")
print(user.name) # Алексей1