'''
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. 
The function should iterate n times, rounding each intermediate solution to four decimal places, 
and return the approximate solution x.
'''

import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
'''
1. Initialization: Start with an initial guess for ( x ).
2. Iteration: For each equation ( i ), update ( x[i] ) using:
    x[i] = (1 / a[ij]) * (b[i] - sum(j!=i)x[j]*a[ij])\
where ( a_{ii} ) are the diagonal elements of ( A ), and ( a_{ij} ) are the off-diagonal elements.
3. Convergence: Repeat the iteration until the changes in ( x ) are below a certain tolerance or until a maximum number of iterations is reached.
'''

    x= np.zeros(len(b))
    a_ii = np.diag(A)
    a_ij = A - np.diag(a_ii)
    x_hold = np.zeros(len(b))
    for _ in range(n):
        for i in range(len(A)):
            x_hold[i] = (1/a_ii[i]) * (b[i] - sum(a_ij[i]*x))
        x = x_hold.copy()
        
    return np.round(x,4).tolist()
