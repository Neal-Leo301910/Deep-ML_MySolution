'''
Dice Score = F1 Score
'''
import numpy as np

def dice_score(y_true, y_pred):
	diff = np.array(y_true) - np.array(y_pred)
    FP = np.count_nonzero(diff == -1)
    FN = np.count_nonzero(diff == 1)
    TP = np.sum(y_pred) - FP

    if (TP + FN) != 0: 
        res = float(2*TP / (2*TP+FP+FN))
    else:
        res = 0.0

    return round(res, 3)

y_true = np.array([1, 1, 0, 0]) 
y_pred = np.array([1, 1, 0, 0]) 
print(dice_score(y_true, y_pred))

y_true = np.array([1, 1, 0, 0]) 
y_pred = np.array([0, 0, 1, 1]) 
print(dice_score(y_true, y_pred))

y_true = np.array([1, 1, 0, 0]) 
y_pred = np.array([1, 0, 0, 0]) 
print(dice_score(y_true, y_pred))

y_true = np.array([0, 0, 0, 0]) 
y_pred = np.array([0, 0, 0, 0]) 
print(dice_score(y_true, y_pred))

y_true = np.array([1, 1, 1, 1]) 
y_pred = np.array([1, 1, 1, 1]) 
print(dice_score(y_true, y_pred))
