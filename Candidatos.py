
from configuracoes import WIDTH

#dicionário com especificações para cada candidato
Candidatos={'Lula':{
'ataque':100,
'hp':WIDTH/6,
'movimentos':[
    ['Jogar dedo',WIDTH/30," Lula regenera seu dedo e o joga no seu adversário","Lula usou ataque Jogar dedo e aplicou dano"],
    ['Recorrer',WIDTH/30,"Lula recorre trazendo vergonha ao seu adversário","Lula usuou ataque Recorrer e aplicou dano"],
    ['Corrupção',WIDTH/20," Lula Rouba Mensalão compra triplex para repousar","Lula utilizou Corrupção e recuperou vida"],
    ['Sair da prisão',WIDTH/15,"Ao sair da prisão lula se arranha, ambos sofrem dano","Lula utilizou Sair da prisão sofrendo e infligindo dano" ]
],
'imagem':'Lula.webp'},
'Bolsonaro':{
'ataque':100,
'hp':WIDTH/6,
'movimentos':[
    ['Jacaré',WIDTH/30,'Bolsaro tomou coronavac e virou um jacaré atacando o adversáiro ',"Bolsonaro usou ataque jacaré e aplicou dano" ],
    ['Porte de arma',WIDTH/30,"Bolsonaro liberou AK47 e pipocou","Bolsonaro utilizou ataque porte de arma e aplicou dano "],
    ['Corrupção',WIDTH/20,"Rachadinha de Bolsonaro cobriu seu convenio ele ganhou 30 de vida","Bolsonáro utilizou Corrupção e recuperou vida"],
    ['Golpe',WIDTH/15,"Bolsonáro tenta dar um golpe mas é burro, toma dano também","Bolsonaro utilizou golpe sofrendo e infligindo dano"]],
'imagem':'Jair.webp'},
'Doria':{
'ataque':100,
'hp':WIDTH/6,
'movimentos':[['Calça justa',WIDTH/30,"Adversário se confunde com as nadegas de Doria","Doria utilizou Calça justa e infligiu dano"],
    ['Coxinha',WIDTH/30,"Doria engorda adversário","Doria utilizou Coxinha e infligiu dano"],
    ['Já foi para Dubai?',WIDTH/20,"Doria vai para Dubai encontra Shake e melhora autoestima","Doria utilizou Já foi para Dubai? e recuperou vida"],
    ['Vacina já',WIDTH/15,"Ambos tem reação a vacina","Doria utiliza Vacina já sofrendo e infligindo dano"]],
'imagem':'Doria.png'},
'Ciro':{
'ataque':100,
'hp':WIDTH/6,
'movimentos':[['Agora vai',WIDTH/30,"Ciro intimida adversário pela sua persistencia","Ciro utilizou Agora vai e infligiu dano"],
    ['Coronelismo',WIDTH/30,"Ciro domina Ceará ","Ciro utilizou Coronelismo e infligiu dano"],
    ['Xingar jornalista',WIDTH/20,"Ciro se sente bem","Ciro utilizou Xingar jornalista e recuperou vida"],
    ['Capitão do mato',WIDTH/15,"Ciro é racista","Ciro utiliza Capião do mato sofrendo e infligindo dano"]],
'imagem':'Ciro.png'},
'Moro':{
'ataque':100,
'hp':WIDTH/6,
'movimentos':[['Incompetencia',WIDTH/30,"Moro tenta prender adversário mas é incompetente","Moro utilizou Incompetencia e infligiu dano"],
    ['Lava jato',WIDTH/30,"Adversário é acusado de corrupção","Moro utilizou Lava jato e infligiu dano"],
    ['Delação premiada',WIDTH/20,"Moro denuncia adversário","Moro utilizou Delação premiada e recuperou vida"],
    ['Paga pau do bolso',WIDTH/15,"Moro vira ministro e se queima","Moro utiliza Paga pau do bolso sofrendo e infligindo dano"]],
'imagem':'Moro.png'},
}

