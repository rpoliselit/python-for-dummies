"""
3 - Special meanings to name of variables or functions.
The PEP8 introduces the foue meaning cases.

__double_leading_underscore

Real private method.

*From the Python docs:

Any identifier of the form __spam (at least two leading
underscores, at most one trailing underscore) is textually
replaced with _classname__spam, where classname is the
current class name with leading underscore stripped. This
mangling is done without regard to the syntactic position
of the identifier, so it can be used to define class-private
instance and class variables, methods, variables stored
in globals, and even variables stored in instances private
to this class on instances of other classes.

*And a warning from the same page:

Name mangling is intended to give classes an easy way to
define "private" instance variables and methods, without
having to worry about instance variables defined by derived
classes, or mucking with instance variables by code outside
the class. Note that the mangling roles are designed to
avoid accidents; it still is possible for a determined soul
to access or modify a variable that is considered private.
"""

class MyClass:
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = "world!"

mc = MyClass()

print(mc.__dict__)
print(mc._semiprivate)
print(mc._MyClass__superprivate)
print(mc.__superprivate)
