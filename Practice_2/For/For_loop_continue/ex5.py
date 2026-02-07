transactions = [100, -20, 50, -5, 80]
for amount in transactions:
    if amount < 0:
        continue
    print("Processing deposit:", amount)