#importar todas as outras bibliotecas
import pygame
import random
from Menu import menu_screen
import luta

pygame.init()

#-------Gera tela de jogo
WIDTH=1220
HEIGHT=820
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pokecrias')

#mudar telas vai ser negocio do while
MENU=0
LUTA=1
ENCERRAR=2

Status=MENU

while Status != ENCERRAR:
    if Status==MENU: 
        Status=menu_screen(window,WIDTH,HEIGHT)
        player=Status
    elif Status!=MENU and Status!=ENCERRAR:
        Status= luta.luta_screen(window,player)
    else:
        Status= ENCERRAR
#sair do jogo
pygame.quit()
