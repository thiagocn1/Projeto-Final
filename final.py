#importando coisas
import pygame
from os import path
from Candidatos import Candidatos
from configuracoes import *
import time


def final_screen(screen,condicao,WIDTH, HEIGHT):
    #unidade de tempo
    clock=pygame.time.Clock()
    clock.tick(60)

    #carregar o fundo da tela de menu
    if condicao==VITORIA:
        Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
        Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))

        #primeira tela de aviso
        screen.fill((0,0,0))
        screen.blit(Derrota_small,(0,0))
        pygame.display.update()
    else:
        Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
        Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))

        #primeira tela de aviso
        screen.fill((0,0,0))
        screen.blit(Derrota_small,(0,0))
        pygame.display.update()
    return ENCERRAR
