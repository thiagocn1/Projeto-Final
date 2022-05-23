
import pygame
from os import path
from configurações import IMG_DIR 
import time

def luta_screen(window,personagem):
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
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    i=1
                    print(i)
                if event.key==pygame.K_2:
                    i=2
                    print(i)
                if event.key==pygame.K_3:
                    i=3
                    print(i)
                if event.key==pygame.K_4:
                    i=4
                    print(i)


            if event.type==pygame.KEYUP:
                rodando=False
            




        	#-------gerando saidas-----
        BLACK=(0,0,0)
        window.fill(BLACK)
        window.blit((tela_fundo),(0,0))
    


        pygame.display.update()#atualizar frames


