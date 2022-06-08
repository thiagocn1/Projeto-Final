
import pygame
from os import path
from configuracoes import * 
from Candidatos import Candidatos
from Classes import Contra, Efeitodano, Efeitovida, Player
import time
import os
pygame.mixer.init()
haduken=pygame.mixer.Sound(os.path.join(SND_DIR, 'raduken.mp3'))
haduken.set_volume(2)
gemido=pygame.mixer.Sound(os.path.join(SND_DIR, 'gemido2.mp3'))
gemido.set_volume(2)
watchau=pygame.mixer.Sound(os.path.join(SND_DIR, 'watchau.mp3'))
watchau.set_volume(2)

def luta_screen(window,personagem):
    pygame.mixer.music.load(os.path.join(SND_DIR, 'luta1.mp3'))
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.3)
    
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
    nome_font=pygame.font.Font('assets/font/PressStart2P.ttf',20)


    all_sprites = pygame.sprite.Group()

    #----Loop principal-----
    rodando=True
    ataque_script = None
   #criaçao de variaveis, principalmente para controlar tempo
    tipo_ataque=0
    tempo = 0
    tempo_script_ataque = 0
    tempo_script_cataque = 0
    #começa while que repetira
    estado = PODE_ATACAR
    while rodando:
        tempo += 1
        clock.tick(60)
        #para iniciar medição de tempo caso chegue nessas variaveis
        if estado == SCRIPT_CATAQUE:
            tempo_script_cataque +=1
            tempo_script_ataque = 0
        elif estado == SCRIPT_ATAQUE:
            tempo_script_ataque += 1 
            tempo_script_cataque=0
        else:
            #ele 0 para só comecar a medir quando entrar no estado certo
            tempo_script_ataque = 0
            tempo_script_cataque = 0
        #------eventos-------
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rodando=False
            if estado == PODE_ATACAR:
                
                if event.type==pygame.KEYDOWN:
                        
                        #quando aperta 1
                        if event.key==pygame.K_1:
                            pygame.mixer.Sound.play(haduken)
                            estado=ATACANDO
                            tempo = 0
                            dano=player.atacar(0)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][0][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                            #tirar vida adiversário
                            contra.hp-=dano
                            #delimita tipo de ataque para a animação depois
                            tipo_ataque=1
                            #esta aqui dentro para não acontecer nada quando aperta outras téclas
                            estado=ANIMACAO_ATAQUE
                        
                        #quando aperta 2
                        elif event.key==pygame.K_2:
                            estado=ATACANDO
                            pygame.mixer.Sound.play(haduken)
                            dano=player.atacar(1)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][1][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                            #tirar vida adiversário
                            contra.hp-=dano
                            #delimita tipo de ataque para animação depois
                            tipo_ataque=2
                            #esta aqui dentro para não acontecer nada quando aperta outras téclas
                            estado=ANIMACAO_ATAQUE

                        #quando aperta 3
                        elif event.key==pygame.K_3:
                            estado=ATACANDO
                            pygame.mixer.Sound.play(gemido)
                            vida=player.atacar(2)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][2][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))

                            #poe vida no player 
                            player.hp+=vida
                            #delimita tipo de ataque para animação depois
                            tipo_ataque=3
                            #esta aqui dentro para não acontecer nada quando aperta outras téclas
                            estado=ANIMACAO_ATAQUE

                        #quando aperta 4
                        elif event.key==pygame.K_4:
                            estado=ATACANDO
                            pygame.mixer.Sound.play(watchau)
                            dano=player.atacar(3)
                            #colocar mensagem quando atacar
                            ataque_script=Candidatos['{}'.format(personagem)]['movimentos'][3][2]
                            text_ataque=nome_font.render("{}".format(ataque_script),True,(0,0,0))
                            #tirar vida adiversário e sua
                            player.hp-=dano/4
                            contra.hp-=dano
                            #delimita tipo de ataque para animação depois
                            tipo_ataque=4
                            #esta aqui dentro para não acontecer nada quando aperta outras téclas
                            estado=ANIMACAO_ATAQUE
                        else:
                            pass
                          
        
        if estado == CATACANDO:
            
            #ataque adversário 
            dano_contra,tipo_cataque=contra.ataque_contra()
            #mensagem que adversário devolve
            ataque_contra_script=Candidatos['{}'.format(contra.nome)]['movimentos'][tipo_cataque][3]
            text_ataque_contra=nome_font.render("{}".format(ataque_contra_script),True,(0,0,0))
            #variaveis dependendo do ataque que adversário usa
            if tipo_cataque==0 or tipo_cataque==1:
                pygame.mixer.Sound.play(haduken)
                player.hp-=dano_contra
            elif tipo_cataque==2:
                pygame.mixer.Sound.play(gemido)
                contra.hp+=dano_contra
            else:
                pygame.mixer.Sound.play(watchau)
                player.hp-=dano_contra
                contra.hp-=dano_contra/4
            estado=ANIMACAO_CATAQUE
            

 

        #-------gerando saidas-----
        BLACK=(0,0,0)
        window.fill(BLACK)
       #dando print nos personagens e tela de fundo 
        window.blit((tela_fundo_small),(0,0))
        window.blit(player.image_small,player.rect)
        window.blit(contra.image_small,contra.rect)
        #vida do player ( barra de vida em cima  )
        pygame.draw.polygon(window, BLACK, [(WIDTH/20, HEIGHT/40), (WIDTH/4.615, HEIGHT/40), (WIDTH/4.615, HEIGHT/13.33333), (WIDTH/20, HEIGHT/13.33333)])
        pygame.draw.polygon(window, (0,128,0), [(WIDTH/20, HEIGHT/40), ((player.hp+WIDTH/20), HEIGHT/40), ((player.hp+WIDTH/20), HEIGHT/13.33333), (WIDTH/20, HEIGHT/13.33333)])
        #vida do contra (barra de vida em cima )
        pygame.draw.polygon(window, BLACK, [(WIDTH/1.27659, HEIGHT/40), (WIDTH/1.0526, HEIGHT/40), (WIDTH/1.0526, HEIGHT/13.33333), (WIDTH/1.27659, HEIGHT/13.33333)])
        pygame.draw.polygon(window, (0,128,0), [(WIDTH/1.27659, HEIGHT/40), ((contra.hp+WIDTH/1.2765), HEIGHT/40), ((contra.hp+WIDTH/1.2765), HEIGHT/13.33333), (WIDTH/1.27659, HEIGHT/13.33333)])
        #caixa ataque blit
        if estado == PODE_ATACAR:
            window.blit(caixa_ataques_small,(0,(HEIGHT-HEIGHT/4)))
            for i in range(0,4):
                ataque=Candidatos['{}'.format(personagem)]['movimentos'][i][0]
                text_surface=nome_font.render("{}".format(ataque),True,(0,0,0))
                text_rect=text_surface.get_rect()
                if i==1:
                    text_rect_pos=(WIDTH/7.5,(HEIGHT-HEIGHT/10))
                    window.blit(text_surface,text_rect_pos)
                elif i==3:
                    text_rect_pos=(WIDTH/1.666,(HEIGHT-HEIGHT/10))
                    window.blit(text_surface,text_rect_pos)
                elif i==0:
                    text_rect_pos=(WIDTH/7.5,(HEIGHT-HEIGHT/5.71428571))
                    window.blit(text_surface,text_rect_pos)
                elif i==2:
                    text_rect_pos=(WIDTH/1.666,(HEIGHT-HEIGHT/5.71428571))
                    window.blit(text_surface,text_rect_pos)
        #aqui da print na messagem quando ataca do player
        if estado == SCRIPT_ATAQUE :
                ataque_rect_pos=(WIDTH/20,(HEIGHT-HEIGHT/5.71428571))
                window.blit(text_ataque,ataque_rect_pos)
                if tempo_script_ataque > 120:
                    estado = CATACANDO
                    tempo_script_ataque = 0
                    
                
        #aqui faz a animação   
        if estado==ANIMACAO_ATAQUE:
            #adicionar animação
            #animaçao varia dependendo da tecla de ataque
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
                
            estado = SCRIPT_ATAQUE
            
        #animação do ataque do oponente
        if estado==ANIMACAO_CATAQUE:

            #adicionar animação
            #animacao varia dependendo do ataque
            if tipo_cataque==0:
                efeito= Efeitodano(player.rect.center)
                all_sprites.add(efeito)
            elif tipo_cataque==1:
                efeito= Efeitodano(player.rect.center)
                all_sprites.add(efeito)
            elif tipo_cataque==2:
                efeito= Efeitovida(contra.rect.center)
                all_sprites.add(efeito)
            elif tipo_cataque==3:
                efeito= Efeitodano(contra.rect.center)
                all_sprites.add(efeito)
                efeito=Efeitodano(player.rect.center)
                all_sprites.add(efeito)
                
            estado = SCRIPT_CATAQUE
            
        #faz a mensagem do ataque do oponente
        if estado ==  SCRIPT_CATAQUE:
            ataque_contra_rect=(WIDTH/20,(HEIGHT-HEIGHT/10))
            window.blit(text_ataque_contra,ataque_contra_rect)
            if tempo_script_cataque > 120:
                tempo_script_cataque = 0
                estado=PODE_ATACAR
                
        #aqui faz as condições se perde ou ganha
        #ela vai mandar isso para o arquivo jogo final
        #e vai delimitar a tela que se vai receber ou de vitoria ou de derrota
        if player.hp<=0 or contra.hp<=0:
            print('ENCERRANDO')
            print(player.hp,'player')
            print(contra.hp)
            if player.hp>0 and contra.hp<=0:
                print('VITORIA')
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join(SND_DIR, 'v.mp3'))
                pygame.mixer.music.play(loops=1)
                return TELA,VITORIA
            elif contra.hp>0 and player.hp<=0:
                print('EMPATE')
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join(SND_DIR, 'derrota.mp3'))
                pygame.mixer.music.play(loops=1)
                return TELA, EMPATE
            else:
                print('DERROTA')
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join(SND_DIR, 'derrota.mp3'))
                pygame.mixer.music.play(loops=1)
                return TELA,DERROTA

         
        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()#atualiza frame com a escritura
