
import pygame
from os import path
from configuracoes import * 
from Candidatos import Candidatos
from Classes import Contra, Player

def luta_screen(window,personagem):
    #unidade de tempo
    clock=pygame.time.Clock()
    
    all_sprites=pygame.sprite.Group()
    all_player=pygame.sprite.Group()
    all_contra=pygame.sprite.Group()
    groups={}
    groups['all_sprites']=all_sprites
    groups['all_players']=all_player
    groups['all_contra']=all_contra
    
    #criar jogador
    player=Player(personagem)
    lista=['Lula','Ciro','Moro','Bolsonaro','Doria']
    contra=Contra(lista)

    #carregar o fundo da tela de luta
    tela_fundo=pygame.image.load(path.join(IMG_DIR, 'palacio.png')).convert()
    tela_fundo_small=pygame.transform.scale(tela_fundo,(WIDTH,HEIGHT))
    tela_fundo_rect = tela_fundo_small.get_rect()



    #----Loop principal-----
    rodando=True
    while rodando:

        
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
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

            




        	#-------gerando saidas-----
        BLACK=(0,0,0)
        window.fill(BLACK)
        window.blit((tela_fundo_small),(0,0))
        window.blit(player.image_small,player.rect)
        window.blit(contra.image_small,contra.rect)
        

    


        pygame.display.update()#atualizar frames


