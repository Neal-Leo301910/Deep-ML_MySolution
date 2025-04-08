import numpy as np
def precision(y_true, y_pred):
	
    diff = y_true - y_pred
    
    FP = np.count_nonzero(diff == -1)
    TP = np.sum(y_pred) - FP
    
    return TP / np.sum(y_pred)

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 0, 0, 1]) 
result = precision(y_true, y_pred) print(result)

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([1, 0, 0, 0, 0, 1]) 
result = precision(y_true, y_pred) print(result)
