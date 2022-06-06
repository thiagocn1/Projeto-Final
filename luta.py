
import pygame
from os import path
from configuracoes import * 
from Candidatos import Candidatos
from Classes import Contra, Efeitodano, Efeitovida, Player
import time

def luta_screen(window,personagem):
    #unidade de tempo
    clock=pygame.time.Clock()
    
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

    all_sprites = pygame.sprite.Group()

    #----Loop principal-----
    rodando=True
    ataque_script = None
    tempo_ataque = 0
    PODE_ATACAR = 'PODE_ATACAR'
    ATACANDO = 'ATACANDO'
    ANIMACAO_ATAQUE = 'ANIMACAO_ATAQUE'
    SCRIPT_ATAQUE = 'SCRIPT_ATAQUE'
    CATACANDO = 'CATACANDO'
    ANIMACAO_CATAQUE = 'ANIMACAO_CATAQUE'
    SCRIPT_CATAQUE = 'SCRIPT_CATAQUE'
    tipo_ataque=0

    estado = PODE_ATACAR
    tempo = 0
    tempo_script=0
    while rodando:
        tempo += 1
        clock.tick(60)
        
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if estado == PODE_ATACAR:
                print('pode atacar')
                if event.type==pygame.KEYDOWN:
                        estado=ATACANDO
                        print('estado atacando')
                        if event.key==pygame.K_1:
                            tempo = 0
                            dano=player.atacar(0)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][0][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                            #tirar vida adiversário
                            contra.hp-=dano
                            #delimita tipo de ataque para a animação depois
                            tipo_ataque=1
                        
                        elif event.key==pygame.K_2:
                            dano=player.atacar(1)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][1][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                            #tirar vida adiversário
                            contra.hp-=dano
                            #delimita tipo de ataque para animação depois
                            tipo_ataque=2

                        elif event.key==pygame.K_3:
                            vida=player.atacar(2)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][2][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))

                            #tirar vida adiversário
                            player.hp+=vida
                            #delimita tipo de ataque para animação depois
                            tipo_ataque=3

                        elif event.key==pygame.K_4:
                            dano=player.atacar(3)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][3][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                            #tirar vida adiversário
                            player.hp-=dano/4
                            contra.hp-=dano
                            #delimita tipo de ataque para animação depois
                            tipo_ataque=4

                        estado=SCRIPT_ATAQUE
                        print('estado script ataque')   
        
        if estado == CATACANDO:
            
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
            estado=SCRIPT_CATAQUE
            print('estado scriptcataque')

 

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
        #caixa ataque blit
        if estado == PODE_ATACAR:
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
    
        if estado == SCRIPT_ATAQUE :
                ataque_rect_pos=(30,(HEIGHT-70))
                window.blit(text_ataque,ataque_rect_pos)
                estado = ANIMACAO_ATAQUE
                print('estado animação ataque')
                
            
        if estado==ANIMACAO_ATAQUE:
            print('entrei na animação')
            print(tipo_ataque)
            #adicionar animação
            if tipo_ataque==1:
                efeito= Efeitodano(contra.rect.center)
                all_sprites.add(efeito)
            elif tipo_ataque==2:
                efeito= Efeitodano(contra.rect.center)
                all_sprites.add(efeito)
            elif tipo_ataque==3:
                efeito= Efeitovida(player.rect.center)
                all_sprites.add(efeito)
            elif tipo_ataque==4:
                efeito= Efeitodano(player.rect.center)
                all_sprites.add(efeito)
                efeito=Efeitodano(contra.rect.center)
                all_sprites.add(efeito)
                
            estado = CATACANDO
            print('estado CATACANDO')

        if estado ==  SCRIPT_CATAQUE:
            ataque_contra_rect=(30,(HEIGHT-40))
            window.blit(text_ataque_contra,ataque_contra_rect)
            estado=PODE_ATACAR
            print('pode atacar')
        
        if player.hp<=0 or contra.hp<=0:
            print('ENCERRANDO')
            print(player.hp,'player')
            print(contra.hp)
            return ENCERRAR

         
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()#atualiza frame com a escritura
