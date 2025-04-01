'''
Write a Python function to calculate various descriptive statistics metrics for a given dataset. 
The function should take a list or NumPy array of numerical values and return a dictionary containing 
mean, median, mode, variance, standard deviation, percentiles (25th, 50th, 75th), and interquartile range (IQR).
'''

import numpy as np 
def descriptive_statistics(data):
	# Your code here
    arr = np.array(data)
    mean = np.mean(arr)
    median = np.median(arr)
    unique, counts = np.unique(data, return_counts=True)
    mode = unique[np.argmax(counts)] if len(data) > 0 else None
    variance = np.var(arr)
    std_dev = np.std(arr)
    percentiles= np.percentile(data, [25, 50, 75])
    iqr = percentiles[2] - percentiles[0]
	stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
	return stats_dict

print(descriptive_statistics([10, 20, 30, 40, 50]))
