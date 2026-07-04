import numpy as np

# Basic array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.shape)
print(arr.dtype)

# Operations
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

# Slicing
print(arr[1:4])
print(arr[:3])
print(arr[2:])

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.shape)

# zeros, ones, arange
print(np.zeros(5))
print(np.ones(3))
print(np.arange(1, 10, 2))
