"""
Basic of linear algebra.
"""
import numpy as np

a = np.array([[1.,2.],[3.,4.]])
print(a)
print(np.transpose(a))
print(np.linalg.det(a.transpose()))
print(np.linalg.inv(a))
print(np.trace(a))
print(np.eye(3)) # identity matrix
y = np.array([[3.],[7.]])
print(np.linalg.solve(a,y)) # solve x+2y==3 && 3x+4y==7
print(np.linalg.eig(a)) # find the eigenvalues and their respectives eigenvectors