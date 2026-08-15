# Raising Custom Errors in Python


age = int(input("Enter your age: "))

if age < 18:
    # raise is used to give our own error message
    raise ValueError("Age must be 18 or above")

print("You are eligible.")