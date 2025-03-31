import turtle

pencil=turtle.Turtle()
pencil.color("red")
pencil.speed(0)

for eye in range(360):
    pencil.forward(1)
    pencil.right(1)

pencil.up()
pencil.forward(200)
pencil.down()

for eye in range(360):
    pencil.forward(1)
    pencil.right(1)
    
pencil.up()
pencil.goto(150,-200)
pencil.right(90)
pencil.down()

for smile in range(180):
    pencil.forward(1)
    pencil.right(1)

turtle.done()