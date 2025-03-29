‘’‘
Task: Convert a Dense Matrix to Compressed Row Sparse (CSR) Format
Your task is to implement a function that converts a given dense matrix into the Compressed Row Sparse (CSR) format, an efficient storage representation for sparse matrices. The CSR format only stores non-zero elements and their positions, significantly reducing memory usage for matrices with a large number of zeros.

Write a function compressed_row_sparse_matrix(dense_matrix) that takes a 2D list dense_matrix as input and returns a tuple containing three lists:

Values array: List of all non-zero elements in row-major order.
Column indices array: Column index for each non-zero element in the values array.
Row pointer array: Cumulative number of non-zero elements per row, indicating the start of each row in the values array.
’‘’

import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.
    
    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    non_zeros_num = np.count_nonzero(dense_matrix)
    non_zero_idx = np.nonzero(dense_matrix)
    
    vals = np.zeros(non_zeros_num, dtype=int)
    col_idx = np.zeros(non_zeros_num, dtype=int)
    row_ptr = np.zeros(len(dense_matrix)+1, dtype=int)
    
    dense_matrix_list = np.array(dense_matrix)
    judge_matrix = dense_matrix_list > 0
    nonzero_num_col = np.sum(judge_matrix,1)
    
    for i in range(non_zeros_num):
        row = non_zero_idx[0][i]
        col = non_zero_idx[1][i]
        vals[i] = dense_matrix[row][col]
        col_idx[i] = col
    
    sum_num_row = 0    
    for j in range(len(nonzero_num_col)):
        sum_num_row += nonzero_num_col[j]
        row_ptr[j+1] = sum_num_row
    
    vals_str = np.array2string(vals, separator=', ')
    col_idx_str = np.array2string(col_idx, separator=', ')
    row_ptr_str = np.array2string(row_ptr, separator=', ')
    
    return (vals_str, col_idx_str, row_ptr_str)
