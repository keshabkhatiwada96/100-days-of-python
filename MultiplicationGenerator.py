# Multiplication Table Generator

a = int (input("enter your number: "))
for i in range(1,11) :
    print(i+1)
    result = a * i
    print(f"{a} * {i} = {result}")