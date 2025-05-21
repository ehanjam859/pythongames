import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("initials")
rect1=pygame.draw.rect(screen,"orange",(100,100,100,30))
rect2=pygame.draw.rect(screen,"orange",(100,100,10,200))
rect3=pygame.draw.rect(screen,"orange",(100,150,100,50))
gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    screen.fill("black")
    rect1=pygame.draw.rect(screen,"orange",(100,100,100,50))
    rect2=pygame.draw.rect(screen,"orange",(100,100,40,250))
    rect3=pygame.draw.rect(screen,"orange",(100,200,100,50))
    rect4=pygame.draw.rect(screen,"orange",(100,300,100,50))
    rect5=pygame.draw.rect(screen,"orange",(300,100,150,50))
    rect6=pygame.draw.rect(screen,"orange",(355,100,40,250))
    rect7=pygame.draw.rect(screen,"orange",(275,300,100,50))
    rect8=pygame.draw.rect(screen,"orange",(275,250,50,100))
    
    pygame.display.flip()

pygame.quit()

