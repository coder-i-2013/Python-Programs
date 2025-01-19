import turtle
turtle.Screen().bgcolor("teal")
turtle.Screen().setup(300,400)
polygon= turtle.Turtle()
tri= turtle.Turtle()

ns= 3
sl=120
a=360.0/ns
for i in range(ns):
    tri.forward(sl)
    tri.right(a)
ns= 3
sl=120
a=360.0/ns
b=15
for c in range(ns):
    polygon.penup()
    polygon.left(45)
    polygon.forward(b)
for i in range(ns):
    polygon.pendown()
    polygon.forward(sl)
    polygon.right(a)
turtle.done()