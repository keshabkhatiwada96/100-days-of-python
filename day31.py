# for Loop with else in Python

# The else block runs only when the loop finishes normally.

for i in range(6):
    if i == 4:
        break    # If the loop is stopped using break, the else block will not execute.

    print(i)
else:
    print("Loop is completed")
