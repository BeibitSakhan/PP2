entries = ["Valid", "Valid", "INVALID", "Valid"]
for status in entries:
    if status == "INVALID":
        print("System halt: Invalid entry found.")
        break
    print("Processing...")