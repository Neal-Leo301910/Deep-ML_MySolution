'''
Write a Python function that calculates the eigenvalues of a 2x2 matrix. 
The function should return a list containing the eigenvalues, sort values from highest to lowest.
eig^2 - eig*trace(matrix) + det(matrix) = 0
trace(matrix) = a+d
det(matrix) = ad - bc
'''


import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    matrix_arr = np.array(matrix)
    #det_matrix = np.linalg.det(matrix_arr)
    #trace_matrix = np.linalg.trace(matrix_arr)
    
    eigenvalues, _ = np.linalg.eig(matrix_arr)

    return eigenvalues


matrix = [[2, 1], [1, 2]]
calculate_eigenvalues(matrix)
