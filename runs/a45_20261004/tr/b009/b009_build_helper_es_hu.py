import json,sys
lang=sys.argv[1]
src=json.load(open('source.json'))
out={}
for line in open(f'b009_{lang}_data.txt',encoding='utf-8'):
    line=line.rstrip('\n')
    if not line: continue
    i,p,n,q,a=line.split('|')
    out[i]={"phrases":p.split(';'),"nouns":n.split(';'),"question":q,"answer":a}
assert list(out)==list(src),(set(src)^set(out))
for k,v in src.items():
    assert len(out[k]['phrases'])==len(v['phrases']),k
    assert len(out[k]['nouns'])==len(v['nouns']),(k,out[k]['nouns'],v['nouns'])
json.dump(out,open(f'{lang}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(lang,len(out))
