class Messenger:
    def send(self, message):
        print(f"Отправка сообщения: {message}")

class SecureMessenger(Messenger):
    def send(self, message):
        print("Шифрование данных...")
        # Вызываем оригинальный метод родителя
        super().send(message)
        print("Сообщение успешно зашифровано и отправлено.")

# Использование
m = SecureMessenger()
m.send("Привет!")