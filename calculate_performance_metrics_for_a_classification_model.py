import numpy as np

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	
	
    diff = np.array(actual) - np.array(predicted)
    

    FP = int(np.count_nonzero(diff == -1))
    FN = int(np.count_nonzero(diff == 1))
    TP = int(np.sum(predicted)) - FP
    TN = len(predicted) - FP - FN - TP

    confusion_matrix = [[TP, FN],[FP, TN]]

    accuracy = (TP + TN) / (TP + TN + FP + FN)

    P = TP / (TP + FP)

    negativePredictive = TN / (TN + FN)

    R = TP / (TP + FN)

    specificity = TN / (TN+FP)

    f1 = 2 * P * R / (P + R)

    
    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

actual = [1, 0, 1, 0, 1] 
predicted = [1, 0, 0, 1, 1] 
print(performance_metrics(actual, predicted))

actual = [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1] 
predicted = [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0] 
print(performance_metrics(actual, predicted))

actual = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0] 
predicted = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1] 
print(performance_metrics(actual, predicted))
