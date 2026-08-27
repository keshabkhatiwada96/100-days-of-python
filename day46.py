# NumPy Basics

import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers * 2)
print('-----------------------------------------------')

arr = np.array([1, 2, 3, 4])

print(arr.ndim)           #(ndim) Shows the number of dimensions
print(arr.shape)           #(shape) Shows the size of each dimension
print(arr.dtype)            #(dtype)Shows the data type.
print("-----------------------------------------------------------")

# Accessing elements
#  NumPy arrays use indexing.

arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[2])
print("------------------------------------------------")

arr = np.array([10, 20, 30])

print(arr + 5)
print(arr * 2)
print(arr - 5)
print(arr / 2)
print("--------------------------------------------")

arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))