'''
Implement the prediction function for binary classification using Logistic Regression. 
Your task is to compute class probabilities using the sigmoid function and return binary predictions based on a threshold of 0.5.

z = w^T x + b

y = 1 / (1 + e^{-(wx+b)})

y >(=) threshold -> 1
y <(=) threshold -> 0

'''

import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	w = weights
    b = bias
    
    
    z = X.dot(w) + b
    z = np.clip(z,-500,500)
    
    prob = 1 / (1 + np.exp(-z))
    
    y = (prob >= 0.5).astype(int)
    
    return y

print(predict_logistic(np.array([[1, 1], [2, 2], [-1, -1], [-2, -2]]), np.array([1, 1]), 0))

print(predict_logistic(np.array([[0, 0], [0.1, 0.1], [-0.1, -0.1]]), np.array([1, 1]), 0))

print(predict_logistic(np.array([[1, 2, 3], [-1, -2, -3], [0.5, 1, 1.5]]), np.array([0.1, 0.2, 0.3]), -1))

print(predict_logistic(np.array([[1], [2], [-1], [-2]]), np.array([2]), 0))

print(predict_logistic(np.array([[1000, 2000], [-1000, -2000]]), np.array([0.1, 0.1]), 0))
