# Day 6 - Operators and Simple Calculator

# Operators perform mathematical operations like +, -, *, and /.
# input() is used to take data from the user.
# float() converts user input into numbers and supports decimal values.
# if, elif, and else are used to make decisions based on conditions.
# Built a simple calculator using arithmetic operators and conditional statements.
# Learned that invalid input can cause a ValueError.
# Discovered that my Num Lock being off resulted in an empty input and caused the error.

a = int(input("Enter your first number: "))
operator = input("Enter your operator (+,-,*,/: )")
b = int(input("Enter your second number: "))

if operator== "+" :
 print ("Addition = ", a+b)

elif operator== "-" :
 print ("Subtraction = ", a-b)

elif operator== "*" :
 print ("Multiplication= ", a*b)

elif operator == "/" :
 print ("Division = ", a/b)

else:
 print("Invalid Operator!! Use (+,-,*,/)")