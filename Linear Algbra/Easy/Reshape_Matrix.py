'''Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list [ ]'''



import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    if np.array(a).size != np.prod(new_shape):
        return []
    else:
        return np.reshape(a, newshape=new_shape).tolist()

