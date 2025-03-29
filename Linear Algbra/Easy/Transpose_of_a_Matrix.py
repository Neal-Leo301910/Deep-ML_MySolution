‘’‘Write a Python function that computes the transpose of a given matrix.‘’‘

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    b =  [[0 for j in range(len(a))] for i in range(len(a[0]))]
    
    for j in range(len(a[0])):
        for i in range(len(a)):
            b[j][i] = a[i][j]
    return b



transpose_matrix([[1,2,3],[4,5,6]])
transpose_matrix([[1,2],[3,4],[5,6]])

