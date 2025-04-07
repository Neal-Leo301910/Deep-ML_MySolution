import numpy as np

def accuracy_score(y_true, y_pred):
	
    diff = np.abs(y_pred - y_true)
    return 1 - np.count_nonzero(diff) / len(y_true)

print(accuracy_score(np.array([1, 0, 1, 1, 0, 1]), np.array([1, 0, 0, 1, 0, 1])))
print(accuracy_score(np.array([1, 1, 1, 1]), np.array([1, 0, 1, 0])))
