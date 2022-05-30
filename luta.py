
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
    #defininfo adversário
    contra=Contra(lista)

    #carregar o fundo da tela de luta e caixa de ataque
    tela_fundo=pygame.image.load(path.join(IMG_DIR, 'palacio.png')).convert()
    tela_fundo_small=pygame.transform.scale(tela_fundo,(WIDTH,HEIGHT))
    tela_fundo_rect = tela_fundo_small.get_rect()
    caixa_ataques=pygame.image.load(path.join(IMG_DIR, 'caixa_luta.png')).convert_alpha()
    caixa_ataques_small=pygame.transform.scale(caixa_ataques,(WIDTH,HEIGHT/4))  

    #carrega fonte que será utilizado 
    nome_font=pygame.font.Font('assets/font/PressStart2P.ttf',10)


    #defininfo player

    #----Loop principal-----
    rodando=True
    ataque_script = None
    while rodando:

        
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    dano=player.atacar(1)
                    #colocar mensagem quando atacar
                    contra.hp-=dano


                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    print(player.hp)
                    #colocar mensagem que o adversário atacou
                if event.key==pygame.K_2:
                    dano=player.atacar(2)
                    #colocar mensagem quando atacar
                    print(Candidatos['{}'.format(personagem)]['movimentos'][i])
                    ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][i][2]
                    text_surface=nome_font.render("{}".format(ataque),True,(0,0,0))
                    text_rect=text_surface.get_rect()
                    #tirar vida adiversário
                    contra.hp-=dano

                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    #colocar mensagem que o adversário atacou
                if event.key==pygame.K_3:
                    dano=player.atacar(3)
                    #colocar mensagem quando atacar
                    contra.hp-=dano

                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    #colocar mensagem que o adversário atacou
                if event.key==pygame.K_4:
                    dano=player.atacar(4)
                    #colocar mensagem quando atacar
                    contra.hp-=dano

                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    
                    #colocar mensagem que o adversário atacou

            




        	#-------gerando saidas-----
        BLACK=(0,0,0)
        window.fill(BLACK)
       #dando print nos personagens e fundo 
        window.blit((tela_fundo_small),(0,0))
        window.blit(player.image_small,player.rect)
        window.blit(contra.image_small,contra.rect)
        pygame.draw.polygon(window, BLACK, [(0, 0), (100, 0), (100, 20), (20, 0)])
         
        #dando print nos nomes de ataque
        if ataque_script == None:
            window.blit(caixa_ataques_small,(0,(HEIGHT-100)))
            for i in range(0,4):
                ataque=Candidatos['{}'.format(personagem)]['movimentos'][i][0]
                text_surface=nome_font.render("{}".format(ataque),True,(0,0,0))
                text_rect=text_surface.get_rect()
                if i==0:
                    text_rect_pos=(80,(HEIGHT-40))
                    window.blit(text_surface,text_rect_pos)
                elif i==1:
                    text_rect_pos=(360,(HEIGHT-40))
                    window.blit(text_surface,text_rect_pos)
                elif i==2:
                    text_rect_pos=(80,(HEIGHT-70))
                    window.blit(text_surface,text_rect_pos)
                elif i==3:
                    text_rect_pos=(360,(HEIGHT-70))
                    window.blit(text_surface,text_rect_pos)
        else:
            pass
    


        pygame.display.update()#atualizar frames


