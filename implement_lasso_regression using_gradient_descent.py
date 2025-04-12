'''
In this problem, you need to implement the Lasso Regression algorithm using Gradient Descent. 
Lasso Regression (L1 Regularization) adds a penalty equal to the absolute value of the coefficients to the loss function. 
Your task is to update the weights and bias iteratively using the gradient of the loss function and the L1 penalty.

The objective function of Lasso Regression is:
J(w,b) = 1/2n sum{i=(1,n)}(yi - (sum{j=(1,p)Xijwj+b}()))^2 + alpha * sum{j=(1,p)|wj|}
'''

import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
	n_samples, n_features = X.shape

	weights = np.zeros(n_features)
	bias = 0
	
    for _ in range(max_iter):
        y_pred = X.dot(weights) + bias
        error = y_pred - y
        grad_w = 1/n_samples * X.T.dot(error) + alpha * np.sign(weights)
        grad_b = 1/n_samples * np.sum(error)

        weights -=  learning_rate * grad_w
        bias -= learning_rate * grad_b

        epsilon = np.linalg.norm(grad_w,ord=1)

        if epsilon < tol:
            break

    return weights, bias

X = np.array([[0, 0], [1, 1], [2, 2]]) 
y = np.array([0, 1, 2]) 
alpha = 0.1 
output = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000) 
print(output)

X = np.array([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) 
y = np.array([1, 2, 3, 4, 5]) 
alpha = 0.1 
output = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000) 
print(output)
