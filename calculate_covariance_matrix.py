'''
Write a Python function to calculate the covariance matrix for a given set of vectors. 
The function should take a list of lists, where each inner list represents a feature with its observations, 
and return a covariance matrix as a list of lists. 
Additionally, provide test cases to verify the correctness of your implementation.
计算协方差 cov(x,y) = (x-E[x])(y-E[y]) / [std(x)*std(y)] 
对于矩阵而言：
cov(X,Y) = sum_{k=1}^{m} (x_k - E[X])(y_k - E[Y])
如果变量为行 则E[x]是每一行的平均值, k是行数
如果变量为列 则E[x]是每一列的平均值，k是列数
协方差矩阵为
[[Var(X1)    Cov(X1,X2) Cov(X1,X3)]
 [Cov(X2,X1) Var(X2)    Cov(X2,X3)]
 [Cov(X3,X1) Cov(X3,X2) Var(X3)   ]]
‘’‘

import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

    # np.stack()函数将vectors沿着行方向堆叠
    # np.cov直接返回协方差
    return np.cov(np.stack(vectors,axis=0))


print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]))
