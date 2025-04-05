'''
In this task, you are required to implement a function matrix_image(A) that calculates the column space of a given matrix A. 
The column space, also known as the image or span, consists of all linear combinations of the columns of A. 
To find this, you'll use concepts from linear algebra, focusing on identifying independent columns that span the matrix's image. 
Your task: Implement the function matrix_image(A) to return the basis vectors that span the column space of A. 
These vectors should be extracted from the original matrix and correspond to the independent columns.
1. 先计算RREF
2. 找到主元（每行第一个非零元素）所在列：主元列
3. 提取原矩阵里的主元列所有元素
'''
import numpy as np

def matrix_image(A):
	
    B = A.copy()

    row,col = A.astype(np.float32).shape


    for i in range(row):
        if A[i,i] == 0:
            non_zero_idx = np.nonzero(A[i:,i])[0]

            if len(non_zero_idx) == 0:
                continue
            
            A[i] = A[i] + A[non_zero_idx[0]+1]

        A[i] = A[i] / A[i,i]

        for j in range(row):
            if j != i:
                A[j] -= A[j,i] * A[i]
    
    RREF = A

    piv_row,piv_col = RREF.shape

    image = []

    for m in range(piv_row):
        piv_idx = np.nonzero(RREF[m])[0]
        if len(piv_idx) != 0:
            image.append(B[:,piv_idx[0]])
        

    return np.column_stack(image).tolist()
