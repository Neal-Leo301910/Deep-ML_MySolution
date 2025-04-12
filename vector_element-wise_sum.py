'''
Write a Python function that computes the element-wise sum of two vectors. 
The function should return a new vector representing the resulting sum if the operation is valid, 
or -1 if the vectors have incompatible dimensions. Two vectors (lists) can be summed element-wise only if they are of the same length.
'''

import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	

    if len(a) != len(b):
        return -1
    else:
        vec_sum = np.array(a) + np.array(b)
        
        return vec_sum.tolist()
        
print(vector_sum([1, 2, 3], [4, 5, 6]))

print(vector_sum([1, 2], [1, 2, 3]))

print(vector_sum([1.5, 2.5, 3.0], [2, 1, 4]))
