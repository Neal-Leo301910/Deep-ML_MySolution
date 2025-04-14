'''
Write a Python function to generate polynomial features for a given dataset. 
The function should take in a 2D numpy array X and an integer degree, 
and return a new 2D numpy array with polynomial features up to the specified degree.

degree = 2, features = 2: [0, x1, x2, x1^2, x1x2, x2^2] -> [ (), (0), (1), (0,0), (0,1), (1,1)]
degree = 3, features = 2: [0, x1, x2, x1^2, x1x2, x2^2, x1^3, x1^2*x1, x1*x2^2, x2^3] -> [(), (0,), (1,), (0, 0), (0, 1), (1, 1), (0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)]
degree = 3, features = 3: [0, x1, x2, x3, x1^2, x1x2, x1x3, x2^2, x2x3 x3^2 x1^3, x1^2*x1, x1^2x3, x1x2^2, x1x3^3, x1x2^2, x1x2x3, x1*x3^2, x2^3, x2^2x3, x2x3^2, x3^3] ->
                          [(), (0,), (1,), (2,), (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]

'''
import numpy as np
from itertools import combinations_with_replacement


def polynomial_features(X, degree):
    
    n_samples, n_features = X.shape
    
    
    combs = [combinations_with_replacement(range(n_features),i) for i in range(0,degree+1) ]

    flat_combs = [item for sublist in combs for item in sublist]
    
    n_output_features = len(flat_combs)
    X_new = np.empty((n_samples,n_output_features))
    
    for i,idx_comb in enumerate(flat_combs):
        X_new[:,i] = np.prod(X[:,idx_comb],axis=1)
        
    return X_new
    
    
    
print(polynomial_features(np.array([[2, 3], [3, 4], [5, 6]]), 2))
print(polynomial_features(np.array([[1, 2], [3, 4], [5, 6]]), 3))
print(polynomial_features(np.array([[1, 2, 3], [3, 4, 5], [5, 6, 9]]), 3))
    
    
