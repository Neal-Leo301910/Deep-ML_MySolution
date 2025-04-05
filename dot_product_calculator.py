'''Write a Python function to calculate the dot product of two vectors. The function should take two 1D NumPy arrays as input and return the dot product as a single number.'''

import numpy as np

def calculate_dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        float: Dot product of the two vectors.
    """
    return np.dot(vec1, vec2)

print(calculate_dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])))

print(calculate_dot_product(np.array([-1, 2, 3]), np.array([4, -5, 6])))

print(calculate_dot_product(np.array([1, 0]), np.array([0, 1])))

print(calculate_dot_product(np.array([0, 0, 0]), np.array([0, 0, 0])))

print(calculate_dot_product(np.array([7]), np.array([3])))
