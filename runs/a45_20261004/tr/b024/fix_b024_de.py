import json
p='tr/b024/de.json'
d=json.load(open(p))
def rn(i,old,new):
    l=d[i]['nouns']; assert old in l,(i,old); l[l.index(old)]=new
rn('6851','ein Metallgehäuse','ein Metallkoffer')
rn('6910','Blattgold','Goldfolie')
rn('6914','Klippen','Felswände')
rn('6935','eine Caféteke','eine Cafétheke')
rn('6940','eine Tasse','ein Becher')
assert d['6912']['answer']=='Sie hält eine gestreifte Socke über ihren Kopf.'
d['6912']['answer']='Sie hält eine gestreifte Socke über ihrem Kopf.'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
