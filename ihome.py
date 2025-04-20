import pgzrun

WIDTH = 500
HEIGHT = 300

sm=Actor("hulk.jpg")
sm.pos=100,100

def draw():
    screen.fill("dark green")
    sm.draw()

pgzrun.go()