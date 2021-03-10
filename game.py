import pygame
resol=(650,650)
color = ( 151, 44, 200)
color1 = ( 11, 44, 20)

pygame.init
clock = pygame.time.Clock

pygame.display.set_caption("john",)
#pygame.display.set_gamma((12,15,45))
screen = pygame.display.set_mode(resol,pygame.RESIZABLE)
screen.fill(color)

print(pygame.get_sdl_version())
pygame.draw.circle(screen,color1,[250,200],150,3)
pygame.draw.circle(screen,color1,[350,250],150,3)
pygame.draw.rect(screen,color1,rect=(200,100,300,300),width=2)
pygame.draw.rect(screen,color1,rect=(100,50,300,300),width=2)
pygame.draw.line(screen,color1,(100,50),(200,100),width=2)
pygame.draw.line(screen,color1,(400,350),(500,400),width=2)
pygame.draw.line(screen,color1,(100,350),(200,400),width=2)
pygame.draw.line(screen,color1,(400,50),(500,100),width=2)
pygame.draw.polygon(screen,color1,([250,350],[100,50],[400,50]),width=2)
pygame.display.flip()
launched= True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    #clock.tick()
    print(f"{clock.get_fps()}FPS")

