#importando coisas
import pygame
from os import path

from sympy import fps
from Candidatos import Candidatos
from configuracoes import *
import time
from Classes import Button

def jogar_novamente_screen(screen,condicao,WIDTH, HEIGHT):
    #unidade de tempo
    clock=pygame.time.Clock()


    #carrega botões
    sair_img = pygame.image.load(path.join(IMG_DIR,'Sair.png')).convert_alpha()
    jogarnv_img = pygame.image.load(path.join(IMG_DIR,'Jogar_novamente.png')).convert_alpha()

           
            
        
    sair_button = Button(100,200,sair_img,0.5)
    jogarnv_button = Button(100,300,jogarnv_img,0.5)

    Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
    Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))
    Vitoria=pygame.image.load(path.join(IMG_DIR, 'Vitoria.png')).convert()
    Vitoria_small = pygame.transform.scale(Vitoria, (WIDTH, HEIGHT))


    rodando = True
    while rodando:
        clock.tick(60)
        screen.fill((0,0,0))
        if condicao == VITORIA:
            screen.blit(Vitoria_small,(0,0))
            sair_button.draw(screen)
            jogarnv_button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Status = ENCERRAR
                    rodando = False
                if sair_button.click() == True:
                    Status = ENCERRAR
                    rodando = False
                if jogarnv_button.click() == False:
                    Status = MENU
                    rodando = False
            
            
        if condicao == DERROTA or condicao == EMPATE:
            screen.blit(Derrota_small,(0,0))
            sair_button.draw(screen)
            jogarnv_button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Status = ENCERRAR
                    rodando = False
                if sair_button.click() == True:
                    Status = ENCERRAR
                    rodando = False
                if jogarnv_button.click() == False:
                    Status = MENU
                    rodando = False
    

    return Status
        

        #carregar o fundo da tela de menu
'''if condicao==VITORIA:
            Derrota=pygame.image.load(path.join(IMG_DIR, 'Vitoria.png')).convert()
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
            pygame.display.update()'''

