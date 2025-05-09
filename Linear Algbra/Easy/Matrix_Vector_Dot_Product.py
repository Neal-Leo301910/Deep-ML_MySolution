'''Write a Python function that computes the dot product of a matrix and a vector. 
The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. 
A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. 
For example, an n x m matrix requires a vector of length m.
'''


'''矩阵和向量相乘（矩阵-向量乘法）需要满足：矩阵的列数必须等于向量的长度
矩阵的每一行与向量做点积，结果是一个新的向量，长度等于矩阵的行数
m*n矩阵a 和 1*n向量b 相乘, 得到 1*n向量c
c1 = a11*b1+a12*b2+...a1n*bn 
cn = am1*b1+am2*b2+...amn*bn 
'''


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
# Return a list where each element is the dot product of a row of 'a' with 'b'.
# If the number of columns in 'a' does not match the length of 'b', return -1.

    if len(a[0]) != len(b):
        return -1
    
    dot = []
    
    for row in range(len(a)):
        sum_row = 0
        for col in range(len(a[0])):
            sum_row += (a[row][col] * b[col])
        dot.append(sum_row)
        
    return dot

print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
print(matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]))
print(matrix_dot_vector([[1.5, 2.5], [3.0, 4.0]], [2, 1]))



