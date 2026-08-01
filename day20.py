# Introduction to Lists in Python

marks = [78, 98, 74, "keshab", 6.5, 45, 89]     # list can store different data types

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-2])      # negative indexing

if 96 in marks:       # checks if 96 is in list
    print("yes")
else:
    print("no")

print("++++++++++++++++++++")

# List Slicing

print(marks[1:4])     # prints index 1 to 3
print(marks[:4])      # prints from start to index 3
print(marks[2:])      # prints from index 2 to end
print(marks[-4:-1])   # slicing with negative index

print("++++++++++++++++++++")

# Jump Indexing

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numbers[::2])      # every 2nd item
print(numbers[1::2])     # every 2nd item from index 1
print(numbers[1:8:3])    # step of 3

print("++++++++++++++++++++")

# List Comprehension

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newlist = [i for i in num]      # copy all items
print(newlist)

square = [i*i for i in num]     # square of each number
print(square)

even = [i for i in num if i % 2 == 0]     # only even numbers
print(even)

odd = [i for i in num if i % 2 != 0]      # only odd numbers
print(odd)