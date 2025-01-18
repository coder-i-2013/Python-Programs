number = int(input("Enter a number: ")) 
ns=number
numlen = 0 
while number > 0: 
    number //= 10 
    numlen += 1 
print("The amount of digits in the number",ns,"is",numlen,)