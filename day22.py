# Introduction to Tuple in Python
# List and tuple are same but list is mutable while tuple is immutable.
tup = (78, 98, 74, "keshab", 6.5, 45, 89)    # tuple can store different data types
print(type(tup))

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-2])      # negative indexing

if 96 in tup:       # checks if 96 is in tuple prints yes else no
    print("yes")
else:
    print("no")

print("++++++++++++++++++++")

# Tuple Slicing

print(tup[1:4])     # prints index 1 to 3
print(tup[:4])      # prints from start to index 3
print(tup[2:])      # prints from index 2 to end
print(tup[-4:-1])   # slicing with negative in