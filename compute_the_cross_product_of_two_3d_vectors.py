‘’‘
Implement a function to compute the cross product of two 3-dimensional vectors. 
The cross product of two vectors results in a third vector that is perpendicular to both and follows the right-hand rule. 
This concept is fundamental in physics, engineering, and 3D graphics.
’‘’
import numpy as np

def cross_product(a, b):
    crx_prod = np.zeros_like(a,dtype=int)
    
    for i in range(len(crx_prod)):
        idx_m = np.mod(i+1,3).astype(int)
        idx_n = np.mod(i+2,3).astype(int)
        m = [a[idx_m],a[idx_n]]
        n = [b[idx_m],b[idx_n]]  
        new_arr = np.vstack((m,n))
        crx_prod[i] = new_arr[0][0]*new_arr[1][1] - new_arr[0][1]*new_arr[1][0]
    

    return crx_prod.tolist()
    
