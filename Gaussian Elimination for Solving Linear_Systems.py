'''
Your task is to implement the Gaussian Elimination method, which transforms a system of linear equations into an upper triangular matrix. 
This method can then be used to solve for the variables using backward substitution.

Write a function gaussian_elimination(A, b) that performs Gaussian Elimination with partial pivoting to solve the system (Ax = b).

The function should return the solution vector (x).
'''

import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
    # combination of coefficient matrix A and vector source b
    comb = np.column_stack((A,b))

    row,col = coff.shape

    # Gaussian Elimination
    for k in range(row-1):
        pat_pivot = np.max(np.abs(coff[k:,k]))
        max_idx = k + np.argmax(np.abs(coff[k:,k]))
        coff[[k,max_idx]] = coff[[max_idx,k]]
        for i in range(k+1,row):
            m_ik = coff[i,k] / coff[k,k]
            coff[i] -= coff[k] * m_ik
    
    x = np.zeros_like(b,dtype=float)
    
    # Backwards Substitution
    for m in range(row-1,-1,-1):
        x[m] = (coff[m,col-1] - np.dot(coff[m,:col-1],x)) / coff[m,m]
    
    return x

A = np.array([[2,8,4], [2,5,1], [4,10,-1]], dtype=float) 
b = np.array([2,5,1], dtype=float) 
print(gaussian_elimination(A, b))

A = np.array([ [0, 2, 1, 0, 0, 0, 0], [2, 6, 2, 1, 0, 0, 0], [1, 2, 7, 2, 1, 0, 0], [0, 1, 2, 8, 2, 1, 0], [0, 0, 1, 2, 9, 2, 1], [0, 0, 0, 1, 2, 10, 2], [0, 0, 0, 0, 1, 2, 11] ], dtype=float) 
b = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float) 
print(gaussian_elimination(A, b))

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float) 
b = np.array([8, -11, -3], dtype=float) 
print(gaussian_elimination(A, b))
