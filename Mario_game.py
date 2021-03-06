import time
import random
import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load('image_chome/' + sprite_name +'.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animat(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop == False:
                    self.animation = False
            self.image = self.images[self.current_image]


def load_animate_images(sprite_name):
    images = []
    path = 'image_chome/'+ sprite_name
    for num in range(1, 5):
        imag_path = path + str(num) + '.png'
        images.append(pygame.image.load(imag_path))
    return images


animations = { 'jouer': load_animate_images('jouer') }
class jouer (AnimateSprite):
    def __init__(self):
        super().__init__('jouer')

        self.points = 2 # nombre de points qu'aura le joueur
        self.maximum_points = 250
        self.vitesse = 7
        self.image = pygame.transform.scale(self.image,(400,400))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 40
        self.pressed={}
        self.saut_montee=0
        self.saut_descente=5
        self.saut=0
        self.a_sauter= False
        self.nombre_de_saut =0

    def ajouter_points(self):
        if self.points + 5 <= self.maximum_points:  # limite de points
            print("+5 points")
            self.points += 50

        # methode enlever 2 points

    def enlever_points(self):
        if self.points - 2 > 0:
            print("-2 points")
            self.points -= 10

        else:
            # perdu
            print("Perdu")

    def update_animation(self):
        self.animat()

    def deplacement_droite(self):
        self.rect.x += self.vitesse
        self.start_animation()

    def deplacement_gauche(self):
        self.rect.x -= self.vitesse
        self.start_animation()
    def sauter (self):

        if self.a_sauter:
            if self.saut_montee >= 10:
                self.saut_descente -= 1
                self.saut =self.saut_descente
            else:
                self.saut_montee += 1
                self.saut=self.saut_montee
            if self.saut_descente < 0:
                self.saut_descente = 5
                self.saut_montee = 0
                self.a_sauter = False
        self.rect.y= self.rect.y-(10*(self.saut/2))

        self.image = pygame.image.load('image_chome/jouer2.png')



class Obstacle (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.vie = 100
        self.vie_max =100
        self.attack =0.3
        self.image= pygame.image.load("image_mario/fondEcran.png")
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y =0
        self.vitesse = 3
    def deplace(self):
        self.rect.x -= self.vitesse
    def remove(self) :
        if self.rect.x < -1000:
         self.rect.x = random.randint(1000, 1500)






resol = (800,340)
pygame.init()
temps = pygame.time.Clock()

# creation de la fenêtre du jeu
pygame.display.set_caption("mario game")
screen = pygame.display.set_mode(resol)
sol = pygame.image.load("assets_cho/sol.png")

#pygame.display.set_gamma((12,15,45))

img_font = pygame.image.load("image_mario/fondEcran.png")

banner_rect= img_font.get_rect()

fond_x = 0
jouer = jouer()
obs = Obstacle()
obstac = pygame.sprite.Group()
obstac.add(Obstacle())
obstac.add(Obstacle())
launched=True

while launched:
    for obstacle in obstac:
     obstacle.deplace()
     obstacle.remove()

    jouer.update_animation()
    if jouer.pressed.get(pygame.K_RIGHT) and jouer.rect.x < 9999 :
        jouer.deplacement_droite()



    elif jouer.pressed.get(pygame.K_LEFT)and jouer.rect.x > 0:
        jouer.deplacement_gauche()


    elif jouer.pressed.get(pygame.K_SPACE) :
        jouer.a_sauter=True
        jouer.nombre_de_saut +=1
        jouer.sauter()

    temps.tick(30)
    fond_x = 1
    if fond_x < 940:
        fond_x =0


    screen.fill((255, 255, 255))
    screen.blit(sol, (0, 20))



    #screen.blit(obs.image, obs.rect)


    screen.blit(img_font, banner_rect)
    #
    obstac.draw(screen)

    screen.blit(jouer.image, (10, 100))




    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            jouer.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            jouer.pressed[event.key] = False
