class Base:
    def action(self):
        print("Действие в Base")

class A(Base):
    def action(self):
        print("Действие в A")
        super().action()

class B(Base):
    def action(self):
        print("Действие в B")
        super().action()

class C(A, B):
    def action(self):
        print("Действие в C")
        super().action()

obj = C()
obj.action() # Вызовет цепочку C -> A -> B -> Base1