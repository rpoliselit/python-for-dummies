"""
More basic operations.
"""
import numpy as np

A = np.array( [[2,0],[1,1]] )
B = np.array( [[1,3],[4,5]] )

print(A @ B) # matrix product
print(A.dot(B)) # matrix product
print(A.sum(axis=0)) # sum of each column
print(B.max(axis=1)) # max of each row
print(B.cumsum(axis=1)) # cumulative sum of each row