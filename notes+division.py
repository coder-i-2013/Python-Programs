amount=int(input("Please enter your withdrawl amount"))
note1= (amount//100)
note2= (amount%100)//50
note3=((amount%100)%50)//10
print("the amount of hundred ruppees bills are", note1)
print("the amount of fifty ruppees bills are", note2)
print("the amount of ten ruppees bills are", note3)
