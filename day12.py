# FIXME: If-Else Statements in Python


age = int(input("Enter your age: "))  # FIXME: "input() takes input from the user."

# FIXME: "if statement executes a block of code if the condition is True."
if age >= 18:
    print("You can vote")

# FIXME: "if-else statement executes one block if the condition is True and another block if it is False."
if age >= 18:
    print("Adult")
else:
    print("Minor")

# FIXME: "input() takes input from the user."
marks = float(input("Enter your marks: "))

# FIXME: "elif checks another condition if the previous condition is False.
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# FIXME: "comparison operators compare two values and return True or False."
print(age > 18)    # Greater than
print(age < 18)    # Less than
print(age >= 18)   # Greater than or equal to
print(age <= 18)   # Less than or equal to
print(age == 18)   # Equal to
print(age != 18)   # Not equal to

# FIXME: "nested if statement is an if statement inside another if statement."
salary = float(input("Enter your salary: "))
experience = int(input("Enter your years of experience: "))

if salary >= 40000:
    if experience >= 2:
        print("Eligible for promotion")
    else:
        print("Need more experience")
else:
    print("Salary requirement not met")

# FIXME: "indentation defines the block of code in Python."
number = float(input("Enter a number: "))

if number > 0:
    print("Positive Number")
    print("Program Finished")
elif number <0:
 print("Negative number")
 print("Program Finished")
