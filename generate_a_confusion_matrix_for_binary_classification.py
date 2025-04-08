import numpy as np

def confusion_matrix(data):
	
    data = np.array(data)
    
    y_true = data.T[0]
    y_pred = data.T[1]

    
    diff = y_true - y_pred
    

    
    FP = int(np.count_nonzero(diff == -1))
    FN = int(np.count_nonzero(diff == 1))
    TP = int(np.sum(y_pred) - FP)

    TN = len(y_true) - FP - FN - TP
    
    return [[TP,FN],[FP,TN]]

data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]] 
print(confusion_matrix(data))

data = [[0, 1], [1, 0], [1, 1], [0, 1], [0, 0], [1, 0], [0, 1], [1, 1], [0, 0], [1, 0], [1, 1], [0, 0], [1, 0], [0, 1], [1, 1], [1, 1], [1, 0]] 
print(confusion_matrix(data))

data = [[0, 1], [0, 1], [0, 0], [0, 1], [0, 0], [0, 1], [0, 1], [0, 0], [1, 0], [0, 1], [1, 0], [0, 0], [0, 1], [0, 1], [0, 1], [1, 0]] 
print(confusion_matrix(data))
