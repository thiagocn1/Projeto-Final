#importando coisas
import pygame
from os import path
from configurações import IMG_DIR
import time

def menu_screen(screen,WIDTH, HEIGHT):
    #unidade de tempo
    clock=pygame.time.Clock()
    clock.tick(60)

    #carregar o fundo da tela de menu
    fundo1=pygame.image.load(path.join(IMG_DIR, 'Warning.png')).convert()
    fundo2 = pygame.image.load(path.join(IMG_DIR, 'Imagemfundo.png')).convert()
    fundo1_small = pygame.transform.scale(fundo1, (WIDTH, HEIGHT))
    fundo2_small = pygame.transform.scale(fundo2, (WIDTH, HEIGHT))
    tela_fundo1_rect = fundo1.get_rect()
    tela_fundo2_rect = fundo2.get_rect()


    screen.fill((0,0,0))
    screen.blit(fundo1_small,(0,0))
    pygame.display.update()
    time.sleep(5)





    continuar = True
    while continuar:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuar = False
            
        
        screen.fill((0,0,0))
        screen.blit(fundo2_small,(0,0))

        pygame.display.update()
        
            

    return lista
#players



class escolha(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0

