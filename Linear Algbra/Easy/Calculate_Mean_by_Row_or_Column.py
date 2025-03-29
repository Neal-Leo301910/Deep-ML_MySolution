'''Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. 
The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
'''


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
    row_num = len(matrix)
    col_num = len(matrix[0])

    if mode == 'column':
        means = [0] * col_num
        for i in range(col_num):
            sum_row_i = 0   
            for j in range(row_num):
                sum_row_i += matrix[j][i]
            means[i] = sum_row_i / row_num
    elif mode == 'row':
        means = [0] * row_num
        for i in range(row_num):
            sum_col_i = 0   
            for j in range(col_num):
                sum_col_i += matrix[i][j]
            means[i] = sum_col_i / col_num
    return means

