import math
def Calculate_circ_perimiter(radius):
    return (math.pi*2)*radius
def Calculate_rect_perimiter(l,w):
    return (l*2)+(w*2)
def Calculate_squ_perimiter(l):
    return l*4
def Calculate_tri_perimiter(b,h,l):
    return b+h+l
while True:
    print("Welcome to the perimiter calculator")
    print("1. square \n 2.rectangle \n 3.circle \n 4.triangle:")
    choice= int(input("Enter your choice(1/2/3/4): "))
    if (choice==1):
        l =float(input("Enter the length:"))
        print("The perimiter of this square is ",Calculate_squ_perimiter(l))
    elif (choice==2):
        l =float(input("Enter the length:"))
        w=float(input("Enter the width:"))
        print("The perimiter of this reactangle is ",Calculate_rect_perimiter(l,w))
    elif (choice==3):
        radius= float(input("Enter a radius for your circle: "))
        perimiter= Calculate_circ_perimiter(radius)
        print("The perimiter of this circle is:",perimiter)
    elif (choice==4):
        l=float(input("Enter the first side:"))
        w=float(input("Enter the second side:"))
        b=float(input("Enter the third side:"))
        perimiter=Calculate_tri_perimiter(l,w,b)
        print(f"The perimiter of this triange is {perimiter}")
    else:
        print("invalid choice")
    exit1= input("Do you want to exit yes or no (y/n):")
    if (exit1=="y"):
        break

