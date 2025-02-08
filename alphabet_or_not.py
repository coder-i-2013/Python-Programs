value=input("Enter any number digit or letter: ")
if value.isalpha():
    print("The value is a letter.")
else:
    print("The value is not a letter.")
    value=float(input("Enter the same number, digit, or letter as before:  "))
if type(value) in (int, float):
    print("The value is a number.")
else:
    print("The value is not a number.")
