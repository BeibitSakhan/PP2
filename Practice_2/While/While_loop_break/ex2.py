n = 1
while n < 100:
    if n % 7 == 0 and n % 3 == 0:
        print("Found magic number:", n)
        break
    n += 1