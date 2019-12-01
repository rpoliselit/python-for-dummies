"""
3 - Special meanings to name of variables or functions.
The PEP8 instroduces the four meaning cases.

single_trailing_underscore_

This convention is used to avoid conflicts with Python
key words or build-ins.

Good habits: Do not use it often. Choose other words.
"""

class Hero:

    def __init__(self, name, gender, race='elf', class_):
        self.name = name
        self.gender = gender
        self.race = race
        self.class_ = class_ # Avoiding conflict with class.
