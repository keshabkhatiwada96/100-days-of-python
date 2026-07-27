# For Loops in Python

name = "keshab"
for i in name:
 print(i) 

print("*******") 


for r in range(20):
    print(r + 1)  # I used r + 1 because range(20) generates numbers from 0 to 19.
                        # Adding 1 makes the output start from 1 and end at 20.


print("**********")
for k in range(1, 12, 3):   
        print(k)       # Starts from 1 and stops before 12.
                # The step value is 3, so the output is 1, 4, 7, and 10.
             # After 10, Python tries 13, but since 13 is greater than the stop value the loop ends.