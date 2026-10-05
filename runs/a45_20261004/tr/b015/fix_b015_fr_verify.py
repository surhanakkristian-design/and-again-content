import json
f=json.load(open('fr.json'))
fixes=[]
def s(i,field,idx,new,why):
    if idx is None: old=f[i][field]; f[i][field]=new
    else: old=f[i][field][idx]; f[i][field][idx]=new
    fixes.append(f"- {i}, {field}{'' if idx is None else '['+str(idx)+']'}: {old} -> {new} ({why})")
cart='cardboard box at a market stall is "un carton"; "caisse" suggests a wooden crate'
s('4612','phrases',1,'remplir un carton',cart); s('4612','nouns',1,'un carton',cart); s('4612','answer',None,'Il vend un carton de pêches.',cart)
s('4625','nouns',2,'une cocarde','an election rosette is "une cocarde"; French "rosette" is a decoration/sausage')
w='"écarter grand les bras" is not idiomatic'
s('4636','phrases',0,'écarter largement les bras',w); s('4694','phrases',2,'écarter largement les bras',w); s('4706','phrases',1,'écarter largement les bras',w)
s('4706','answer',None,'Il crie, les bras largement écartés.','same wording as the phrase')
s('4653','phrases',2,'être grande ouverte','agreement with "la porte" (target: the front door)')
s('4653','answer',None,'Il tape des pieds pour enlever la boue de ses bottes.','"en caoutchouc" added, not in the English')
s('4723','nouns',1,'un short','one garment; same word as the phrase "porter un short orange"')
s('4734','phrases',0,'être allongée sous une couverture','agreement with the target (the young woman)')
s('4735','phrases',1,"l'attraper par-derrière",'spelling: "par-derrière" takes a hyphen')
json.dump(f,open('fr.json','w'),ensure_ascii=False,indent=1)
open('fixes_b015_fr.txt','w').write('\n'.join(fixes)+'\n')
