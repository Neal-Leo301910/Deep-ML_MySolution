'''
P = C^{-1} * B
inverse matric = adj{C} / det{C}, 使用Numpy的linalg.inv() function可直接求解

'''
import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	
    #C_inverse = np.linalg.inv(C)
    #P = np.dot(C_inverse,B)
    return np.dot(np.linalg.inv(C),B)
