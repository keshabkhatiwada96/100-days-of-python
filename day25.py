# f-strings in Python

# 1. Basic variables
name = "Keshab"
study = "BIT"
semester = "2nd Semester"
address = "Birtamode"

print(f"Hi, my name is {name}. I'm from {address}. Currently, I'm studying {study} {semester}.")

print("****************************")
# 2. Float formatting
price = 28.9879
print(f"For only {price:.2f} dollars")

print("****************************")
# 3. Text alignment
text = "Python"
print(f"|{text:<10}|")   # Left align
print(f"|{text:^10}|")   # Center align
print(f"|{text:>10}|")   # Right align

print("****************************")
# 4. Expressions inside f-strings
a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Product = {a * b}")
