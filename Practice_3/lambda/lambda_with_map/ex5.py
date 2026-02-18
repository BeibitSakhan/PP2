prices = [100, 250, 500, 1000]

# Добавляем 10% налога к каждой цене
prices_with_tax = list(map(lambda p: p * 1.1, prices))

# Округлим результат для красоты
print(list(map(lambda p: round(p, 2), prices_with_tax))) 
# [110.0, 275.0, 550.0, 1100.0]