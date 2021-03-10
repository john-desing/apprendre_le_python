import pygame
import random

class comet (pygame.sprite.Sprite):
    def __init__(self,comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect= self.image.get_rect()
        self.vitesse= random.randint(1,3)
        self.rect.x =random.randint(20,800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        self.son = pygame.mixer.Sound("assets/sounds/meteorite.ogg")
    def  remove(self) :
        self.comet_event.all_comet.remove(self)
        if len(self.comet_event.all_comet)==0:
            print("plus de comet")
            self.comet_event.game.start()



    def fall(self):
        self.rect.y += self.vitesse
        self.son.play()

        if self.rect.y >= 700:
            print("sol")
            self.remove()
            if len(self.comet_event.all_comet)==0:
                print("pluie meteom")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        if self.comet_event.game.check_collision(self,self.comet_event.game.all_players):
            print("jouer toucher")
            self.remove()
            self.comet_event.game.player.domage(5)