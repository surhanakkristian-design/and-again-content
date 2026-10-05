import json,os
p=os.path.expanduser('~/Projects/and-again-content/runs/a45_20261004/tr/b031/de.json')
d=json.load(open(p))
def s(k,f,i,old,new):
    if i is None: assert d[k][f]==old,(k,f); d[k][f]=new
    else: assert d[k][f][i]==old,(k,f,i); d[k][f][i]=new
s('8026','phrases',2,'sich die Schuhe binden','sich die Schuhe zubinden')
s('8045','answer',None,'Sie wirft Schnee mit einer Schaufel.','Sie wirft mit einer Schaufel Schnee.')
s('8048','phrases',2,'sich über die Kante lehnen','sich über den Rand lehnen')
s('8062','phrases',1,'ein gesägtes Holzscheit umklammern','einen gesägten Holzklotz umklammern')
s('8062','nouns',2,'ein Holzscheit','ein Holzklotz')
s('8064','phrases',2,'in die Luft schweben','in die Luft aufsteigen')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
