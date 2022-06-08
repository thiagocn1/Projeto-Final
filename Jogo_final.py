
#importar todas as outras bibliotecas
import pygame
from Menu import menu_screen
from jogar_novamente import jogar_novamente_screen
from luta import luta_screen
from configuracoes import *
from zmundo_aberto import  mundo_screen2
import os
pygame.init()
pygame.mixer.init()

#-------Gera tela de jogo
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pokecrias')

#mudar telas vai ser negocio do while
#alteranod status vai passar de arquivo em arquivo

Status=MENU
numero_vitórias=0 
x=WIDTH-100
y=HEIGHT-100
pygame.mixer.music.load(os.path.join(SND_DIR, 'musica.mp3'))
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.3)
while Status != ENCERRAR:

    if Status==MENU: 
        Status, nome =menu_screen(window,WIDTH,HEIGHT)
        player=Status
    elif Status==LUTA:
        pygame.mixer.music.pause()
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.3)
        Status,condicao= luta_screen(window,nome)
    elif Status==MAPA2:
        pygame.mixer.music.unpause()
        print('MAPA2')
        Status,nome,x,y=mundo_screen2(window,nome,x,y)
        numero_vitórias+=1
    elif Status==TELA:
        Status=jogar_novamente_screen(window,condicao,WIDTH,HEIGHT)
    
    else:
        pygame.mixer.music.stop()
        print('encerrou realmente')
        Status= ENCERRAR
    if numero_vitórias>1:
        condicao=VITORIA
        Status=jogar_novamente_screen(window,condicao,WIDTH,HEIGHT)
#sair do jogo
pygame.quit()

