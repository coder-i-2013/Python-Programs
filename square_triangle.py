import turtle
choice= int(input("if you want to create a triangle type one if you want to create a square type 2 (1/2):"))
def draw_triangle():
    turtle.reset()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def draw_square():
    turtle.reset()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

if (choice==1):
    draw_triangle()
if (choice==2):
    draw_square()
turtle.done() 