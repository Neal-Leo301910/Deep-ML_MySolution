'''
Write a Python function that reshapes a given matrix into a specified shape. 
if it cant be reshaped return back an empty list [ ]
'''

import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
#Write your code here and return a python list after reshaping by using numpy's tolist() method
     if np.array(a).size != np.prod(new_shape):
        return []
    else:
        return np.array(a).reshape(new_shape).tolist()


print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (4, 2)))
print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 4)))
print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 4)))
print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (2, 4)))
