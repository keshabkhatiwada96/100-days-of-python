# Function Arguments in Python

# # Default Argument
def Average(a=4,b=8):     # a and b are required
 print("  Default Argument: ", (a+b)/2)

Average(30,20)              # Pass values in correct order
Average()
 
print("+++++++++++++++++++")


# keyword Arguments
def Subtract(a,b):          # value of a and b are not required
    print("keyword Arguments ",a-b)


Subtract(a=20, b=30)  # Order doesn't matter
Subtract(b=20, a=30)  # Order doesn't matter

print("+++++++++++++++++++")

# Required Arguments                     # Both arguments must be provided.
def add(a,b):
   print("Required Arguments", a+b)

add(10,2)


print("+++++++++++++")


# Variable-Length Arguments                 
def details(**info):                         # Stores multiple keyword arguments in a dictionary.
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Country:", info["country"])

details(name="Keshab", age=20, country="Nepal")