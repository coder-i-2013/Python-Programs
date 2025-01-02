medicalcause=input("do you have a medical cause Y or N:  ")
atten=int(input("Enter the attendene of a student:  "))
if medicalcause=="Y":
    print("You are allowed")
else:
    if atten>= 75:
        print("You are allowed")
    else:
        print("You are not allwoed")
