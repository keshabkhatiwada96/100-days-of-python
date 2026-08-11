# Dictionary Methods in Python

students = {
    1: "Keshab",
    10: "Ram",
    101: "Shyam",
    123: "Hari",
    156: "Sita"
}
print(students)
print("************************")

# update() method
students.update({189: "Prabesh"})     # Adds a new key-value pair.
print(students)
print("************************")

# clear() method
students.clear()                      # Removes all items.
print(students)
print("************************")

# pop() method
students = {
    1: "Keshab",
    10: "Ram",
    101: "Shyam",
    123: "Hari"
}
students.pop(101)                     # Removes the item with key 101.
print(students)
print("************************")

# popitem() method
students.popitem()                    # Removes the last key-value pair.
print(students)
print("************************")

# del keyword
del students[10]                      # Deletes the item with key 10.
print(students)
print("************************")

# del the whole dictionary
del students