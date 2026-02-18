class CustomList(list):
    def append(self, item):
        print(f"Добавляем элемент: {item}")
        # Вызываем стандартный метод append из встроенного класса list
        super().append(item)

my_list = CustomList()
my_list.append(10) # Выведет текст и добавит число в список