# Day 10 - String Slicing in Python

# Creating a string
name = "Python Programming"

print(name)

# Finding the length of the string
print(len(name))

# Accessing characters using indexing
print(name[0])      # First character
print(name[7])      # Character at index 7

# Basic string slicing
print(name[0:6])    # Python
print(name[7:18])   # Programming

# Omitting the start index
print(name[:6])     # Starts from index 0

# Omitting the end index
print(name[7:])     # Goes till the end

# Copying the entire string
print(name[:])

# Negative indexing
print(name[-1])     # Last character
print(name[-5])     # Fifth character from the end

# Negative slicing
print(name[-11:])   # Programming
print(name[:-12])   # Python

# Mixing positive and negative indices
print(name[0:-12])  # Python
print(name[-11:-1]) # Programmin

# Coding challenge examples (predict before running)
text = "Martha"

print(text[-4:-2])
print(text[-3:])
print(text[:-1])
print(text[-5:-1])