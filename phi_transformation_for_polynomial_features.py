'''
Write a Python function to perform a Phi Transformation that maps input features into a higher-dimensional space by generating polynomial features. 
The transformation allows models like linear regression to fit nonlinear data by introducing new feature dimensions that represent polynomial combinations of the original input features. 
The function should take a list of numerical data and a degree as inputs, and return a nested list where each inner list represents the transformed features of a data point. 
If the degree is less than 0, the function should return an empty list.
'''

import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    """
	  Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	  Args:
	  data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.
    X(Phi) = 1 + x + x^2 + x^3 + .... + x^d
    """

    if degree < 0:
        return []
    else:
        data_inarray = np.array(data,dtype=float)
        data_num = data_inarray.size
        poly_num = degree+1
        
        powers = np.arange(degree+1)
        
        results = np.zeros((data_num,poly_num))
        ‘’‘
        enumerate(powers): enumerate() 是一个内置函数，它接受一个可迭代对象（比如列表、数组、字符串等），并返回一个迭代器。这个迭代器每次产生一对值：(索引, 元素)。
        例如，如果 powers = [10, 20, 30]，那么 enumerate(powers) 会依次生成：(0, 10) (1, 20) (2, 30)
        for i, powers in ...:
        for 循环会遍历 enumerate(powers) 返回的每一对值。
        通过解包（unpacking），每一对值被赋值给两个变量：
        i：索引（通常是整数，从 0 开始）。
        powers：对应的元素（来自 powers 可迭代对象）。
        注意：这里的变量名 powers 可能会引起混淆，因为它和外层的 powers 同名。通常应该用一个不同的名字（比如 power），但代码本身是合法的，内层的 powers 会覆盖外层的作用域。
        循环的行为：每次循环时，i 是当前元素的索引，powers 是当前元素的值。循环会遍历整个 powers 可迭代对象。
        ’‘’
        for i, powers in enumerate(powers):
            results[:,i] = data_inarray ** powers
            print(results[:,i])
            print(powers)
    
        return results.tolist()

print(phi_transform([], 2))
print(phi_transform([1.0, 2.0], -1))
print(phi_transform([1.0, 2.0], 2))
print(phi_transform([1.0, 3.0], 3))
print(phi_transform([2.0], 4))


