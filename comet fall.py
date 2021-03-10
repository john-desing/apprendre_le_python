import pygame
from projectil import projectile
from game2 import  Game
from  monstre import Mummy,Alien,Monstre
resol = (1080,750)
pygame.init()
pygame.mixer.init()
temps = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,1000)
FPS =60
counteur, text= 1,'30'.rjust(3)
cont, text1= 30,'30'.rjust(3)
font= pygame.font.SysFont("consolas",40)
# creation de la fenêtre du jeu
pygame.display.set_caption("comette  fall Game")
screen = pygame.display.set_mode(resol,pygame.RESIZABLE)
#pygame.display.set_gamma((12,15,45))

img_font = pygame.image.load("assets/bg.jpg")
banner = pygame.image.load("assets/banner.png")
banner=pygame.transform.scale(banner,(500,500))
banner_rect= banner.get_rect()
banner_rect.x= screen.get_width()/4

play_button = pygame.image.load("assets/button.png")
play_button =pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x=screen.get_width()/3
play_button_rect.y=screen.get_height()/2
# pour les sons:
son_clic = pygame.mixer.Sound("assets/sounds/click.ogg")

game=Game()


launched=True

while launched:

    screen.fill((255, 255, 255))
    screen.blit(img_font, (0,-100))

    if game.is_playing:
        game.update(screen)

        screen.blit(font.render(text, True, (240, 20, 45)), (200, 10))
        screen.blit(font.render(text1, True, (240, 20, 45)), (0, 10))



    else:

        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    temps.tick(FPS)
    pygame.display.flip()
    for event in pygame.event.get():
           if event.type == pygame.QUIT:
               launched = False
           elif event.type == pygame.KEYDOWN:
               game.pressed[event.key] = True
               if event.key == pygame.K_SPACE:
                   game.player.launch_projectile()
           elif event.type == pygame.KEYUP:
               game.pressed[event.key] = False
           elif event.type == pygame.MOUSEBUTTONDOWN:
               if play_button_rect.collidepoint(event.pos):
                   game.start()
                   son_clic.play()
           elif event.type ==(pygame.USEREVENT):
               counteur += 1
               text = str(counteur).rjust(4) if counteur > 0 else '0'



               cont+= 4

               text1 = str(cont).rjust(4) if cont > 0 else '0'







