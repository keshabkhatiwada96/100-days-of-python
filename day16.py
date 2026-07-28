# While Loop in Python

r = 1

# '<=' prints 1 to 5, '<' prints 1 to 4.
while (r <= 5):
    print(r)
    r = r + 1

print("********************1")


count = 5

# Decreases count until it reaches 0.
while (count > 0):
    print(count)
    count = count - 1

print("**************2")


x = 5

# 'else' runs after the loop ends normally.
while (x > 0):
    print(x)
    x = x - 1
else:
    print("Counter is 0")