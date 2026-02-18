class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# При создании объекта Python сам вызывает __init__
admin = User("Alice", "Administrator")
print(admin.username) # Alice