import math
def Calculate_circ_area(radius):
    return math.pi*radius**2
def Calculate_rect_area(l,w):
    return l*w
def Calculate_squ_area(l):
    return l*l
def Calculate_tri_area(b,h):
    return (b*h)/2
while True:
    print("Welcome to the area calculator")
    print("1. square \n 2.rectangle \n 3.circle \n 4.triangle:")
    choice= int(input("Enter your choice(1/2/3/4): "))
    if (choice==1):
        l =float(input("Enter the length"))
        print("The area of this square is ",Calculate_squ_area(l))
    elif (choice==2):
        l =float(input("Enter the length"))
        w=float(input("Enter the width"))
        print("The area of this reactangle is ",Calculate_rect_area(l,w))
    elif (choice==3):
        radius= float(input("Enter a radius for your circle: "))
        area= Calculate_circ_area(radius)
        print("The area of this circle is:",area)
    elif (choice==4):
        l =float(input("Enter the length"))
        w=float(input("Enter the width"))
        area=Calculate_tri_area(l,w)
        print(f"The area of this triange is {area}")
    else:
        print("invalid choice")
    exit1= input("Do you want to exit yes or no (y/n)")
    if (exit1=="y"):
        break

