'''
RMSE = (1/n sum_(i=1)^n (y_true - y_pred)^2)^0.5
'''
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	
    diff = y_true - y_pred
    rmse_res = np.mean(diff*diff) ** 0.5
    
    return round(rmse_res,3)


y_true1 = np.array([3, -0.5, 2, 7]) 
y_pred1 = np.array([2.5, 0.0, 2, 8]) 
print(rmse(y_true1, y_pred1))

y_true2 = np.array([[0.5, 1], [-1, 1], [7, -6]]) 
y_pred2 = np.array([[0, 2], [-1, 2], [8, -5]]) 
print(rmse(y_true2, y_pred2))

y_true3 = np.array([[1, 2], [3, 4]]) 
y_pred3 = np.array([[1, 2], [3, 4]]) 
print(rmse(y_true3, y_pred3))
