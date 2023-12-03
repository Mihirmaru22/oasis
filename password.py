import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by sampling from the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Set the desired password length (default is 12)
    password_length = 12

    # Generate and print a password
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
