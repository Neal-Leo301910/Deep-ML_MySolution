‘’‘
Write a Python function that calculates the inverse of a 2x2 matrix. Return 'None' if the matrix is not invertible.
inverse(A) = 1 / det(A) * adjugate(A)
det(A) = ad - bc
adjugate(A) = [[d,a],[-c,-b]]
’‘’

import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:


    matrix_arr = np.array(matrix)
    #inverse = np.linalg.inv(matrix_arr)
    
    diag_product = matrix_arr[0][0] * matrix_arr[1][1]
    anti_diag_product = matrix_arr[0][1] * matrix_arr[1][0]


    if diag_product - anti_diag_product == 0:
        inverse = 'None'
    else:
        inver_det = 1 / (diag_product - anti_diag_product)
        adjugate = np.array([
            [matrix_arr[1][1], -matrix_arr[0][1]],
            [-matrix_arr[1][0], matrix_arr[0][0]]
        ])
        inverse = np.dot(inver_det, adjugate)

    return inverse


