import os

# 1
os.makedirs("new_logs", exist_ok=True)

# 2
print(os.listdir("."))

# 3
files = [f for f in os.listdir(".") if os.path.isfile(f)]

# 4
print(f"I am currently in: {os.getcwd()}")

# 5
print(os.path.isdir("new_logs"))