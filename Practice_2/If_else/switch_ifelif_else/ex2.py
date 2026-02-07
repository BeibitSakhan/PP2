day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Work day")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Invalid day")