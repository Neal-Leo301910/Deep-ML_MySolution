‘’‘
Write a Python function to convert a 1D numpy array into a diagonal matrix. 
The function should take in a 1D numpy array x and return a 2D numpy array representing the diagonal matrix.
‘’‘

import numpy as np

def make_diagonal(x):

	return np.diag(x)


print(make_diagonal(np.array([1, 2, 3])))
print(make_diagonal(np.array([4, 5, 6, 7])))
