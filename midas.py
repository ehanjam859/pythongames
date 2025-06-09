import pygame

pygame.init()

WITDH= 800
HEIGHT= 600

screen=pygame.display.set_mode((WITDH,HEIGHT))
pygame.display.set_caption("MIDAS")

gameloop=True

squarepostison=(500,350,20,20)
square1=pygame.draw.rect(screen,"blue",squarepostison)

square2position=(300,350,20,20)
square2=pygame.draw.rect(screen,"blue",square2position)

square3position=(300,150,20,20)
square3=pygame.draw.rect(screen,"blue",square3position)

square4position=(500,150,20,20)
square4=pygame.draw.rect(screen,"blue",square4position)

midas_x=400
midas_y=300

midasposition=(midas_x,midas_y,20,20)
midas=pygame.draw.rect(screen,"lime",midasposition)

midas_dx=0
midas_dy=0

speed=20
FPS=20
clock=pygame.time.Clock()

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            midas_dx=0
            midas_dy=speed*1
        if event.key == pygame.K_UP:
            midas_dx=0
            midas_dy=speed*-1
        if event.key == pygame.K_RIGHT:
            midas_dx=speed*1
            midas_dy=0
        if event.key == pygame.K_LEFT:
            midas_dx=speed*-1
            midas_dy=0

    midas_x=midas_x+midas_dx
    midas_y=midas_y+midas_dy
    midasposition=(midas_x,midas_y,20,20)

    if midas.colliderect(square1):
        square1.color("gold")

    if midas.colliderect(square2):
        square2.color("gold")

    if midas.colliderect(square3):
        square3.color("gold")

    if midas.colliderect(square4):
        square4.color("gold")

    screen.fill("black")
    midas=pygame.draw.rect(screen,"lime",midasposition)
    square1=pygame.draw.rect(screen,"blue",squarepostison)
    square2=pygame.draw.rect(screen,"blue",square2position)
    square3=pygame.draw.rect(screen,"blue",square3position)
    square4=pygame.draw.rect(screen,"blue",square4position)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()