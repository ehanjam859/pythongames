import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 300

sm=Actor("hulk.png")
sm.pos=100,100
message=""

def draw():
    screen.blit("hulkback.jpg",(0,0))
    sm.draw()
    screen.draw.text(message,center=(400,10),fontsize=25)

def place_sm():
    sm.x=randint(50,WIDTH-50)
    sm.y=randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if sm.collidepoint(pos):
        message="GOOD SHOT"
        place_sm()
    else:
        message="BAD SHOT"
    

pgzrun.go()