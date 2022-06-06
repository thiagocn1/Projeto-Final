import pygame
import os
from configuracoes import *

#vamos fazer listas com todas as animações dentro delas
#como nao da para converter quando se nao coloca o display na tela ainda
#vamos fazer uma def


#animação dano
def load_animacoes():
    animacao_dano=[]
    for i in range(1,10):
        #arquivos de animação numerado de 0 a 9
        filename=os.path.join(ANI_DIR,"Dano_ambos_0{}-removebg-preview.png".format(i))
        img=pygame.image.load(filename).convert_alpha()
        img=pygame.transform.scale(img,(100,100))
        animacao_dano.append(img)


    #animação vida
    animacao_vida=[]
    for i in range(0,10):
        #arquivos de animação numerado de 0 a 9
        filename=os.path.join(ANI_DIR,"Vida_0{}-removebg-preview.png".format(i))
        img=pygame.image.load(filename).convert_alpha()
        img=pygame.transform.scale(img,(100,100))
        animacao_vida.append(img)
    animacoes=[animacao_dano,animacao_vida]
    return animacoes


