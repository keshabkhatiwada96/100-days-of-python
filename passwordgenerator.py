import secrets
import string

def generate_password():
    # Define available characters
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Continuously ask for input until a valid number is entered
    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                print("Length must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
            
    # Generate the secure password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Run the generator
print("Your secure password is: ", generate_password())
