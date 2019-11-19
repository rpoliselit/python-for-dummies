class Book:
    TYPES = ('paperback','hardcover')

    def __init__(self, title, cover_type, paper_weight):
        self.title = title
        self.cover_type = cover_type
        self.paper_weight = paper_weight

    def __repr__(self):
        return f"< Book {self.title}, {self.cover_type}, weighting {self.paper_weight}g >"

    @classmethod
    def paperback(cls, title, paper_weight):
        return cls(title, cls.TYPES[0], paper_weight)

    @classmethod
    def hardcover(cls, title, paper_weight):
        return cls(title, cls.TYPES[1], paper_weight + 100)


book_1 = Book('Atomic and Nuclear Physics', 'hardcover', 1600)

book_2 = Book.paperback('Quantum electrodynamics', 670)

book_3 = Book.hardcover('Mathematical Methods in the Physical Science', 1390)

print(f'{book_1}\n{book_2}\n{book_3}')
