import pygame
from player import player
from monstre import Monstre, Mummy,Alien
from comet_event import CometFallEvent
class Game:
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.son = pygame.mixer.Sound("assets/sounds/game_over.ogg")
        self.player = player(self)
        self.all_players.add(self.player)
        self.commet_event = CometFallEvent(self)
        self.all_monstres=pygame.sprite.Group()
        self .pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monstre(Mummy)
        self.spawn_monstre(Mummy)
        self.spawn_monstre(Alien)
    def game_over(self):
        self.all_monstres= pygame.sprite.Group()
        self.commet_event.all_comet= pygame.sprite.Group()
        self.player.vie= self.player.max_vie
        self.commet_event.reset_percent()
        self.son.play()
        self.is_playing = False
    def update(self,screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.char_bar_vie(screen)
        self.commet_event.update_bar(screen)
        self.player.update_animation()


        for projectile in self.player.all_projectiles:
            projectile.move()
        for monstre in self.all_monstres:
            monstre.forward()
            monstre.char_bar_vie(screen)
            monstre.update_animation()


            self.player.all_projectiles.draw(screen)  # charger le joueur

        for comet in self.commet_event.all_comet:
            comet.fall()

        self.all_monstres.draw(screen)
        self.commet_event.all_comet.draw(screen)
        # VERIVIER LE DEPLACEMENT
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1200:
            self.player.deplacement_droite()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.deplacement_gauche()


    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    def spawn_monstre(self,monster_class_name):

        self.all_monstres.add(monster_class_name.__call__(self))