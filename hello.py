import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a random password of length 12
password = generate_password(12)
print("Random password:", password)
