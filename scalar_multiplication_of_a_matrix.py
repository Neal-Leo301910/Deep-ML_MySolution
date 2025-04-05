'''Write a Python function that multiplies a matrix by a scalar and returns the result.'''


def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	# concise version

	result = []

    	for row in matrix:
        	result.append([ele * scalar for ele in row])

	return result

	
	# result = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]	
	# for i in range(len(matrix)):
	# 	for j in range(len(matrix[0])):
	# 		result[i][j] = matrix[i][j] * scalar

	# return result
