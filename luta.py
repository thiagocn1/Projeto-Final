
import pygame
from os import path
from configuracoes import * 
from Candidatos import Candidatos
from Classes import Contra, Player
import time

def luta_screen(window,personagem):
    #unidade de tempo
    clock=pygame.time.Clock()
    clock.tick(60)
    
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
    while rodando:
        ataque_script = None

        
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    dano=player.atacar(1)
                    #colocar mensagem quando atacar
                    i=0
                    ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][i][2]
                    text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                    #tirar vida adiversário
                    contra.hp-=dano


                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    #colocar mensagem que o adversário atacou

                elif event.key==pygame.K_2:
                    dano=player.atacar(2)
                    #colocar mensagem quando atacar
                    i=1
                    ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][i][2]
                    text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                    #tirar vida adiversário
                    contra.hp-=dano

                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    #colocar mensagem que o adversário atacou

                elif event.key==pygame.K_3:
                    dano=player.atacar(3)
                    #colocar mensagem quando atacar
                    i=2
                    ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][i][2]
                    text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))

                    #tirar vida adiversário
                    contra.hp-=dano

                    dano_contra=contra.ataque_contra()
                    player.hp-=dano_contra
                    #colocar mensagem que o adversário atacou

                elif event.key==pygame.K_4:
                    dano=player.atacar(4)
                    #colocar mensagem quando atacar
                    i=3
                    ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][i][2]
                    text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                    #tirar vida adiversário
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
        #vida do player
        pygame.draw.polygon(window, BLACK, [(30, 10), (130, 10), (130, 30), (30, 30)])
        pygame.draw.polygon(window, (0,128,0), [(30, 10), ((player.hp+30), 10), ((player.hp+30), 30), (30, 30)])
        #vida do contra
        pygame.draw.polygon(window, BLACK, [(470, 10), (570, 10), (570, 30), (470, 30)])
        pygame.draw.polygon(window, (0,128,0), [(470, 10), ((player.hp+470), 10), ((player.hp+470), 30), (470, 30)])

         
        #dando print nos nomes de ataque e caixa ataque
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
        if ataque_script!=None:
            ataque_rect_pos=(30,(HEIGHT-70))
            window.blit(text_ataque,ataque_rect_pos)
            pygame.display.update()#atualiza frame com a escritura
            time.sleep(1)
        if player.hp<=0 or contra.hp<=0:
            return ENCERRAR

