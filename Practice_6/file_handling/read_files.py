# 1
with open("README.md", "r") as f:
    print(f.read())

# 2
with open("README.md", "r") as f:
    for line in f:
        print(f"Line: {line.strip()}")

# 3
with open("README.md", "r") as f:
    lines = f.readlines()

# 4
with open("README.md", "r") as f:
    matches = [line for line in f if "theme" in line.lower()]

# 5
with open("README.md", "r") as f:
    print(f.read(10))