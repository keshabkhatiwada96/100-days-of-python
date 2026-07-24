
# TODO: Password Strength Checker

# TODO: Password Strength Checker

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    else:
        has_special = True

# Check password strength AFTER the loop
if len(password) < 8:
    print("Weak Password")

elif has_upper and has_lower and has_digit and has_special:
    print("Very Strong Password")

elif has_lower and has_digit:
    print("Medium Password")

else:
    print("Weak Password")