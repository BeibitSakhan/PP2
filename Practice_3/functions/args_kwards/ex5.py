def create_point(x, y, z):
    print(f"Координаты: x={x}, y={y}, z={z}")

coords = [10, 20, 30]
data = {"x": 1, "y": 2, "z": 3}

create_point(*coords) # Распаковка списка
create_point(**data)   # Распаковка словаря