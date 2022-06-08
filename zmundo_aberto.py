
from configuracoes import *
from zclasse_mundo_aberto import *
pygame.init()

clock=pygame.time.Clock()

#gera tela de jogo 
mapa_sprittes= pygame.sprite.Group()
tchsuco_sprittes=pygame.sprite.Group()
versus_sprittes=pygame.sprite.Group()
class Cenario:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.matriz=MAPA
    def criar_mapa(self):
        for index_linha, linha in enumerate (MAPA):
            for index_coluna,coluna in enumerate(linha):
                x=index_coluna*TAMNHO_PEDACOS
                y=index_linha*TAMNHO_PEDACOS
                if coluna=='X':
                    rua=Rua([x,y])
                    mapa_sprittes.add(rua)
                if coluna =="c":
                    candidato=Candidato([x,y])
                    versus_sprittes.add(candidato)

                    




def mundo_screen2(screen,nome,x,y):
    rodando='s'
    tchusco=mapa_player()
    tchusco.rect.centerx=x-50
    tchusco.rect.centery=y-50
    tchsuco_sprittes.add(tchusco)
    Cenario.criar_mapa(screen)
    while rodando=='s':
        clock.tick(60)
        #-----Eventos------
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    rodando=False
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            tchusco.vy-=8
                        if event.key == pygame.K_s:
                            tchusco.vy+=8
                        if event.key == pygame.K_d:
                            tchusco.vx+=8
                        if event.key == pygame.K_a:
                            tchusco.vx-=8
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                            tchusco.vy+=8
                        if event.key == pygame.K_s:
                            tchusco.vy-=8
                        if  event.key == pygame.K_d:
                            tchusco.vx-=8
                        if event.key == pygame.K_a:
                            tchusco.vx+=8

        screen.fill((0,0,0))
        tchsuco_sprittes.update()
        versus_sprittes.update()
        #colide entre coisa do mapa e o player
        encontros=pygame.sprite.spritecollide(tchusco,mapa_sprittes,False)
        #verifica se tem colisão e não deixa passar 
        if encontros:
            if tchusco.vx!=0:
                tchusco.rect.centerx-=tchusco.vx
            if tchusco.vy!=0:
                tchusco.rect.centery-=tchusco.vy
        lutas=pygame.sprite.spritecollide(tchusco,versus_sprittes,True)
        if lutas:
            tchusco.kill()
            return LUTA,nome,tchusco.rect.centerx,tchusco.rect.centery
        
            print('lutem')
        #gera saidas
        tchsuco_sprittes.draw(screen)
        mapa_sprittes.draw(screen)
        versus_sprittes.draw(screen)
        pygame.display.update()
