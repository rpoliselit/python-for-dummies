# Custom errors in classes.

class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.title}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages):
        if self.pages_read + pages > self.page_count:
            msg = f"You tried to read {self.pages_read + pages} but this book only has {self.page_count} pages."
            raise TooManyPagesReadError(msg)
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


book_1 = Book("Fluent Python", 800)
try:
    book_1.read(450)
    book_1.read(800)
except TooManyPagesReadError as e:
    print(e)
finally:
    print(book_1)
