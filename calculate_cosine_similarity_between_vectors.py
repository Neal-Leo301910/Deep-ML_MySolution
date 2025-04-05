'''
Task: Implement Cosine Similarity
In this task, you need to implement a function cosine_similarity(v1, v2) that calculates the cosine similarity between two vectors. Cosine similarity measures the cosine of the angle between two vectors, indicating their directional similarity.

Input:
v1 and v2: Numpy arrays representing the input vectors.
Output:
A float representing the cosine similarity, rounded to three decimal places.
Constraints:
Both input vectors must have the same shape.
Input vectors cannot be empty or have zero magnitude.
'''


import numpy as np

def cosine_similarity(v1, v2):
	'''
    cos(theta) = v1 dot v2 / (L2-norm v1 * L2-norm v2)
    '''
	Mag_v1 = np.linalg.norm(v1)
    Mag_v2 = np.linalg.norm(v2)
    if v1.shape != v2.shape:
        return []
    elif v1.size == 0 or v2.size == 0 or Mag_v1 == 0 or Mag_v2 == 0:
        return []
    else:
        return np.around(np.divide(np.dot(v1,v2),Mag_v1*Mag_v2),3)


v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))

v1 = np.array([1, 2, 3]) 
v2 = np.array([-1, -2, -3]) 
print(cosine_similarity(v1, v2))

v1 = np.array([1, 0, 7]) 
v2 = np.array([0, 1, 3]) 
print(cosine_similarity(v1, v2))
