
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
    
    #criar jogador
    player=Player(personagem)
    lista=['Lula','Ciro','Moro','Bolsonaro','Doria']
    #defininfo adversário
    contra=Contra(lista)

    #carregar o fundo da tela de luta e caixa de ataque
    tela_fundo=pygame.image.load(path.join(IMG_DIR, 'palacio.png')).convert()
    tela_fundo_small=pygame.transform.scale(tela_fundo,(WIDTH,HEIGHT))
    caixa_ataques=pygame.image.load(path.join(IMG_DIR, 'caixa_luta.png')).convert_alpha()
    caixa_ataques_small=pygame.transform.scale(caixa_ataques,(WIDTH,HEIGHT/4))  

    #carrega fonte que será utilizado 
    nome_font=pygame.font.Font('assets/font/PressStart2P.ttf',10)

    #criar variavel para delimitar quando a tecla funciona
    pode_atacar='Sim'

    #----Loop principal-----
    rodando=True
    while rodando:
        ataque_script = None

        
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if pode_atacar=='Sim':
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_1:
                        dano=player.atacar(0)
                        #colocar mensagem quando atacar
                        ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][0][2]
                        text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                        #tirar vida adiversário
                        contra.hp-=dano

                        #ataque adversário 
                        dano_contra,i=contra.ataque_contra()
                        #mensagem que adversário devolve
                        ataque_contra_script=Candidatos['{}'.format(contra.nome)]['movimentos'][i][3]
                        text_ataque_contra=nome_font.render("{}".format(ataque_contra_script),True,(0,0,0))
                        #variaveis dependendo do ataque que adversário usa
                        if i==0 or i==1:
                            player.hp-=dano_contra
                        elif i==2:
                            contra.hp+=dano_contra
                        else:
                            player.hp-=dano_contra
                            contra.hp-=dano_contra/4
                        #faz com que não de para atacar quando não der para ver os ataques na tela
                        pode_atacar='nao'

                    elif event.key==pygame.K_2:
                        dano=player.atacar(1)
                        #colocar mensagem quando atacar
                        ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][1][2]
                        text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                        #tirar vida adiversário
                        contra.hp-=dano

                        #ataque adversário 
                        dano_contra,i=contra.ataque_contra()
                        #mensagem que adversário devolve
                        ataque_contra_script=Candidatos['{}'.format(contra.nome)]['movimentos'][i][3]
                        text_ataque_contra=nome_font.render("{}".format(ataque_contra_script),True,(0,0,0))
                        #variaveis dependendo do ataque que adversário usa
                        if i==0 or i==1:
                            player.hp-=dano_contra
                        elif i==2:
                            contra.hp+=dano_contra
                        else:
                            player.hp-=dano_contra
                            contra.hp-=dano_contra/4
                        
                        #faz com que não de para atacar quando não der para ver os ataques na tela
                        pode_atacar='nao'

                    elif event.key==pygame.K_3:
                        vida=player.atacar(2)
                        #colocar mensagem quando atacar
                        ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][2][2]
                        text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))

                        #tirar vida adiversário
                        player.hp+=vida

                        #ataque adversário 
                        dano_contra,i=contra.ataque_contra()
                        #mensagem que adversário devolve
                        ataque_contra_script=Candidatos['{}'.format(contra.nome)]['movimentos'][i][3]
                        text_ataque_contra=nome_font.render("{}".format(ataque_contra_script),True,(0,0,0))
                        #variaveis dependendo do ataque que adversário usa
                        if i==0 or i==1:
                            player.hp-=dano_contra
                        elif i==2:
                            contra.hp+=dano_contra
                        else:
                            player.hp-=dano_contra
                            contra.hp-=dano_contra/4

                        #faz com que não de para atacar quando não der para ver os ataques na tela
                        pode_atacar='nao'

                    elif event.key==pygame.K_4:
                        dano=player.atacar(3)
                        #colocar mensagem quando atacar
                        ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][3][2]
                        text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                        #tirar vida adiversário
                        player.hp-=dano/4
                        contra.hp-=dano
                        #ataque adversário 
                        dano_contra,i=contra.ataque_contra()
                    #mensagem que adversário devolve
                        ataque_contra_script=Candidatos['{}'.format(contra.nome)]['movimentos'][i][3]
                        text_ataque_contra=nome_font.render("{}".format(ataque_contra_script),True,(0,0,0))
                        #variaveis dependendo do ataque que adversário usa
                        if i==0 or i==1:
                            player.hp-=dano_contra
                        elif i==2:
                            contra.hp+=dano_contra
                        else:
                            player.hp-=dano_contra
                            contra.hp-=dano_contra/4

                        #faz com que não de para atacar quando não der para ver os ataques na tela
                        pode_atacar='nao'





        #-------gerando saidas-----
        BLACK=(0,0,0)
        window.fill(BLACK)
       #dando print nos personagens e tela de fundo 
        window.blit((tela_fundo_small),(0,0))
        window.blit(player.image_small,player.rect)
        window.blit(contra.image_small,contra.rect)
        #vida do player ( barra de vida em cima  )
        pygame.draw.polygon(window, BLACK, [(30, 10), (130, 10), (130, 30), (30, 30)])
        pygame.draw.polygon(window, (0,128,0), [(30, 10), ((player.hp+30), 10), ((player.hp+30), 30), (30, 30)])
        #vida do contra (barra de vida em cima )
        pygame.draw.polygon(window, BLACK, [(470, 10), (570, 10), (570, 30), (470, 30)])
        pygame.draw.polygon(window, (0,128,0), [(470, 10), ((contra.hp+470), 10), ((contra.hp+470), 30), (470, 30)])

         
        #dando print nos nomes de ataque e caixa ataque
        if ataque_script == None:
            window.blit(caixa_ataques_small,(0,(HEIGHT-100)))
            for i in range(0,4):
                ataque=Candidatos['{}'.format(personagem)]['movimentos'][i][0]
                text_surface=nome_font.render("{}".format(ataque),True,(0,0,0))
                text_rect=text_surface.get_rect()
                if i==1:
                    text_rect_pos=(80,(HEIGHT-40))
                    window.blit(text_surface,text_rect_pos)
                elif i==3:
                    text_rect_pos=(360,(HEIGHT-40))
                    window.blit(text_surface,text_rect_pos)
                elif i==0:
                    text_rect_pos=(80,(HEIGHT-70))
                    window.blit(text_surface,text_rect_pos)
                elif i==2:
                    text_rect_pos=(360,(HEIGHT-70))
                    window.blit(text_surface,text_rect_pos)
                
                #faz com que quando apareça os ataques pode se atacar denovo
                pode_atacar='Sim'
        else:
            pass
    


        pygame.display.update()#atualizar frames
        #dar print nas escrituras pós ataques
        if ataque_script!=None:
            ataque_rect_pos=(30,(HEIGHT-70))
            window.blit(text_ataque,ataque_rect_pos)
            pygame.display.update()#atualiza frame com a escritura
            time.sleep(1)
            ataque_contra_rect=(30,(HEIGHT-40))
            window.blit(text_ataque_contra,ataque_contra_rect)
            pygame.display.update()
            time.sleep(1)
        if player.hp<=0 or contra.hp<=0:
            return ENCERRAR

