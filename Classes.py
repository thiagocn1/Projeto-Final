import pygame
from Candidatos import Candidatos
from configuracoes import *
from os import path


class Player(pygame.sprite.Sprite):
    def __init__(self,nome):
        pygame.sprite.Sprite.__init__(self)
        
        nois=Candidatos[nome]['imagem']
        self.image=pygame.image.load(path.join(IMG_DIR,nois)).convert_alpha()
        self.image_small=pygame.transform.scale(self.image,(200,200))
        self.rect=self.image_small.get_rect()
        self.nome=nome
        self.movimentos=Candidatos['{}'.format(nome)]['movimentos']
        self.ataque=Candidatos['{}'.format(nome)]['ataque'] 
        self.hp=Candidatos['{}'.format(nome)] ['hp']  #quanto de vida ele tem
        self.rect.centerx=WIDTH/4
        self.rect.centery=HEIGHT/2

    #luta entre dois casas
    def ataque(self):
        if self.rect.centerx<900:
            velocidadex=50
        else:
            velocidade=-50
        self.rect.centerx+=velocidadex





class Contra(pygame.sprite.Sprite):
    def __init__(self,nome):
        pygame.sprite.Sprite.__init__(self)

        self.image=Candidatos[nome]['imagem']
        self.rect=self.image.get_rect()
        self.nome=nome
        self.movimentos=Candidatos['{}'.format(nome)]['movimento']
        self.ataque=Candidatos['{}'.format(nome)]['ataque'] 
        self.hp=Candidatos['{}'.format(nome)] ['hp']  #quanto de vida ele tem
        self.rect.centerx=WIDTH*3/4
        self.rect.centery=HEIGHT/2 

