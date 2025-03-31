'''write a Python function that transforms a given matrix A using the operation T^-1AS, where T and S are invertible matrices. 
The function should first validate if the matrices T and S are invertible, and then perform the transformation. 
In cases where there is no solution return -1
'''

import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    '''
    如果T和S的行列式为0，则矩阵不可逆
    '''
    	
    A_arr = np.array(A)
    T_arr = np.array(T)
    S_arr = np.array(S)

    det_T = np.linalg.det(T_arr)
    det_S = np.linalg.det(S_arr)
    if det_T == 0 or det_S == 0:
        transformed_matrix = -1
    else:
        inver_T = np.linalg.inv(T_arr)
        # dot返回的是矩阵内积 *返回的是矩阵对应index相乘
        transformed_matrix_arr = np.dot(np.dot(inver_T,A_arr),S_arr)
        transformed_matrix = transformed_matrix_arr.tolist()
    
    return transformed_matrix


print(transform_matrix([[1, 2], [3, 4]], [[2, 0], [0, 2]], [[1, 1], [0, 1]]))

print(transform_matrix([[2, 3], [1, 4]], [[3, 0], [0, 3]], [[1, 1], [1, 1]]))
