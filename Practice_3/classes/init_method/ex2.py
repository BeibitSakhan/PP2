class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

# Здесь баланс будет 500
acc1 = Account("Ivan", 500)
# А здесь баланс будет 0 (по умолчанию)
acc2 = Account("Elena")