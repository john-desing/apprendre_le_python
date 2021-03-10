import pygame,random
hauteur= 800
largeur= 500
resol = (hauteur,largeur)
jeton = 100

pygame.init()
#classe pour l'emplacement:
class emplacement (pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load("images/cerise.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y =pos_y
    def set_image(self,image):
        self.image=image

def lancemeent():
            global jeton
            # liste stokantle nom de chaque fruits
            fruits = ['orange', "cerise", 'annas', 'pasteque', 'pomme_dore']
            # probabilité de des fruits
            proba_fruits = [40, 25, 20, 10, 5]
            fruits_dict = {
                "orange": 10, "cerise": 20, "pasteque": 50, "pomme_dore": 100,'annas':25
            }



            # fruit_hasard = random.choices(fruits,k=3)
            # print("fruit:{}-{}-{}".format( fruit_hasard [0],fruit_hasard [1],fruit_hasard [2]))

            choix_fruits = random.choices(fruits, proba_fruits, k=3)
            print(choix_fruits[0], choix_fruits[1], choix_fruits[2])
            # verifier les les fruits:
            fruit_gauche = fruit_dict[choix_fruits[0]]
            fruit_milieux = fruit_dict[choix_fruits[1]]
            fruit_droit = fruit_dict[choix_fruits[2]]

            emplacement_gau.set_image(fruit_gauche)
            emplacement_mil.set_image(fruit_milieux)
            emplacement_droit.set_image(fruit_droit)
            if choix_fruits[0] == choix_fruits[1] == choix_fruits[2]:  # si les trois fuits sont identique
                jetons = fruits_dict[choix_fruits[0]]
                jeton += jetons
        # if choix_fruits
                print("les trois colonne sont complétées par ", choix_fruits[0], " vous avez gagnier ", jetons," jetonns de plus")

# creation de la fenêtre du jeu
pygame.display.set_caption("machine a sou")
screen = pygame.display.set_mode(resol)
#pygame.display.set_gamma((12,15,45))

img_font = pygame.image.load("images/slot.png")

launched=True
hauteur_emplacement = hauteur / 3 #bonjourgdfhjfek
emplacements= pygame.sprite.Group()
emplacement_gau = emplacement(232,hauteur_emplacement)
emplacement_mil = emplacement(332,hauteur_emplacement)
emplacement_droit = emplacement(432,hauteur_emplacement)

emplacements.add(emplacement_gau)
emplacements.add(emplacement_mil)
emplacements.add(emplacement_droit)

fruit_dict= {
    "annas":pygame.image.load('images/ananas.png'),"cerise":pygame.image.load('images/cerise.png'),"pomme_dore":pygame.image.load('images/pomme_dore.png'),
"pasteque":pygame.image.load('images/pasteque.png'),"orange":pygame.image.load("images/orange.png")
}
text= pygame.font.SysFont('Goudy Stout',30)
while launched:
    screen.fill((255, 255, 255))
    screen.blit(img_font, (5, 0))
    emplacements.draw(screen)
    trs=text.render(str(jeton),True,(0,0,0))
    screen.blit(trs,(310,390))
    pygame.display.flip()

    for event in pygame.event.get():
           if event.type == pygame.QUIT:
               launched = False
           if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_SPACE and jeton >=5:
                   print("lancemement")
                   lancemeent()
                   jeton-=5
