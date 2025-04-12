'''
Write a Python function ridge_loss that implements the Ridge Regression loss function. 
The function should take a 2D numpy array X representing the feature matrix, 
a 1D numpy array w representing the coefficients, a 1D numpy array y_true representing the true labels, 
and a float alpha representing the regularization parameter. 
The function should return the Ridge loss, which combines the Mean Squared Error (MSE) and a regularization term.

L(w) = 1/n sum{i=(1,n)}(yi_true - yi_pred)^2 + alpha * sum{j=(1,p)}w^2

'''

import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    y_pred = X.dot(w)
    error = y_pred - y_true
    mse = np.mean(error ** 2)
    pen = alpha * sum(w ** 2)
    
    return mse + pen

X = np.array([[1,1],[2,1],[3,1],[4,1]]) 
W = np.array([.2,2]) 
y = np.array([2,3,4,5]) 
alpha = 0.1 
output = ridge_loss(X, W, y, alpha) 
print(output)

X = np.array([[1,1,4],[2,1,2],[3,1,.1],[4,1,1.2],[1,2,3]])
W = np.array([.2,2,5]) 
y = np.array([2,3,4,5,2]) 
alpha = 0.1 
output = ridge_loss(X, W, y, alpha) 
print(output)
