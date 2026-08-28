# NumPy: Indexing, Slicing and Operations

import numpy as np

numbers = np.array([1,2,3,4,5,6,7,8,9])    
print(numbers[0])       #indexing
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

print("------------------------")

print(numbers[1:4])                #slicing
print(numbers[1:])

print("------------------------------")

numbers[1]=100   #changing array element numpy array are mutable
print(numbers)

print("-----------------------------")

numbers1 = np.array([10,20,30,40,50,60])
print(numbers1 > 30)                     # comparison operation returns True or False for each element


print("--------------------------------")


print(numbers1[numbers1 < 30])          #boolean filtering

print("--------------------------------")
arr = np.array([        # 2D array
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr[0, 1])
print(arr[1, 2])

print("--------------------------------")


print(arr[0:2, 1:3])              # 2D slicing

