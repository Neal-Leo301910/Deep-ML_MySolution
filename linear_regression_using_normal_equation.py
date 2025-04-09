'''
y = W^T X + b 

a scalar dependent variable ( y ) and one or more independent variables ( X ). find the coefficient theta
Normal Equations: theta = (X.T X).-1 X.T y
'''

import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	
    X = np.array(X)
    X_transpose = X.T
    y = np.array(y).reshape(-1,1)

    theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)

	return np.round(theta).flatten().tolist()

print(linear_regression_normal_equation([[1, 1], [1, 2], [1, 3]], [1, 2, 3]))

print(linear_regression_normal_equation([[1, 3, 4], [1, 2, 5], [1, 3, 2]], [1, 2, 1]))
