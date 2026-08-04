# Tuple Operations in Python

# Original Tuple
tup = (1, 2, 3, 4, 5)
print(tup)

print("******************************")

# Modifying a Tuple

tup = (1, 2, 3, 4, 5)

temp = list(tup)      # Convert tuple to list
temp.append(6)        # Add an element
temp.pop(1)           # Remove element at index 1

tup = tuple(temp)     # Convert list back to tuple

print(tup)

print("******************************")

# Tuple Concatenation

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

new_tuple = tup1 + tup2

print(new_tuple)

print("******************************")

# count() Method

tup = (1, 2, 3, 2, 5, 2)

print(tup.count(2))      # Counts how many times 2 appears

print("******************************")

# index() Method

tup = (10, 20, 30, 40, 50)

print(tup.index(30))     # Returns the index of 30

print("******************************")

# index() with Start and End

tup = (10, 20, 30, 20, 50, 20)
  
print(tup.index(20, 2, 6))    # Searches for 20 between index 2 and 5

print("******************************")

# len() Function

tup = (10, 20, 30, 40, 50)

print(len(tup))      # Returns the total number of elements

print("******************************")

# ValueError Example

tup = (10, 20, 30, 40)

try:
    print(tup.index(100))    # Raises ValueError if element is not found
except ValueError:
    print("Value not found in tuple")