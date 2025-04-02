import numpy as np

def phi_corr(x: list[int], y: list[int]) -> float:
    """
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
    
    x_arr = np.array(x)
    y_arr = np.array(y)
    sum_arr = np.add(x_arr,y_arr)

    
    x_00,x_11,x_11,x_01 = 0
    for bit in range(len(sum_arr)):
        if sum_arr[bit] == 2:
            x_11 += 1
        elif sum_arr[bit] == 0:
            x_00 += 1
        else:
            if x_arr[bit] == 1:
                x_10 += 1
            else:
                x_01 += 1
    
    A = (x_00 * x_11) - (x_01 * x_10) 
    B = (x_00 + x_01) * (x_10 + x_11) * (x_00 + x_10) * (x_01 + x_11)
    phi = A / B ** 0.5 
 
    return round(phi,4)
    

print(phi_corr([1, 1, 0, 0], [0, 0, 1, 1]))
print(phi_corr([1, 1, 0, 0], [1, 0, 1, 1]))
print(phi_corr([0, 0, 1, 1], [0, 1, 0, 1]))
print(phi_corr([1, 0, 1, 0,1,1,0], [1, 1, 0, 0,1,1,1]))
