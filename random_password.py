import random
import string
def password():
    password_length = int(input("How many characters should the password contain? "))
    characters = string.ascii_letters + string.digits
    random_password = ''.join(random.choices(characters, k=password_length))
    shuffled_password = ''.join(random.sample(random_password, len(random_password)))
    print("Your randomly generated password is:", shuffled_password)
another=input("Want a new password (y/n) ")
if another == 'y' or another == 'y':
    print(password())
