
import pygame
from os import path
from configurações import IMG_DIR
FPS=60

def luta_screen(screen):
    #unidade de tempo
    clock=pygame.time.Clock()

    #carregar o fundo da tela de luta
    tela_fundo=pygame.image.load(path.join(IMG_DIR, 'palacio')).convert()
    tela_fundo_rect = tela_fundo.get_rect()


    #----Loop principal-----
    rodando=True
    


    
    pygame.display.update()


