class Payment:
    def process(self, amount):
        print(f"Обработка базового платежа на сумму {amount}")

class PayPalPayment(Payment):
    def process(self, amount):
        print(f"Вход в систему PayPal... Оплата {amount} выполнена.")

class CardPayment(Payment):
    def process(self, amount):
        print(f"Проверка CVV... Снятие {amount} с банковской карты.")

# Система просто вызывает .process(), не зная, какой именно это платеж
def checkout(payment_method, amount):
    payment_method.process(amount)

checkout(PayPalPayment(), 500)