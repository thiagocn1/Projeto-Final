import pygame
from Candidatos import Candidatos
from Jogo_final import WIDTH,HEIGHT
from Candidatos import Candidatos
from configurações import IMG_LULA, IMG_jair

class Player(pygame.sprite.sprite):
    def __init__(self,nome):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=Candidatos[nome]['imagem']
        self.rect=self.image.get_rect()
        self.nome=nome
        self.movimentos=Candidatos['{}'.format(nome)]['movimento']
        self.ataque=Candidatos['{}'.format(nome)]['ataque'] 
        self.hp=Candidatos['{}'.format(nome)] ['hp']  #quanto de vida ele tem
        self.rect.centerx=WIDTH/4
        self.rect.centery=HEIGHT/2

    #luta entre dois casas
    def lutas(self, candidato2):
        while self.hp>0 and candidato2.hp>0:
            candidato2['ataque']