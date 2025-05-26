import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("initials")
gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    screen.fill("black")
    rect1=pygame.draw.rect(screen,"red",(100,100,50,200))
    rect2=pygame.draw.rect(screen,"red",(100,200,100,50))
    rect3=pygame.draw.rect(screen,"red",(200,100,50,200))
    
       
    pygame.display.flip()

pygame.quit()