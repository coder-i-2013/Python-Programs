print("Half Pyramid pattern of numbers: ")
n= int(input("Enter the number of rows: "))
k=1
for i in range(n):
    for j in range(i+1):
        print(k, end=" ")
        k+=1
    print()