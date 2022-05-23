#importando coisas
import pygame
from os import path
from configurações import IMG_DIR


def menu_screen(screen):
    #unidade de tempo
    clock=pygame.time.Clock()

    #carregar o fundo da tela de menu
    tela_fundo=pygame.image.load(path.join(IMG_DIR, 'Warning')).convert()
    tela_fundo_rect = tela_fundo.get_rect()


