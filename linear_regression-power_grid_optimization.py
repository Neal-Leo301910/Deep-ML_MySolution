'''
It is the year 2157. Mars has its first thriving colony, and energy consumption is steadily on the rise. 
As the lead data scientist, you have daily power usage measurements (10 days) affected by both a growing linear trend and a daily fluctuation. 
The fluctuation follows the formula fáµ¢ = 10 x sin(2Ï x i / 10), where i is the day number (1 through 10). 
Your challenge is to remove this known fluctuation from each data point, fit a linear regression model to the detrended data, 
predict day 15's base consumption, add back the fluctuation for day 15, and finally include a 5% safety margin. 
The final answer must be an integer, ensuring you meet the colony's future needs.


daily fluctuation for day i: f_i = 10 * sin(2*pi*i/10)
y = w*x + b
w = \sum_{i=1}^{m} y_i *(x_i - x_mean) / (\sum_{i=1}^{m} x_i^2 - 1/m * (\sum_{i=1}^{m} x_i)^2)
b = 1 /m * \sum_{i=1}^{m}(y_i - w*x_i)
predicted_15 = w*x + b + 10 * sin(2*pi*15/10)
final_15 = 1.05 * ceil(predicted_15)
'''


import math
import numpy as np

PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
    
    y = np.array(consumption_data)
    
    n = len(consumption_data)
     
    x = np.arange(n) + 1
    fluc = 10 * np.sin(PI * 2 * x / 10)
    y = y - fluc
    
   
    w = ( n*sum(x*y) - sum(x)*sum(y) ) / ( n * sum(x ** 2) - sum(x) ** 2)
    b = (sum(y) - w * sum(x)) / n
    
    base_15 = w * 15 + b
    pred_15 = base_15 + 10 * np.sin(PI * 2 * 15 / 10)
        
    return int(1.05 * np.ceil(pred_15))


print(power_grid_forecast([150, 165, 185, 195, 210, 225, 240, 260, 275, 290]))

print(power_grid_forecast([160, 170, 190, 200, 215, 230, 245, 265, 280, 295]))

print(power_grid_forecast([140, 158, 180, 193, 205, 220, 237, 255, 270, 288]))
