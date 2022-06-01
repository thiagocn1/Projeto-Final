import pygame
from Candidatos import Candidatos
from configuracoes import *
from os import path
import random
from Animacoes import animacao_vida, animacao_dano
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

#classe animação de dano no personágem
class Efeitodano(pygame.sprite.Sprite):
    #construtor classe
    def __init__(self,posicao):
        pygame.sprite.Sprite.__init__(self)
        
        self.animation_dano=animacao_dano
        
        #para iniciar o processo de animação frame por frame
        self.frame=0
        self.image=self.animation_dano[self.frame]
        self.rect=self.image.get_rect()
        self.rect.center=posicao #posiciona ela na imaagem

        #guarda o tick da primeira imagem
        self.lastupdate=pygame.time.get_ticks()
        
        #tempo para proxima imagem ser mostrada
        self.frame_ticks
    def update(self):
        #verifica o tempo
        now=pygame.time.get_ticks()
        #ve quantos ticks passaram desde o ultimo
        elapsed_tickes=now-self.lastupdate
        #caso já seja para mudar de imagem
        if elapsed_tickes>self.frame_ticks:
            self.lastupdate=now

            #avanca um quadro
            self.frame+=1
            
            # verifica se já chegou no final da animacao
            if self.frame==len(self.animation_dano):
                #se sim acabar com a explosão
                self.kill()
            else:
                #caso contrário troca de imagem
                center = self.rect.center
                self.image = self.animation_dano[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

#classe animação de vida no personágem
class Efeitodano(pygame.sprite.Sprite):
    #construtor classe
    def __init__(self,posicao):
        pygame.sprite.Sprite.__init__(self)
        
        self.animation_vida=animacao_vida
        
        #para iniciar o processo de animação frame por frame
        self.frame=0
        self.image=self.animation_vida[self.frame]
        self.rect=self.image.get_rect()
        self.rect.center=posicao #posiciona ela na imaagem

        #guarda o tick da primeira imagem
        self.lastupdate=pygame.time.get_ticks()
        
        #tempo para proxima imagem ser mostrada
        self.frame_ticks
    def update(self):
        #verifica o tempo
        now=pygame.time.get_ticks()
        #ve quantos ticks passaram desde o ultimo
        elapsed_tickes=now-self.lastupdate
        #caso já seja para mudar de imagem
        if elapsed_tickes>self.frame_ticks:
            self.lastupdate=now

            #avanca um quadro
            self.frame+=1
            
            # verifica se já chegou no final da animacao
            if self.frame==len(self.animation_vida):
                #se sim acabar com a explosão
                self.kill()
            else:
                #caso contrário troca de imagem
                center = self.rect.center
                self.image = self.animation_vida[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



