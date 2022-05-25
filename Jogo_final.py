#importar todas as outras bibliotecas
import pygame
import random
from Menu import menu_screen
from luta import luta_screen
from configuracoes import *

pygame.init()

#-------Gera tela de jogo
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pokecrias')

#mudar telas vai ser negocio do while

Status=MENU

while Status != ENCERRAR:
    if Status==MENU: 
        Status, nome =menu_screen(window,WIDTH,HEIGHT)
        player=Status
    elif Status==LUTA:
        Status= luta_screen(window,nome)
    else:
        Status= ENCERRAR
#sair do jogo
pygame.quit()
