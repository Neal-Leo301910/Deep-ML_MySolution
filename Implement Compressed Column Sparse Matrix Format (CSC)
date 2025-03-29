Task: Create a Compressed Column Sparse Matrix Representation
Your task is to implement a function that converts a dense matrix into its Compressed Column Sparse (CSC) representation. The CSC format stores only non-zero elements of the matrix and is efficient for matrices with a high number of zero elements.

Write a function compressed_col_sparse_matrix(dense_matrix) that takes in a two-dimensional list dense_matrix and returns a tuple of three lists:

values: List of non-zero elements, stored in column-major order.
row indices: List of row indices corresponding to each value in the values array.
column pointer: List that indicates the starting index of each column in the values array.

import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	non_zeros_num = np.count_nonzero(dense_matrix)
    non_zero_idx = np.nonzero(dense_matrix)
    non_zero_idx_order = np.argsort(non_zero_idx[1])
    
    vals = np.zeros(non_zeros_num, dtype=int)
    row_idx = np.zeros(non_zeros_num, dtype=int)
    col_ptr = np.zeros(len(dense_matrix[0])+1, dtype=int)
    
    dense_matrix_list = np.array(dense_matrix)
    judge_matrix = dense_matrix_list > 0
    nonzero_num_row = np.sum(judge_matrix,0)
    
    
    for i in range(non_zeros_num):
        row = non_zero_idx[0][non_zero_idx_order[i]]
        col = non_zero_idx[1][non_zero_idx_order[i]]
        vals[i] = dense_matrix[row][col]
        row_idx[i] = row
    
    sum_num_col = 0    
    for j in range(len(nonzero_num_row)):
        sum_num_col += nonzero_num_row[j]
        col_ptr[j+1] = sum_num_col
    
    vals_str = np.array2string(vals, separator=', ')
    row_idx_str = np.array2string(row_idx, separator=', ')
    col_ptr_str = np.array2string(col_ptr, separator=', ')
    
    return (vals_str, row_idx_str, col_ptr_str)


dense_matrix = [
    [0, 0, 3, 0],
    [1, 0, 0, 4],
    [0, 2, 0, 0]
]

vals, row_idx, col_ptr = compressed_col_sparse_matrix(dense_matrix)
