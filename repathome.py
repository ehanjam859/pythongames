import pgzrun

WIDTH = 400
HEIGHT = 400


def draw():

    w=300
    h=200

    for i in range(20):
        r=Rect((0,0),(w,h))
        r.center=(150,150)
        screen.draw.rect(r,"green")

        w=w+10
        h=h-10

pgzrun.go()