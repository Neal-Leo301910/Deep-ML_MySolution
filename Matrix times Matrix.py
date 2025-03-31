'''
multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. C=A⋅B
'''

import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(b) != len(a[0]):
        return -1
    else:
        c = np.dot(a,b).tolist()
        
    
    return c

print(matrixmul([[1,2,3],[2,3,4],[5,6,7]],[[3,2,1],[4,3,2],[5,4,3]]))
print(matrixmul([[0,0],[2,4],[1,2]],[[0,0,1],[2,4,1],[1,2,3]]))
