class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"'{self.title}' by {self.author}"

# Usage
my_book = Book("The Hobbit", "J.R.R. Tolkien")
print(my_book.get_info())