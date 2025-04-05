'''
P = C^{-1} * B
Determinant 使用Numpy的linalg.det(matrix)function可直接求解
inverse matric = adj{C} / det{C}, 使用Numpy的linalg.inv() function可直接求解
adjugate matrix Numpy无直接的 function求解，需要从上面两个function中得到答案后求解
'''
import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	
    #C_inverse = np.linalg.inv(C)
    #P = np.dot(C_inverse,B)
    return np.dot(np.linalg.inv(C),B)

print(transform_basis([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 2.3, 3], [4.4, 25, 6], [7.4, 8, 9]]))
print(transform_basis([[1,0],[0,1]],[[1,2],[9,2]]))
