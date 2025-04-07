‘’‘
k-fold cross-validation是把D划分成k个互斥的大小相似的子集，每次用k-1个子集作为训练集，余下的作为测试集，经过k次训练和测试，返回k次训练结果的均值
’‘’

import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.

    Parameters:
    X (np.ndarray): Feature dataset.
    y (np.ndarray): Target labels.
    k (int): Number of folds.
    shuffle (bool): Whether to shuffle the data before splitting.
    random_seed (int, optional): Seed for reproducibility.

    Returns:
    list of tuples: Each tuple contains train and test indices as lists.
    """
    

    sample_sizes = len(X)
    indices = np.arange(sample_sizes) #生成dataset的indices

    if shuffle:
        np.random.seed(random_seed) if random_seed is not None else None
        np.random.shuffle(indices) #随机重排indices

    folds_size = np.full(k,sample_sizes // k, dtype = int) #生成k个值(为sample_sizes // k)的folds(array)，子集(fold)的大小为sample_sizes整除k的值
    folds_size[:sample_sizes % k] += 1 #如果sample_sizes // k不能整除，把余数安排到前几个fold中，前几个folds的size+1

    folds = []
    current = 0
    for fold_size in folds_size:
        folds.append(indices[current:current+fold_size])#将indices值依次放入folds中，每次放fold_size个
        current += fold_size

    return [(np.concatenate(folds[:i] + folds[i+1:]).tolist(), folds[i].tolist()) for i in range(k)] #返回[x,y]，训练集和测试集，存储的是数据集的indices。

print(k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=5, shuffle=False))
print(k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=2, shuffle=True, random_seed=42))
print(k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]), np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]), k=3, shuffle=False))
print(k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=2, shuffle=False))
