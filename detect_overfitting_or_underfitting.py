def model_fit_quality(training_accuracy, test_accuracy):
	"""
	Determine if the model is overfitting, underfitting, or a good fit based on training and test accuracy.
	:param training_accuracy: float, training accuracy of the model (0 <= training_accuracy <= 1)
	:param test_accuracy: float, test accuracy of the model (0 <= test_accuracy <= 1)
	:return: int, one of '1', '-1', or '0'.
	"""
	# Your code here
	if (training_accuracy - test_accuracy) > 0.2:
        return 1
    elif (test_accuracy < 0.7) and (training_accuracy < 0.7):
        return -1
    else:
        return 0 

print(model_fit_quality(0.95, 0.65))
print(model_fit_quality(0.6, 0.5))
print(model_fit_quality(0.85, 0.8))
print(model_fit_quality(0.5, 0.6))
print(model_fit_quality(0.75, 0.74))
