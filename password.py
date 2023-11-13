import random
import string

def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12, uppercase=True, digits=True, special_chars=True):
    passwords = [generate_password(length, uppercase, digits, special_chars) for _ in range(num_passwords)]
    return passwords
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        if length <= 0 or num_passwords <= 0:
            raise ValueError("Length and number of passwords must be greater than zero.")
        
        passwords = generate_multiple_passwords(num_passwords, length)
        
        print("\nGenerated Passwords:")
        for idx, password in enumerate(passwords, start=1):
            print(f"{idx}. {password}")

    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        if length <= 0 or num_passwords <= 0:
            raise ValueError("Length and number of passwords must be greater than zero.")
        
        passwords = generate_multiple_passwords(num_passwords, length, uppercase, digits, special_chars)
        
        print("\nGenerated Passwords:")
        for idx, password in enumerate(passwords, start=1):
            print(f"{idx}. {password}")

    except ValueError as e:
        print(f"Error: {e}")
