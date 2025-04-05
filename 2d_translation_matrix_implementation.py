'''
Your task is to implement a function that applies a 2D translation matrix to a set of points. 
A translation matrix is used to move points in 2D space by a specified distance in the x and y directions.
Write a function translate_object(points, tx, ty) 
where points is a list of [x, y] coordinates and tx and ty are the translation distances in the x and y directions, respectively.
The function should return a new list of points after applying the translation matrix.
'''


import numpy as np
def translate_object(points, tx, ty):
'''

translated_points = [x+x_t, y+y_t]
'''
    # concise version
    trans_arr = [tx,ty]

    translated_points = []

    for point in points:
        translated_points.append([point[0]+trans_arr[0],point[1]+trans_arr[1]])
    
    return translated_points


    # trans_matrix = np.eye(3)
    # trans_matrix[:,2] += [tx,ty,0]
    # translated_points = []
    # for point in points:

    #     homo_cord = point + [1]
    #     mid = np.dot(trans_matrix,homo_cord).tolist()
    #     translated_points.append(mid[0:2])
  
    # return translated_points


triangle = [[0, 0], [1, 0], [0.5, 1]] 
tx, ty = 2, 3 
print(translate_object(triangle, tx, ty))

square = [[0, 0], [1, 0], [1, 1], [0, 1]] 
tx, ty = -1, 2 
print(translate_object(square, tx, ty))

points = [[0, 0], [1, 0], [0.5, 1]]
tx, ty = 2, 3
print(translate_object(points, tx, ty))
