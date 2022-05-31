import pygame
from Candidatos import Candidatos
from configuracoes import *
from os import path
import random

#Classe do personagem controlado 
class Player(pygame.sprite.Sprite):
    def __init__(self,nome):
        pygame.sprite.Sprite.__init__(self)
        nois=Candidatos[nome]['imagem']
        self.image=pygame.image.load(path.join(IMG_DIR,nois)).convert_alpha()
        self.image_small=pygame.transform.scale(self.image,(125,125))
        self.rect=self.image_small.get_rect()
        self.nome=nome
        self.movimentos=Candidatos['{}'.format(nome)]['movimentos']
        self.ataque=Candidatos['{}'.format(nome)]['ataque'] 
        self.hp=Candidatos['{}'.format(nome)] ['hp']  #quanto de vida ele tem
        self.rect.centerx= 100
        self.rect.centery= 125

    #luta entre dois casas quando escolher um ataque
    def atacar(self,i):
        dano_ataque=Candidatos[self.nome]['movimentos'][i][1]
        return dano_ataque


        




#Classe do personagem que vai lutar contra
class Contra(pygame.sprite.Sprite):
    def __init__(self,lista):
        pygame.sprite.Sprite.__init__(self)
        i=random.randint(0,4)
        nome=lista[i]
        nois=Candidatos[nome]['imagem']
        self.image=pygame.image.load(path.join(IMG_DIR,nois)).convert_alpha()
        self.image_small=pygame.transform.scale(self.image,(125,125))
        self.rect=self.image_small.get_rect()
        self.nome=nome
        self.movimentos=Candidatos['{}'.format(nome)]['movimentos']
        self.ataque=Candidatos['{}'.format(nome)]['ataque'] 
        self.hp=Candidatos['{}'.format(nome)] ['hp']  #quanto de vida ele tem
        self.rect.centerx= 500
        self.rect.centery= 125
    def ataque_contra(self):
        i=random.randint(0,3)
        dano_ataque=Candidatos[self.nome]['movimentos'][i][1]
        return dano_ataque,i