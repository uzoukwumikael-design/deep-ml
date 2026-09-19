import numpy as np

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])  

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	return np.dot(vec1, vec2)