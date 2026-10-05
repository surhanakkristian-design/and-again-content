import json,sys,os
D=os.path.dirname(os.path.abspath(__file__))
code=sys.argv[1]
src=json.load(open(os.path.join(D,'source.json')))
out={}
for line in open(os.path.join(D,f'b015_{code}.txt'),encoding='utf-8'):
    line=line.strip()
    if not line: continue
    f=line.split('|')
    assert len(f)==7,line
    out[f[0]]={"phrases":f[1:4],"nouns":f[4].split(';'),"question":f[5],"answer":f[6]}
res={}
for k,v in src.items():
    o=out[k]
    assert len(o['phrases'])==len(v['phrases']) and len(o['nouns'])==len(v['nouns']),k
    res[k]=o
assert set(out)==set(src)
json.dump(res,open(os.path.join(D,f'{code}.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(code,len(res))
