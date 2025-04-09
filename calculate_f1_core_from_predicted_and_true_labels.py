import numpy as np
def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
    diff = np.array(y_true) - np.array(y_pred)
    FP = np.count_nonzero(diff == -1)
    FN = np.count_nonzero(diff == 1)
    TP = np.sum(y_pred) - FP

    P = TP / (TP + FP)
    if (TP + FN) != 0: 
        R = TP / (TP + FN)
        f1 = float(2 * P * R / (P + R))
    else:
        f1 = 0.0

    
    return round(f1,3)
