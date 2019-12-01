"""
3 - Special meanings to name of variables or functions.
The PEP8 introduces the foue meaning cases.

__double_leading_and_trailing_underscore__

This is a convention for special variables and/or methods,
so-called MAGIC METHODS, such as: __init__, __str__, __repr__,
__name__, and so on. These methods provide special syntactic
features. For instance, __file__ indicates the location of
Python file.
"""

class my_class:
    def __init__(self, a): # special method to inicializing
        self.a = a

mc = my_class(10)
print(mc.__dict__)
print(__name__)
print(__file__)
