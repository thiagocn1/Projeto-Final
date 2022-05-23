
import pygame
from os import path
from configurações import IMG_DIR 

def luta_screen(window):
    #unidade de tempo
    clock=pygame.time.Clock()
    HEIGHT=400
    WIDTH=600

    #carregar o fundo da tela de luta
    tela_fundo=pygame.image.load(path.join(IMG_DIR, 'palacio.png')).convert()

    tela_fundo_rect = tela_fundo.get_rect()


    #----Loop principal-----
    rodando=True
    while rodando:
        
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if event.type==pygame.KEYUP:
                rodando=False
            




        	#-------gerando saidas-----
        BLACK=(0,0,0)
        window.fill(BLACK)
        window.blit((tela_fundo),(0,0))
    


        pygame.display.update()#atualizar frames


