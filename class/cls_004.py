# Class composition
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

    def list_of_books(self):
        print("The books on shelf are:")
        for num, book in enumerate(self.books):
            print(f"{num + 1}º {book.__repr__()}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"

    def __str__(self):
        return f"Book entitled {self.title} by {self.author}."

book_1 = Book("Statistical Mechanics", "R. Feynman")
book_2 = Book("The Case of Charles Dexter Ward", "H.P. Lovecraft")

shelf = BookShelf(book_1, book_2)

print(f"\n{book_1}\n\n{book_2}\n\n{shelf}\n\n{shelf.books}\n")

shelf.list_of_books()
