import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon= turtle.Turtle()

ns= 6
sl=70
a=360.0/ns
for i in range(ns):
    polygon.forward(sl)
    polygon.right(a)

turtle.done()