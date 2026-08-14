# Finally keyword in Python

def sunflower():                 # Created a function named sunflower
    try:                    # Used for risky code which might give an error
        l = [1, 2, 3, 4, 5, 6]
        i = int(input("Enter the index for number l: "))

        print(l[i])

    except:                 # Used to handle the error
        print("Sorry, some error occurred")
        return ("enter indexing form 0 to 5")

    finally:                # Always executes whether the code runs or gives an error
        print("Finally is always executed")


x = sunflower()
print(x)