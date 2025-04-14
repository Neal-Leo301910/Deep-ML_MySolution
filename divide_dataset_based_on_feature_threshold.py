'''
Write a Python function to divide a dataset based on whether the value of a specified feature is greater than or equal to a given threshold. 
The function should return two subsets of the dataset: one with samples that meet the condition and another with samples that do not.


'''

import numpy as np

def divide_on_feature(X, feature_i, threshold):

    samples = X[:,feature_i]

    idx_1st = np.where(samples >= threshold)
    idx_2nd = np.where(samples < threshold)
    
    first_subset = X[idx_1st]
    second_subset = X[idx_2nd]

    return first_subset,second_subset


print(divide_on_feature(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 0, 5))

print(divide_on_feature(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), 1, 3))
