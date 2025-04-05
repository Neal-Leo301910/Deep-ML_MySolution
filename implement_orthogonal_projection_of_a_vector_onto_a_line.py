'''
project_L(v) = (v dot L) divide (L dot L) dot L = (v * unit vector L^) dot unit vector L^
'''
import numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
    proj_vec = np.dot(np.divide(np.dot(v,L),np.dot(L,L)),L)
    return [round(float(x), 3) for x in proj_vec]

v = [3, 4]
L = [1, 0]
print(orthogonal_projection(v, L))
    
v = [1, 2, 3] 
L = [0, 0, 1] 
print(orthogonal_projection(v, L))    

v = [5, 6, 7] 
L = [2, 0, 0] 
print(orthogonal_projection(v, L))



