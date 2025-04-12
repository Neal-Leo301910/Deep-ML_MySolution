'''
Implement a batch iterable function that samples in a numpy array X and an optional numpy array y. 
The function should yield batches of a specified size. \
If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.
'''

import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	
    m,n = X.shape

    if y is None:
        return X.tolist()
    else:
        batch_data = []

        for i in range(0,m,batch_size):
            X_batch = X[i:i+batch_size]
            y_batch = y[i:i+batch_size]
            batch_data.append([X_batch,y_batch])

        return [[arr.tolist() for arr in item] for item in batch_data]

    
    
print(batch_iterator(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), batch_size=3))

print(batch_iterator(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), np.array([1, 2, 3, 4, 5]), batch_size=2))
