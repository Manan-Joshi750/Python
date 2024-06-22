import random
import string

def genPassword(pass_len, use_letters=True, use_digits=True, use_punctuation=True):
    char_values = ''
    if use_letters:
        char_values += string.ascii_letters
    if use_digits:
        char_values += string.digits
    if use_punctuation:
        char_values += string.punctuation
    
    if not char_values:
        print("Please enable at least one character type (letters, digits, punctuation).")
        return None
    
    password_list = [random.choice(char_values) for _ in range(pass_len)]
    password = ''.join(password_list) 
    return password

# Checking the validity of password length.
while True:
    try:
        pass_len = int(input("Enter the length of the password: "))
        if pass_len <= 0:
            print("Password length must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# So the user can decide how their password should look like...
use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
use_punctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'

result = genPassword(pass_len, use_letters, use_digits, use_punctuation)
if result:
    print("Your Password is:", result)