class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        print(f"User: {self.username} | Email: {self.email}")

user1 = User("Coder99", "hello@python.com")
user1.display()