user_role = "editor"
if user_role == "admin":
    print("Full access granted.")
elif user_role == "editor":
    print("Can edit content.")
elif user_role == "guest":
    print("Read-only access.")
else:
    print("Access denied.")