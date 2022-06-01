import pygame
import os
from configuracoes import *

#vamos fazer listas com todas as animações dentro delas


#animação dano
animacao_dano=[]
for i in range(0,10):
    #arquivos de animação numerado de 0 a 9
    filename=os.path.join(ANI_DIR,"Dano_ambos_0{}.png".format(i))
    img=pygame.image.load(filename).convert()
    img=pygame.transform.scale(img,(50,50))
    animacao_dano.append(img)


#animação vida
animacao_vida=[]
for i in range(0,10):
    #arquivos de animação numerado de 0 a 9
    filename=os.path.join(ANI_DIR,"Vida_0{}.png".format(i))
    img=pygame.image.load(filename).convert()
    img=pygame.transform.scale(img,(50,50))
    animacao_vida.append(img)
    #pegar animação que é fora do padrão a 10
    if i==9:
        filename=os.path.join(ANI_DIR,"Vida_10.png")
    img=pygame.image.load(filename).convert()
    img=pygame.transform.scale(img,(50,50))
    animacao_vida.append(img)
