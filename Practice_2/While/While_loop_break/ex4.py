attempts = 0
while attempts < 5:
    if input("Password: ") == "secret":
        break
    attempts += 1