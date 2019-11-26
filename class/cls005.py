# Python 3.5+
# Type hinting for cls_002.py

class Book:
    TYPES = ('paperback','hardcover')

    def __init__(self, title: str, cover_type: str, paper_weight: int):
        self.title = title
        self.cover_type = cover_type
        self.paper_weight = paper_weight

    def __repr__(self) -> str:
        return f"< Book {self.title}, {self.cover_type}, weighting {self.paper_weight}g >"

    @classmethod
    def paperback(cls, title: str, paper_weight: int) -> "Book":
        return cls(title, cls.TYPES[0], paper_weight)

    @classmethod
    def hardcover(cls, title: str, paper_weight: int) -> "Book":
        return cls(title, cls.TYPES[1], paper_weight + 100)
