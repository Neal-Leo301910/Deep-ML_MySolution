'''
Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. 
The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. 
It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. 
Make sure all results are rounded to the nearest 4th decimal.

standardized_data = (x - miu) / sigma
normalized_data = (x-min(x)) / (max(x) - min(x)) * (max - min) + min
'''

import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
    means = np.mean(data,axis=0)
    stds = np.std(data,axis=0)
    standardized_data = (data - means) / stds
    
    max_vals = np.max(data,axis=0)
    min_vals = np.min(data,axis=0)
    normalized_data = (data - min_vals) / (max_vals - min_vals) 
    
    return np.round(standardized_data,4).tolist(), np.round(normalized_data,4).tolist()

print(feature_scaling(np.array([[1, 2], [3, 4], [5, 6]])))
