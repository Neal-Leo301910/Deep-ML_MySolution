import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""

    diff = y_true - y_pred
	FP = np.count_nonzero(diff == -1)
    FN = np.count_nonzero(diff == 1)
    TP = np.sum(y_pred) - FP

    P = TP / np.sum(y_pred) 
    R = TP / (TP + FN)

    return round((1+beta ** 2) * (P * R / (beta ** 2 * P + R)),3)

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 0, 0, 1]) 
beta = 1 
print(f_score(y_true, y_pred, beta))

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([1, 0, 0, 0, 0, 1]) 
beta = 1 
print(f_score(y_true, y_pred, beta))

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([1, 0, 1, 1, 0, 0]) 
beta = 2 
print(f_score(y_true, y_pred, beta))

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([0, 0, 0, 1, 0, 1]) 
beta = 2 
print(f_score(y_true, y_pred, beta))
