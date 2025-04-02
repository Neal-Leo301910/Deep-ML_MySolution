‘’‘
Write a Python function that computes the transpose of a given matrix.
转置矩阵就是矩阵行index和列index交换位置
‘’‘

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    b = [ [0 for j in range(len(a))] for i in range(len(a[0])) ]
    
    for row in range(len(a)):
        for col in range(len(a[0])):
            b[col][row] = a[row][col]
    
    return b

print(transpose_matrix([[1,2],[3,4],[5,6]]))
print(transpose_matrix([[1,2,3],[4,5,6]]))


