class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def complete(self):
        self.is_done = True

# Usage
todo = Task("Buy groceries")
todo.complete()
print(f"{todo.description} done? {todo.is_done}")