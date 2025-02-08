number=int(input("enter a number: "))
t= number
numlen=0
while t>0:
    numlen+=1
    t=int(t/10)
if numlen >= 4:
    numlen=int(numlen/2)
    chk=0
    while number>0:
        remainder=number%10
        if chk==numlen:
            mid1=remainder
        elif chk==(numlen-1):
            mid2=remainder
        number=int(number/10)
        chk=chk+1
    product=mid1*mid2
    print("The product of the middle digts are",product)
else:
    print("This not a 4 or larger than 4 digit number")

