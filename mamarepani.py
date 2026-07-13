print("Think of a number between 1 and 100.")

low = 1
high = 100
attempts = 0

while low <= high:
    guess = (low + high) // 2
    attempts += 1

    print(f"My guess is: {guess}")
    answer = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

    if answer == "c":
        print(f"Yay! I guessed your number in {attempts} attempts.")
        break
    elif answer == "h":
        high = guess - 1
    elif answer == "l":
        low = guess + 1
    else:
        print("Please enter h, l, or c.")