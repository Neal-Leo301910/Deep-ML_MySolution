Write a Python function that performs linear regression using gradient descent. 
The function should take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, 
along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array. 
Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.
'''

import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros(n)

    coeff = alpha / m
    
    for _ in range(iterations):
        
        gradient = np.zeros(n)
        for i in range(m):
            pred = X[i].dot(theta)
            error = pred - y[i]
            for j in range(n):
                gradient[j] += error * X[i,j]
        theta -= coeff * gradient

    return np.round(theta,4)  

