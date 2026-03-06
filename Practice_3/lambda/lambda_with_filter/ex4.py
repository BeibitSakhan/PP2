raw_data = ["sensor_1", "", "sensor_2", None, "sensor_3", "  "]

# Оставляем только те элементы, которые не пустые и не None
# .strip() убирает лишние пробелы
clean_data = list(filter(lambda x: x and str(x).strip(), raw_data))

print(clean_data)  # ['sensor_1', 'sensor_2', 'sensor_3']s