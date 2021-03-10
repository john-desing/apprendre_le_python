import pygame
resol=(650,650)
color = ( 151, 44, 200)
color1 = ( 11, 44, 20)
color2=(0,0,0)
pygame.init()
pygame.display.set_caption("john",)
#pygame.display.set_gamma((12,15,45))
screen = pygame.display.set_mode(resol,pygame.RESIZABLE)
arial_font = pygame.font.SysFont("arial",60,False,True)
dimension_text = arial_font.render("{}".format(resol),True,color1)
screen.blit(dimension_text,(10,10))
pygame.display.flip()
launched=True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.VIDEORESIZE:
            screen.fill(color2)
            dimension_text = arial_font.render("{}x{}".format(event.w,event.h), True, color1)
            screen.blit(dimension_text, [10,10])
            pygame.display.flip()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print("HAUT")

            elif event.key == pygame.K_DOWN:
                    print("BAS")
            elif event.key == pygame.K_RIGHT:
                    print("Droite")
            elif event.key == pygame.K_LEFT:
                    print("Gauche")

            else:
                print("autre touche....")
