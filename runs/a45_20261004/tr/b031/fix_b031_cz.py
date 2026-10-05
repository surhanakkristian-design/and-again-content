import json
p='tr/b031/cz.json'
d=json.load(open(p))
assert d['8034']['phrases'][2]=='stékat po úbočí hory'; d['8034']['phrases'][2]='řinout se po úbočí hory'
assert d['8035']['phrases'][2]=='ležet napříč lavicí'; d['8035']['phrases'][2]='ležet přes lavici'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
