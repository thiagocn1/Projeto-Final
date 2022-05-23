#importar todas as outras bibliotecas
from tkinter import Menu
import pygame
from Menu import menu_screen
from luta import luta_screen

pygame.init()
pygame.mixer.init()

#-------Gera tela de jogo
WIDTH=600
HEIGHT=400
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pokecrias')

#mudar telas vai ser negocio do while
MENU=0
LUTA=1
ENCERRAR=2

Status=MENU

while Status != ENCERRAR:
    if Status==MENU:
        state=menu_screen(window)
    elif state==LUTA:
        state= luta_screen(window)
    else:
        state= ENCERRAR
#sair do jogo
pygame.quit()
