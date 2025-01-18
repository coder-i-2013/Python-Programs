rs=int(input("enter the number of rows"))
if rs%2==0:
    hdr= int(rs/2)
else:
    hdr=int(rs/2)+1
space= hdr-1
for i in range(1,hdr+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,hdr+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(hdr-i)):
        print(end=str(num))
        num=num+1
    print()

              