age=int(input("Enter your age in whole numbers: "))
value=1
value1=1
if age>10:
    value=2
else:
    value=0
if age<20:
    value1=2
else:
    value1=0
if value1==2 and value==2:
    print("The user's age is between 10 and 20")
else:
    print("The user's age is not between 10 and 20")