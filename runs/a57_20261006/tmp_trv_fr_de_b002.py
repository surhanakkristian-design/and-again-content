import json
p='tr/b002/de/fr.json'
d=json.load(open(p))
log=[]
def sub(k,old,new,why):
    v=d[k];n=0
    for fld in ['phrases','nouns','recall']:
        for i,x in enumerate(v[fld]):
            if old in x:
                v[fld][i]=x.replace(old,new);n+=1;log.append((k,f'{fld}[{i}]',x,v[fld][i],why))
    for fld in ['question','answer']:
        if old in v[fld]:
            x=v[fld];v[fld]=x.replace(old,new);n+=1;log.append((k,fld,x,v[fld],why))
    assert n,(k,old)
sub('7996','se remarquer nettement','ressortir nettement','auffallen: "ressortir" is the natural verb')
sub('7996','Quelle tulipe se remarque ?','Quelle tulipe ressort ?','same verb in the whole video')
sub('7996','se remarque parmi','ressort parmi','same verb in the whole video')
sub('7124','applaudir depuis le balcon','crier de joie depuis le balcon','jubeln = cheer, not clap')
sub('7932','applaudir les bras levés','exulter les bras levés','jubeln = cheer, not clap')
sub('7563','applaudir près du portail','crier de joie près du portail','jubeln = cheer, not clap')
sub('36','pendouiller dans les airs','pendre dans le vide','pendouiller is slangy; neutral entry form')
sub('673','regarder fixement, abasourdie','fixer d\'un air abasourdi','unnatural comma construction')
sub('7870','pendre de la fourchette','pendre au bout de la fourchette','natural French')
sub('5053','pendre de la valise','pendre à la valise','natural French')
sub('98','plisser fort les yeux','fermer très fort les yeux','zukneifen = squeeze shut')
sub('7813','jouer en duo sur des seaux','jouer des percussions en duo sur des seaux','trommeln was missing; same verb as the answer')
sub('596','les coureuses','les coureurs','die Läufer is generic masculine plural')
sub('4209','le masque','le masque facial','Gesichtsmaske = face mask')
sub('4125','tirer sur un drap','tirer sur un tissu','drap = bed sheet; Tuch on stage = cloth')
sub('5417','le tote bag','le sac en toile','anglicism; Stoffbeutel = sac en toile')
sub('4918','Que porte le jeune homme en haut de l\'escalier ?',"Qu'est-ce que le jeune homme monte dans l'escalier ?",'original reads "carries at the top of the stairs"')
sub('4918','monte les sacs en papier en haut de l\'escalier',"monte péniblement les sacs en papier dans l'escalier",'schleppen = lug; clearer direction')
sub('730','essuyer le plan de travail de la cuisine','essuyer le comptoir de la cuisine','Küchentheke in a restaurant = counter')
sub('7200','porter le pilote vers le haut','élever le pilote dans les airs','natural French')
sub('5538',"rougeoyer d'orange et de rose","s'illuminer d'orange et de rose",'rougeoyer d\'orange is unidiomatic')
sub('5117','bouquine dans une librairie','fouine dans une librairie','stöbern = browse, bouquiner = read')
sub('5540','escalade un mur d\'escalade raide','gravit un mur d\'escalade raide','avoid "escalade un mur d\'escalade"')
sub('515',"escalader un mur d'escalade","gravir un mur d'escalade",'avoid "escalader un mur d\'escalade"')
sub('124','croquer le pain avec gourmandise','mordre dans le pain avec gourmandise','beißen in = bite into')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
with open('tmp_trv_fr_de_b002.log','w') as f:
    for r in log: f.write('- %s %s: %s -> %s (%s)\n'%r)
print(len(log))
