def build_car(brand, model, **features):
    print(f"Машина: {brand} {model}")
    for key, value in features.items():
        print(f"- {key}: {value}")

# Передаем основные данные и любые дополнительные через ключевые слова
build_car("Tesla", "Model S", color="red", autopilot=True, wheels="sport")