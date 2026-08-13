#Exception Handling in Python

a = input("enter a number: ")
print(f"Multiplicaton table of {a} is: ")
try:                        # try Runs the code that may cause an error
                            
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:                      #if error occur the except block will be executed
    print("Invalid Input")
print("Important lines of code ")
print("End of Program")

