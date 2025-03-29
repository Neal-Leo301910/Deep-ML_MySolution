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
	#pass

    if len(a[0]) == len(b):
        sol = [0]*len(a)
        print(sol)
        for i in range(len(a)):
            # i = 0~m-1
            c_j = 0
            for j in range(len(a[i])):
                # j = 0~n-1
                c_ij = a[i][j] * b[j]
                c_j += c_ij              
            #sol.append(c_j)
            sol[i] = c_j
        return sol
    else:
        return -1

matrix = [[1,2],[2,4]]
vector = [1,2]
print(matrix_dot_vector(matrix, vector))



