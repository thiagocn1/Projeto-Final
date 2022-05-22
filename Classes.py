class Candidato:
    def __init__(self,nome,movimento,stats):
        self.nome=nome
        self.movimentos=movimento
        self.ataque=stats['ataque'] 
        self.hp=stats['hp']  #quanto de vida ele tem
    
    #luta entre dois casas
    def lutas(self, candidato2):
        while self.hp>0 and candidato2.hp>0:
            candidato2['ataque']