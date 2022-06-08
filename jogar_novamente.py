#importando coisas
import pygame
from os import path

from sympy import fps
from Candidatos import Candidatos
from configuracoes import *
import time


def jogar_novamente_screen(screen,condicao,WIDTH, HEIGHT):
    #unidade de tempo
    clock=pygame.time.Clock()
    clock.tick(FPS)
    tempo=0
    #para ficar parado 60s
    while tempo<60:
        tempo+=1
        #carregar o fundo da tela de menu
        if condicao==VITORIA:
            Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
            Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))

            #primeira tela final
            screen.fill((0,0,0))
            screen.blit(Derrota_small,(0,0))
            pygame.display.update()
        elif condicao==EMPATE:
            Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
            Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))

            #segunda tela final
            screen.fill((0,0,0))
            screen.blit(Derrota_small,(0,0))
            pygame.display.update()

        else:
            Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
            Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))

            #terceira tela de final
            screen.fill((0,0,0))
            screen.blit(Derrota_small,(0,0))
            pygame.display.update()
    return ENCERRAR
