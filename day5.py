# Variables and Data Types  What is a Variable?
#   A variable is a container used to store data in a program.
#   The value stored in a variable can be changed during program execution.
#   What are Data Types? 
#  A data type defines what kind of value a variable stores.


# Day 5 - Variables and Data Types

# Variable: A variable is a named container used to store data in a program.
# Data Type: A data type defines what kind of value a variable stores.

# Main Data Types in Python

age = 20                          # int     Stores whole numbers.
height = 5.8                      # float   Stores decimal numbers.
name = "Keshab"                   # str     Stores text inside quotes.
is_student = True                 # bool    Stores True or False values.
fruits = ["Apple", "Banana"]      # list    Stores multiple ordered items (mutable).
colors = ("Red", "Green")         # tuple   Stores ordered items (immutable).
student = {"Name": "Keshab"}      # dict    Stores data as key-value pairs.
numbers = {1, 2, 3, 3, 4}         # set     Stores unique values only.

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print(type(fruits))
print(type(colors))
print(type(student))
print(type(numbers))