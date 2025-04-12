'''
Implement a function to calculate the Bhattacharyya distance between two probability distributions. 
The function should take two lists representing discrete probability distributions p and q, and return the Bhattacharyya distance rounded to 4 decimal places. 
If the inputs have different lengths or are empty, return 0.0.
'''

import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    
    if len(q) != len(p) or q is None or p is None:
        return 0.0
    else:
        p = np.array(p)
        q = np.array(q)
        
        bc = np.sum((p * q) ** 0.5)
        bd = -np.log(bc)

        return round(float(bd),4)

print(round(bhattacharyya_distance([0.1, 0.2, 0.3, 0.4], [0.4, 0.3, 0.2, 0.1]),4))
print(round(bhattacharyya_distance([0.7, 0.2, 0.1], [0.4, 0.3, 0.3]),4))
print(round(bhattacharyya_distance([], [0.5, 0.4, 0.1]),4))
print(round(bhattacharyya_distance([0.6, 0.4], [0.1, 0.7, 0.2]),4))
print(round(bhattacharyya_distance([0.6, 0.2, 0.1, 0.1], [0.1, 0.2, 0.3, 0.4]),4))
