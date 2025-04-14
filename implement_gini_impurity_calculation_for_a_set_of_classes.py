'''
Task: Implement Gini Impurity Calculation
Your task is to implement a function that calculates the Gini Impurity for a set of classes. 
Gini impurity is commonly used in decision tree algorithms to measure the impurity or disorder within a node.

Gini Impurity=1− 1 -∑(p_i)^2
'''
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	unqiue_chara = np.unique(y)
    tot_num = len(y)

    Gini_imp = 1

    for val in unqiue_chara:
        Gini_imp -= (np.count_nonzero(y == val) / len(y)) ** 2
    
    return round(Gini_imp,3)


y = [0, 0, 0, 0, 1, 1, 1, 1] print(gini_impurity(y))
y = [0, 0, 0, 0, 0, 1] print(gini_impurity(y))
y = [0, 1, 2, 2, 2, 1, 2] print(gini_impurity(y))
