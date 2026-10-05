import json
p='tr/b031/sk.json'
d=json.load(open(p))
assert d['8035']['phrases'][2]=='ležať naprieč lavicou'; d['8035']['phrases'][2]='ležať krížom cez lavicu'
assert d['8057']['nouns'][1]=='šálka'; d['8057']['nouns'][1]='kelímok'
assert d['8064']['phrases'][0]=='pafkať z fajky'; d['8064']['phrases'][0]='bafkať z fajky'
assert d['8064']['answer']=='Ropucha pafká z fajky.'; d['8064']['answer']='Ropucha bafká z fajky.'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
