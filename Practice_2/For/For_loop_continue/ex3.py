data = ["User1", None, "User3", "User4"]
for user in data:
    if user is None:
        continue
    print("Sending email to:", user)