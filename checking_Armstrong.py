num=int(input("Enter an number to check if it is armstrong: "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+(digit**len(str(num)))
    temp=temp//10
if num==sum:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")
