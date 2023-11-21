import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))

    if length <= 0:
        print("Password length should be greater than 0.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")
