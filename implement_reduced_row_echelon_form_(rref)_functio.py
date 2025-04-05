‘’‘
In this problem, your task is to implement a function that converts a given matrix into its Reduced Row Echelon Form (RREF). 
The RREF of a matrix is a special form where each leading entry in a row is 1, 
and all other elements in the column containing the leading 1 are zeros, except for the leading 1 itself.

However, there are some additional details to keep in mind:

Diagonal entries can be 0 if the matrix is reducible (i.e., the row corresponding to that position can be eliminated entirely).
Some rows may consist entirely of zeros.
If a column contains a pivot (a leading 1), all other entries in that column should be zero.
Your task is to implement the RREF algorithm, which must handle these cases and convert any given matrix into its RREF.

一个矩阵是行阶梯形矩阵，如果满足以下条件：

所有全零行（如果有）位于矩阵底部。
每行的第一个非零元素（称为主元，pivot）严格位于前一行主元的右侧。
主元以下的元素全为零。

计算方法
1.从第i列开始，以第i行i列的元素向下查找第一个非零元素作为主元。
2.如果第i行i列的元素就为0，则沿着i列向下寻找第一个非零元素
  2.1.如果搜索出来的元素均为0，则跳到下一行开始搜索
  2.2.将第一个非零元素，作为主元，加到第i行
3.如果第i行i列不为0，则作为主元
4.主元所在行 / 主元的值
5.遍历i列的每一行
  5.1如果该行的index j 不等于 i，则将第j行的所有元素减去 （第j行i列元素*第i行所有元素）的值

’‘’

import numpy as np

def rref(matrix):
	# Convert to float for division operations
    A = matrix.astype(np.float32)
    row,col = A.shape
    
    for i in range(row):
        if A[i,i] == 0:
            non_zero_idx = np.nonzero(A[i:,i])[0]
            
            if len(non_zero_idx) == 0:
                continue
            
            A[i] = A[i] + A[non_zero_idx[0]+i]
            
        A[i] = A[i] / A[i,i]
        for j in range(row):
            if i != j:
                A[j] -= A[j,i] * A[i]
                    
    return A
			
