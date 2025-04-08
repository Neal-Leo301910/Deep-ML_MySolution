import numpy as np
def recall(y_true, y_pred):
    
    diff = y_true - y_pred
    
    FP = np.count_nonzero(diff == -1)
    FN = np.count_nonzero(diff == 1)
    TP = np.sum(y_pred) - FP
    
    return round(TP / (TP + FN),3)

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([1, 0, 0, 0, 0, 1]) 
print(recall(y_true, y_pred))

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 0, 0, 1]) 
print(recall(y_true, y_pred))

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([1, 0, 1, 1, 0, 0]) 
print(recall(y_true, y_pred))

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([0, 0, 0, 1, 0, 1]) 
print(recall(y_true, y_pred))

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([0, 1, 0, 0, 1, 0]) 
print(recall(y_true, y_pred))
