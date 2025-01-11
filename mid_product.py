num=int(input("enter a number: "))
t= num
numlen=0
while t>0:
    numlen+=1
    t=int(t/10)
if numlen >= 4:
    numlen=int(numlen/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlen:
            mid1=rem
        elif chk==(numlen-1):
            mid2=rem
        num=int(num/10)
        chk=chk+1
    product=mid1*mid2
    print("the product of the middle digts are",product)
else:
    print("this not a 4 or larger than 4 digit number")

