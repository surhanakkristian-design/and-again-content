import json
p='tr/b024/sk.json'
d=json.load(open(p))
def ph(i,n,old,new):
    assert d[i]['phrases'][n]==old,(i,d[i]['phrases'][n]); d[i]['phrases'][n]=new
def f(i,k,old,new):
    assert d[i][k]==old,(i,k,d[i][k]); d[i][k]=new
ph('6856',0,'uväzovať červenú stužku','zaväzovať červenú stužku')
f('6856','answer','Uväzuje červenú stužku.','Zaväzuje červenú stužku.')
ph('6871',0,'chňapnúť po biskupovej mitre','chytiť biskupovu mitru')
f('6871','answer','Chňape po biskupovej mitre.','Chytá biskupovu mitru.')
ph('6888',0,'viať nad šnúrou','preletieť cez šnúru')
f('6917','answer','Zastavuje sa v malom prístave.','Zastavuje v malom prístave.')
assert d['6940']['nouns'][3]=='šálka'; d['6940']['nouns'][3]='pohár'
ph('6942',2,'preklenúť úzky kanál','klenúť sa nad úzkym kanálom')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
