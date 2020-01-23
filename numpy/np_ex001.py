"""
About arrays.
"""
import numpy as np

a = np.arange(24).reshape(4,3,2)
print(a)
print(a.ndim) # the number of dimensions of the array
print(a.dtype.name) # the type of elements of the array
print(type(a))
print(a.shape) # the sizes of the array
print(a.size) # the total number of elements
print(a.itemsize) # the size in bites of each element
print(a.data) # memory address