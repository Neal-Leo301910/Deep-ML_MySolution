'''
Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. 
The function should have an optional seed parameter for reproducibility.
'''
import numpy as np

def shuffle_data(X, y, seed=None):
    
    if seed:
        np.random.seed(seed)
    
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    
    X_shuffled = X[idx]
    y_shuffled = y[idx]
    
    return X_shuffled, y_shuffled


print(shuffle_data(np.array([[1, 2], [3, 4], [5, 6], [7, 8]]), np.array([1, 2, 3, 4]), seed=42))
print(shuffle_data(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), np.array([10, 20, 30, 40]), seed=24))
