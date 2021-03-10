import pygame




class projectile(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.vitesse =10
        self.player=player


        self.image =pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x = player.rect.x +120
        self.origin_image =self.image
        self.angle = 0

        self.rect.y = player.rect.y+80

    def remove(self):
        self.player.all_projectiles.remove(self)
    def move(self):
        self.rect.x += self.vitesse
        self.rotation()
        for monster in  self.player.game.check_collision(self,self.player.game.all_monstres):

            self.remove()
            monster.domage(self.player.attack)





        if  self.rect.x > 1500:
            self.remove()

    def  rotation(self):
        self.angle += 12
        self.rect = self.image.get_rect(center=self.rect.center)
        self.image= pygame.transform.rotozoom(self.origin_image,self.angle,1)
