s = "python"
idx = 0
while idx < len(s):
    char = s[idx]
    idx += 1
    if char == "y":
        continue
    print(char)