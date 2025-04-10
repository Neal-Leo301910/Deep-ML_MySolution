'''
R-squared, also known as the coefficient of determination, 
is a measure that indicates how well the independent variables explain the variability of the dependent variable in a regression model.
Your Task: To implement the function r_squared(y_true, y_pred) that calculates the R-squared value, given arrays of true values y_true and predicted values y_pred.

R^2 = 1 - SSR / SST

SSR = sum(y_true - y_pred)^2
SST = sum(y_true - y_mean)^2

'''

import numpy as np

def r_squared(y_true, y_pred):
	
    
    ssr = sum((y_true - y_pred) ** 2)
    sst = sum((y_true - np.mean(y_true)) ** 2)

    return float(1 - ssr / sst)

y_true = np.array([1, 2, 3, 4, 5]) 
y_pred = np.array([1, 2, 3, 4, 5]) 
print(r_squared(y_true, y_pred))

y_true = np.array([1, 2, 3, 4, 5]) 
y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8]) 
print(r_squared(y_true, y_pred))

y_true = np.array([1, 2, 3, 4, 5]) 
y_pred = np.array([2, 1, 4, 3, 5]) 
print(r_squared(y_true, y_pred))

y_true = np.array([1, 2, 3, 4, 5]) 
y_pred = np.array([3, 3, 3, 3, 3]) 
print(r_squared(y_true, y_pred))

y_true = np.array([1, 2, 3, 4, 5]) 
y_pred = np.array([5, 4, 3, 2, 1]) 
print(r_squared(y_true, y_pred))
