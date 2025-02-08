def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y
print("a add")
print("b subtract")
print("c multiply")
print("d divide")
choice=input("enter you choice from the list above: a/b/c/d")
x=float(input("Enter a number you want to calculate"))
y=float(input("Enter a number you want to calculate"))
if choice=="a":
    print("the sum of x and y is:",add(x,y))
if choice=="b":
    print("the difference of x and y is:",subtract(x,y))
if choice=="c":
    print("the product of x and y is:",multiply(x,y))
if choice=="d":
    print("the quotionet of x and y is:",divide(x,y))



