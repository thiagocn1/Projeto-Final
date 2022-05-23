class Candidato(pygame.sprite.sprite):
    def __init__(self,nome,Candidatos):
        self.nome=nome
        self.movimentos=Candidatos['{}'.format(nome)]['movimento']
        self.ataque=Candidatos['{}'.format(nome)]['ataque'] 
        self.hp=Candidatos['{}'.format(nome)] ['hp']  #quanto de vida ele tem
    
    #luta entre dois casas
    def lutas(self, candidato2):
        while self.hp>0 and candidato2.hp>0:
            candidato2['ataque']