'''
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. 
The function should iterate n times, rounding each intermediate solution to four decimal places, 
and return the approximate solution x.

The Jacobi method is an iterative algorithm used for solving a system of linear equations ( Ax = b ). 
This method is particularly useful for large systems where direct methods, 
such as Gaussian elimination, are computationally expensive.
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
    a_ii = np.diag(A) #获得对角线元素
    a_ij = A - np.diag(a_ii) #获得非对角线元素
    x_hold = np.zeros(len(b))
    for _ in range(n):#实现n次迭代
        for i in range(len(A)):
            x_hold[i] = (1/a_ii[i]) * (b[i] - sum(a_ij[i]*x)) # Jacob Method 更新该迭代次数下的x值
        x = x_hold.copy() #将原本的x值复写
        
    return np.round(x,4).tolist()

print(solve_jacobi(np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]]), np.array([-1, 2, 3]),2))
print(solve_jacobi(np.array([[4, 1, 2], [1, 5, 1], [2, 1, 3]]), np.array([4, 6, 7]),5))
print(solve_jacobi(np.array([[4,2,-2],[1,-3,-1],[3,-1,4]]), np.array([0,7,5]),3))
