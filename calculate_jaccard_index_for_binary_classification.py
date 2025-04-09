'''
Jaccard Index = Intersection(A,B) / Union(A,B)
在以下方面特别有用：
1.评估聚类算法。
2.比较二元分类结果。
3.记录相似性分析。
4.图像分割评估。
在实现 Jaccard index时，处理边缘情况很重要，例如当两个集都为空时（在这种情况下，索引通常定义为 0）。
'''
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
  
    sum_AB = y_true + y_pred

    Intersect = np.count_nonzero(sum_AB == 2)
    Union = np.count_nonzero(sum_AB >= 1)
    
    result = Intersect / Union

    return round(result, 3)

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 1, 0, 1]) 
print(jaccard_index(y_true, y_pred))

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([0, 1, 0, 0, 1, 1]) 
print(jaccard_index(y_true, y_pred))

y_true = np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([1, 0, 1, 0, 0, 0]) 
print(jaccard_index(y_true, y_pred))

np.array([1, 0, 1, 1, 0, 1]) 
y_pred = np.array([0, 1, 0, 1, 1, 0]) 
print(jaccard_index(y_true, y_pred))
