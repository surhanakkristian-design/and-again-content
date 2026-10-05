import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b031/fr.json'
d=json.load(open(p))
def ph(i,n,old,new):
    assert d[i]['phrases'][n]==old,(i,d[i]['phrases'][n]); d[i]['phrases'][n]=new
ph('8020',1,"l'entraîner plus loin","l'éloigner en la tirant")
ph('8029',1,"participer avec des pièces","mettre des pièces au pot")
ph('8035',2,"être allongé en travers du banc","être allongée en travers du banc")
ph('8048',0,"fixer le fond de la gorge","fixer le fond du ravin")
ph('8058',1,"être accroché au mur","être accrochée au mur")
ph('8064',2,"s'élever dans l'air","s'élever dans les airs")
assert d['8060']['answer']=="Un casque de réalité virtuelle couvre ses yeux."
d['8060']['answer']="Un casque de réalité virtuelle lui couvre les yeux."
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
