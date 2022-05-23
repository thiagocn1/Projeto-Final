#importar todas as outras bibliotecas
import pygame
import random
from Menu import menu_screen
from luta import luta_screen


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

Status=LUTA

while Status != ENCERRAR:
    if Status==MENU:
        
        Status=menu_screen(window)
    elif Status==LUTA:
        Status= luta_screen(window,'lula')
    else:
        Status= ENCERRAR
#sair do jogo
pygame.quit()
