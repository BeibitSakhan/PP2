# 1
with open("test.txt", "w") as f:
    f.write("Hello Python!")

# 2
with open("log.txt", "a") as f:
    f.write("\nNew log entry at 2026-03-18")

# 3
items = ["Apple\n", "Banana\n", "Cherry\n"]
with open("grocery.txt", "w") as f:
    f.writelines(items)

# 4
data = ["Name,Age", "Alice,30", "Bob,25"]
with open("data.csv", "w") as f:
    f.write("\n".join(data))

# 5
with open("output.txt", "w") as f:
    print("Directly printing to a file!", file=f)