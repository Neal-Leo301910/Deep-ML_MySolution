'''
Write a Python function kernel_function that computes the linear kernel between two input vectors x1 and x2. 
The linear kernel is defined as the dot product (inner product) of two vectors.

K(X1,X2) = X1 dot X2
'''

import numpy as np

def kernel_function(x1, x2):

    return x1.dot(x2)


x1 = np.array([1, 2, 3]) 
x2 = np.array([4, 5, 6]) 
result = kernel_function(x1, x2) 
print(result)

x1 = np.array([0, 1, 2]) 
x2 = np.array([3, 4, 5]) 
result = kernel_function(x1, x2) 
print(result)
