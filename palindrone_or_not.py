number=int(input("Enter Your Number: "))
original_number=number
reversed_number=0

while number> 0:
    digit= number%10
    reversed_number= reversed_number * 10 + digit
    number//=10

if original_number== reversed_number:
    print(f"{original_number} is a plaindrome")
else:
    print(f"{original_number} is not a plaindrome")
