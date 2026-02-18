class Storage:
    def save(self, data):
        print(f"Данные '{data}' сохранены в БД.")

class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class SecureData(Storage, Logger):
    def update_data(self, new_data):
        self.save(new_data)
        self.log(f"Данные изменены на {new_data}")

# Теперь сохранение всегда сопровождается записью в лог
data_manager = SecureData()
data_manager.update_data("Секретный пароль")