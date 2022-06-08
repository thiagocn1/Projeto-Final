#importar 
import pygame
from configuracoes import *





class mapa_player(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        print('veio aqui')
        #falta colocar a imagem
        self.image=pygame.image.load(path.join(IMG_DIR,'jair.webp')).convert_alpha()
        self.image=pygame.transform.scale(self.image,(WIDTH/20,HEIGHT/20))
        self.rect=self.image.get_rect()
        self.rect.centerx= WIDTH-100
        self.rect.centery= HEIGHT-100
        self.vx = 0
        self.vy = 0
    def update(self):
        # Atualização da posição do casa
        self.rect.x += self.vx
        self.rect.y += self.vy


class Rua(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        #falta colocar a imagem
        self.image=pygame.image.load(path.join(IMG_DIR,'Lula.webp')).convert_alpha()
        self.image=pygame.transform.scale(self.image,(WIDTH/20,HEIGHT/20))
        self.rect=self.image.get_rect()
        self.rect.centerx= pos[0]
        self.rect.centery= pos[1]