import pygame
import random
""""
@Auteur: john medy
"""
class panier (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.points = 2 # nombre de points qu'aura le joueur
        self.maximum_points = 250
        self.vitesse = 7
        self.image = pygame.image.load("assets_cho/panier.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 320
        self.pressed={}

    def ajouter_points(self):
        if self.points + 5 <= self.maximum_points:  # limite de points
            print("+5 points")
            self.points += 50
            text2 = str(counteur).rjust(4) if counteur > 0 else 'boom!'

        # methode enlever 2 points

    def enlever_points(self):
        if self.points - 2 > 0:
            print("-2 points")
            self.points -= 10
           # text2 = str(counteur).rjust(4) if counteur > 0 else 'predu!'
        else:
            # perdu
            print("Perdu")

    def deplacement_droite(self):
        if self.rect.x <= 700:
           self.rect.x += self.vitesse
    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.vitesse

    def update_bar(self, screen):

        pygame.draw.rect(screen, (0, 1, 1), [0, screen.get_height() - 20, screen.get_width(), 20])
        pygame.draw.rect(screen, (87, 64,54),
                         [0, screen.get_height() - 20, self.points * 3 - 20, 20])





class Ouefs (pygame.sprite.Sprite):
    def __init__(self,panier):
        super().__init__()

        self.vites = random.randint(1,4)
        self.image = pygame.image.load("assets_cho/carrot.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(10,800)
        self.rect.y = - random.randint(10,800)
        self.panier = panier
        self.panier_group = pygame.sprite.Group()
        self.panier_group.add(self.panier)



    def remove(self) :
        self.rect.x = random.randint(10, 800)
        self.rect.y = - random.randint(10, 800)


        print("chocola supprimé")


    def chute(self):
        self.rect.y += self.vites

        if self.rect.y >= 400:
            print(" Oeuf au sol")
            self.remove()
            self.panier.enlever_points()
        if pygame.sprite.spritecollide(self,self.panier_group,False,pygame.sprite.collide_mask)and self.rect.y >= 360:
            print("colision",self.rect.y)
            self.panier.ajouter_points()
            self.remove()



resol = (800,480)
pygame.init()



# creation de la fenêtre du jeu
pygame.display.set_caption("fête du chocolat")
screen = pygame.display.set_mode(resol)

img_font = pygame.image.load('assets_cho/fond.jpg')
sol = pygame.image.load("assets_cho/sol.png")
temps=pygame.time.Clock()
counteur, text= 30,'30'.rjust(3)
counteur, text3= 30,'30'.rjust(3)
# charger la barre de chocolat
bar_chocolat = pygame.image.load('assets_cho/chocolate.png')

# redimentionner
bar_chocolat = pygame.transform.scale(bar_chocolat, (60, 60))
pygame.time.set_timer(pygame.USEREVENT,1000)
if __name__ == '__main__':
    font= pygame.font.SysFont("consolas",40)
panier = panier()

print(panier.points)

ouefs=pygame.sprite.Group()
ouefs.add(Ouefs(panier))
ouefs.add(Ouefs(panier))
ouefs.add(Ouefs(panier))
ouefs.add(Ouefs(panier))
#

panier.points,text2 = panier.points,'50'.rjust(3)
panier.points,text4 = panier.points,'points:'.rjust(3)
panier.points,text1 = panier.points,'vie:'.rjust(3)
panier.points,text5 = panier.points,'VOUS AVEZ GAGNIER!(:'.rjust(3)
panier.points,text6 = panier.points,'VOUS AVEZ perdu!):'.rjust(3)

launched=True
while launched:

    for oeuf in ouefs:
     oeuf.chute()



    if panier.pressed.get(pygame.K_RIGHT) and panier.rect.x < 710 :
        panier.deplacement_droite()
    elif panier.pressed.get(pygame.K_LEFT)and panier.rect.x > -10:
        panier.deplacement_gauche()

    screen.blit(img_font, (0, 0))
    screen.blit(sol, (0, 0))
    screen.blit(font.render(text,True,(240,20,45)),(40,10))
    screen.blit(font.render(text1, True, (240, 20, 45)), (0, 10))
    if panier.points  >= 250  and int(text) >= 0 :
     screen.blit(font.render(text5, True, (240, 20, 45)), (300, 250))
    if panier.points <= 250 and int(text) <= 0:
        screen.blit(font.render(text6, True, (240, 20, 45)), (300, 250))
    screen.blit(font.render(text3, True, (240, 41, 145)), (700, 10))
    screen.blit(font.render(text4, True, (240, 41, 145)), (550, 10))
    screen.blit(panier.image,panier.rect)
    #screen.blit(choco.image,choco.rect)
    screen.blit(bar_chocolat, (( panier.points * 3 - 20) - bar_chocolat.get_width() / 2, 420))
    ouefs.draw(screen)
    panier.update_bar(screen)
    pygame.display.flip()
    temps.tick(60)

    for event in pygame.event.get():
           if event.type == pygame.QUIT:
               launched = False
           elif event.type == pygame.KEYDOWN:
               panier.pressed[event.key]=True
           elif event.type == pygame.KEYUP:
               panier.pressed[event.key]=False
           elif event.type ==(pygame.USEREVENT):
               counteur -=1
               text=str(counteur).rjust(4)if counteur > 0 else '0'
               text3 = str(panier.points).rjust(2) if panier.points > 0 else '0'



