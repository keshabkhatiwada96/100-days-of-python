# List Methods in Python

r = [1,2,3,4,5,6,50,96,54,45]
print(r)

r.append(7)      # Adds an element at the end.
print(r, "append")

r.sort()         # Arranges the list in ascending order.
print(r, "sort")



r.insert(1, 96)  # Inserts 96 at index 1.
print(r, "insert")

r.remove(96)     # Removes the first occurrence of 96.
print(r, "remove")

r.pop()          # Removes the last element.
print(r, "pop")

print(r.count(50), "count")   # Counts how many times 50 appears.

print(r.index(54), "index")   # Returns the index of 54.

copy_list = r.copy()          # Creates a copy of the list.
print(copy_list, "copy")

r.reverse()      # Reverses the list.
print(r, "reverse")