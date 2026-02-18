class Base:
    def show(self):
        print("Метод из Base")

class A(Base):
    def show(self):
        print("Метод из A")

class B(Base):
    def show(self):
        print("Метод из B")

class C(A, B): # Наследуем от A и B
    pass

obj = C()
obj.show() # Выведет "Метод из A", так как A стоит первым в списке наследования
print(C.mro()) # Показывает порядок поиска: C -> A -> B -> Base