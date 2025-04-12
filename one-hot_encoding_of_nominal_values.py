'''
Write a Python function to perform one-hot encoding of nominal values. 
The function should take in a 1D numpy array x of integer values and an optional integer n_col representing the number of columns for the one-hot encoded array. 
If n_col is not provided, it should be automatically determined from the input array.
'''


import numpy as np

def to_categorical(x, n_col=None):
    one_hot_code = []

    for val in x:
        data = [0] * (max(x) + 1)
        data[val] = 1
        one_hot_code.append(data)
    
    return one_hot_code

print(to_categorical(np.array([0, 1, 2, 1, 0])))
print(to_categorical(np.array([3, 1, 2, 1, 3]), 4))

