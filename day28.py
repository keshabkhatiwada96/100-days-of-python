# Sets in Python

# 1. Creating a set
numbers = {1, 2, 3, 4, 5, 6, 8, 9, 95}
print(numbers)

# 2. Sets do not allow duplicates
numbers = {1, 2, 3, 3, 4, 4, 5}
print(numbers)

# 3. Set with strings
employees = {"Keshab", "Ram", "Shyam", "Keshab"}
print(employees)
# Duplicate "Keshab" is automatically removed

# 4. Empty set
empty_set = set()
print(empty_set)

# 5. {} creates an empty dictionary, NOT a set
empty = {}
print(empty)
print(type(empty))

# 6. Cannot access set using index

# 7. Accessing set elements using a for loop
names = {"Keshab", "Ram", "Shyam"}
for name in names:
    print(name)

