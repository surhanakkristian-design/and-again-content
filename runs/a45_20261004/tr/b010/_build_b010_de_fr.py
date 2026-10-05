import json,sys
code=sys.argv[1]
src=json.load(open('tr/b010/source.json'))
out={}
for line in open(f'tr/b010/_data_b010_{code}.txt',encoding='utf-8'):
    line=line.rstrip('\n')
    if not line: continue
    i,p,n,q,a=line.split('|')
    out[i]={"phrases":p.split(';'),"nouns":n.split(';'),"question":q,"answer":a}
assert list(out)==list(src),(set(src)^set(out))
for k,v in src.items():
    assert len(out[k]['phrases'])==len(v['phrases']),k
    assert len(out[k]['nouns'])==len(v['nouns']),k
json.dump(out,open(f'tr/b010/{code}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(code,len(out))
