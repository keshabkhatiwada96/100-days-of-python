
# JSON in Python

import json


# dumps()  Python object -- JSON string

students = {
    "name": "Keshab",
    "age": 21,
    "course": "BIT"
}

json_data = json.dumps(students)

print(json_data)
print(type(json_data))


# loads()  JSON string -- Python object

json_data = '{"name": "Keshab", "age": 21, "course": "BIT"}'

student = json.loads(json_data)

print(student)
print(student["name"])
print(type(student))


#dump() Python object -- JSON file

student = {
    "name": "Keshab",
    "age": 21
}

with open("student.json", "w") as file:
    json.dump(student, file)


#  load()  JSON file -- Python object

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(type(student))


