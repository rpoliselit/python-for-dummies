"""
3 - Special meanings to name of variables or functions.
The PEP8 introduces the four meaning cases.

_single_leading_underscore

This is used to declare private values, function,
methods, and classes in a module; i.e. everything
with this convention is ignored when it is imported
following such structure: from module_name import *.
"""

_internal_vesion = '1.0' # private variable

def _hello_world(): # private function
    print("Hello world!")

class _my_class: # private class
    
    _hidden_factor = 2 # private variable

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _add_values(self): # private method
        return self.x + self.y

    def get_double(self):
        _hello_world()
        return self._hidden_factor * self._add_values()
        
def main():
    object = _my_class(1,1)
    return object.get_double()
