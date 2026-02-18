class Validator:
    @staticmethod
    def is_valid_password(password):
        # Просто логика: пароль должен быть длиннее 6 символов
        return len(password) > 6

# Использование (не нужно создавать объект класса)
print(Validator.is_valid_password("123"))      # False
print(Validator.is_valid_password("password123")) # True