data = 10.5

match data:
    case int():
        print("This is a whole number.")
    case float():
        print("This is a decimal.")
    case str():
        print("This is text.")
    case _:
        print("Other type.")