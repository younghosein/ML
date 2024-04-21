import numpy as np

#create array, matrix

a = np.array([1,2,3,4])

b = np.array([[1,2],[3,4]])

#shape
print(a.shape, b.shape)

#reshaape
c = a.reshape((4, 1))
print(c.shape) 