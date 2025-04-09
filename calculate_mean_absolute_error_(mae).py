'''
MAE = 1/n sum_(i=1)^n |y_true_i - y_pred_i|
'''

import numpy as np

def mae(y_true, y_pred):
	"""
	Calculate Mean Absolute Error between two arrays.

	Parameters:
	y_true (numpy.ndarray): Array of true values
  y_pred (numpy.ndarray): Array of predicted values

	Returns:
	float: Mean Absolute Error rounded to 3 decimal places
	"""
	
    MAE = np.mean(np.abs(y_true - y_pred))

	return round(MAE,3)


print(mae(np.array([3, -0.5, 2, 7]), np.array([2.5, 0.0, 2, 8])))
print(mae(np.array([[0.5, 1], [-1, 1], [7, -6]]), np.array([[0, 2], [-1, 2], [8, -5]])))
print(mae(np.array([-1, -2, -3]), np.array([-1.5, -2.2, -2.8])))
print(mae(np.array([1, -1, 0]), np.array([-1, 1, 0])))
