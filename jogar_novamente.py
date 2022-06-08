#importando coisas
import pygame
from os import path

from sympy import fps
from Candidatos import Candidatos
from configuracoes import *
import time
from Classes import Button
import os
pygame.mixer.init()



def jogar_novamente_screen(screen,condicao,WIDTH, HEIGHT):
    #unidade de tempo
    clock=pygame.time.Clock()
    saida = ENCERRAR

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
    tempo=0
    while rodando:
        clock.tick(60)
        screen.fill((0,0,0))
        #carregar o fundo da tela de menu
        if condicao==VITORIA:
            
            Vitoria=pygame.image.load(path.join(IMG_DIR, 'Vitoria.png')).convert()
            Vitoria_small = pygame.transform.scale(Vitoria, (WIDTH, HEIGHT))

            #primeira tela final
            screen.fill((0,0,0))
            screen.blit(Vitoria_small,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando=False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        rodando= False
                    if event.key == pygame.K_RETURN:
                        saida =  MENU
                        rodando = False
        
        elif condicao==EMPATE:
            Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
            Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando=False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        rodando= False
                    if event.key == pygame.K_RETURN:
                        saida =  MENU
                        rodando = False

            #segunda tela final
            screen.fill((0,0,0))
            screen.blit(Derrota_small,(0,0))
            pygame.display.update()

        else:
            Derrota=pygame.image.load(path.join(IMG_DIR, 'GameOver.png')).convert()
            Derrota_small = pygame.transform.scale(Derrota, (WIDTH, HEIGHT))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando=False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        rodando= False
                    if event.key == pygame.K_RETURN:
                        saida =  MENU
                        rodando = False

            #terceira tela de final
            screen.fill((0,0,0))
            screen.blit(Derrota_small,(0,0))
            pygame.display.update()
    return saida

