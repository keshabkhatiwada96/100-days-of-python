import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))
print("Variance:", np.var(numbers))

print("----------")

numbers1 = np.array([10, 50, 20, 80, 30])

print("Maximum index:", np.argmax(numbers1))
print("Minimum index:", np.argmin(numbers1))

print("-----------------")

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Total:", np.sum(arr))
print("Column sums:", np.sum(arr, axis=0))
print("Row sums:", np.sum(arr, axis=1))