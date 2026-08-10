# Dictionaries in Python
students = {
    # roll number       name
    1:               "Keshab",
    10:                "EBii",
    101:               "kRY",
    123:                "CR",
    156:                "buzz",
    168:                "nissh",
    189:                 "prabss"
}
print(students[1])
print(students[101])
print(students[10])

print("************************")

# Adding a new item
students[200] = "Ram"
print(students)

print("************************")

# Updating a value
students[123] = "CR Updated"
print(students[123])

print("************************")

# Checking if a key exists
if 3 in students:
    print("Roll number found")
else :
    print("Roll Number not found")