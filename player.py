import pygame
from projectil import projectile
import animation
# CREATION CLASSE JOUER
class player (animation.AnimateSprite):

    def __init__(self,game):
        super().__init__('player')
        self.game=game
        self.vie = 150
        self.max_vie = 150
        self.attack = 20
        self.vitesse = 5
        self.son = pygame.mixer.Sound("assets/sounds/tir.ogg")
        self.all_projectiles=pygame.sprite.Group()


        self.rect = self.image.get_rect()
        self.rect.x= 500
        self.rect.y = 600
    def launch_projectile(self):
        self.start_animation()
        self.son.play()

        self.all_projectiles.add(projectile(self))

    def deplacement_droite(self):


        if not self.game.check_collision(self,self.game.all_monstres):
            self.rect.x += self.vitesse
    def deplacement_gauche(self):
        self.rect.x -= self.vitesse

    def char_bar_vie(self, surface):

        pygame.draw.rect(surface, (63, 60, 60), [self.rect.x + 20, self.rect.y + 10, self.max_vie, 7])
        pygame.draw.rect(surface, (111, 210, 45),[self.rect.x + 20, self.rect.y +10, self.vie, 7])
    def domage(self,amount):

        if self.vie - amount > amount:
            self.vie -= amount
        else:
            self.game.game_over()
    def update_animation(self):
        self.animat()