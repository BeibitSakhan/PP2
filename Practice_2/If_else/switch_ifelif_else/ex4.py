number = 15

match number:
    case n if n < 0:
        print("Negative")
    case n if n > 0:
        print("Positive")
    case _:
        print("Zero")