import turtle

P=turtle.Turtle()
P.color("red")

P.fillcolor("red")
P.begin_fill()
for rectangle in range(2):
    P.forward(100)
    P.right(90)
    P.forward(40)
    P.right(90)
P.end_fill()
turtle.done()