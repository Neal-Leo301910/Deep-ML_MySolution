'''
Write a Python function to calculate the correlation matrix for a given dataset. 
The function should take in a 2D numpy array X and an optional 2D numpy array Y. 
If Y is not provided, the function should calculate the correlation matrix of X with itself. 
It should return the correlation matrix as a 2D numpy array.

corr(X,Y) = cov(X,Y) / [ std(X) * std(Y) ]
'''

import numpy as np

def calculate_correlation_matrix(X, Y=None):
	
    if Y is None:
        Y = X

    std_X = np.std(X, axis=0, ddof=1) #计算每一列的标准差
    std_Y = np.std(Y, axis=0, ddof=1)

    ‘’‘
    cov(X,Y) = E( [X - E[X]] [Y - E[Y]] )
             = (1/(n-1)) sum [ (X_i-E[X])(Y_i-E[Y]) ]
    '''

    X_centered = X - np.mean(X, axis=0) # [X - E[X]] 
    Y_centered = Y - np.mean(Y, axis=0) # [Y - E[Y]]

    covariance_matrix = (X_centered.T @ Y_centered) / (X_centered.shape[0] - 1)

    return  covariance_matrix / np.outer(std_X, std_Y)

X = np.array([[1, 2], [3, 4], [5, 6]])

output = calculate_correlation_matrix(X=X)
print(output)
