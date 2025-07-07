import random
import string

# Function to generate password
def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long!"

    # Define possible characters: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
print("Password Generator")
try:
    length = int(input("Enter the desired length of your password: "))
    password = generate_password(length)
    print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")
    
