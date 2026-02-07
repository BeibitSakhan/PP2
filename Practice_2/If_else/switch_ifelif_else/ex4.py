point = (0, 5)

match point:
    case (0, 0):
        print("At the origin")
    case (0, y):
        print(f"On the Y-axis at {y}")
    case (x, 0):
        print(f"On the X-axis at {x}")
    case _:
        print("Somewhere else")