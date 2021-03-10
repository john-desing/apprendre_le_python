import pygame
import random
import animation

""" la notion de monstre"""
class Monstre(animation.AnimateSprite):
    def __init__(self,game,name="Alien",size=(125,125),offset=0):
        super().__init__(name,size)
        self.game=game
        self.vie = 100
        self.vie_max =100
        self.attack =0.3
        self.rect = self.image.get_rect()
        self.rect.x=1000 + random.randint(0,350)
        self.rect.y = 650- offset
        self.vitesse = random.randint(1,3)
        self.start_animation()
        self.pointsr=0


    def domage(self,amount):
        self.vie -= amount
        if self.vie < 0:


            self.rect.x =1500 + random.randint(0,350)

            self.vie =self.vie_max
            if self.game.commet_event.is_full_loaded():
                self.game.all_monstres.remove(self )
                self.game.commet_event.attempt_fall()
    def update_animation(self):
        self.animat(loop=True)
    def char_bar_vie(self,surface):

        position_jauge_vie= [self.rect.x +10,self.rect.y -10,self.vie,5]
        arr_jauge_vie = [self.rect.x + 10, self.rect.y - 10, self.vie_max, 5]

        pygame.draw.rect(surface, (63,60,60), arr_jauge_vie)
        pygame.draw.rect(surface,(111,210,45),position_jauge_vie)

    def forward(self):
        if not  self.game.check_collision(self,self.game.all_players):
            self.rect.x -=self.vitesse
        else:
            self.game.player.domage(self.attack)
class Mummy(Monstre):
    def __init__(self,game):
        super().__init__(game,"mummy",(130,130))
        self.points = 0

class Alien(Monstre):
    def __init__(self,game):
        super().__init__(game,"alien",(300,300),150)
        self.vie =250
        self.vie_max=250
        self.attack = 2# ATAQUE






