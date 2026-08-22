# OOP Practice printing 2 objects.
class Student:

    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


# first object
student1 = Student("Keshab", 20, "BIT")

#  second object
student2 = Student("Ram", 21, "BCA")


# Printing student 1
print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)


# Printing student 2 
print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Course:", student2.course)