"""
Type of arrays.
"""
import numpy as np

print(np.zeros( (2,3) )) # generates array of zeros
print(np.array([ [2j,2], [5,8+1.5j]], dtype=complex)) # array with complex numbers
print(np.ones( (1,4) , dtype=np.int16))
print(np.empty( (2,5) )) # output varies / uninitialized
print(np.arange(0,102.5,2.5))