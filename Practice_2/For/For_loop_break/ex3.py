data = [10, 20, 0, 40]
for num in data:
    if num == 0:
        print("Error: Zero detected. Stopping.")
        break
    print(100 / num)