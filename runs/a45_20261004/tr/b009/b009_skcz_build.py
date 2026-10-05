import json,sys
code=sys.argv[1]; out={}
for l in open(f'b009_{code}_lines.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if not l: continue
    i,p,n,q,a=l.split('|')
    out[i]={'phrases':p.split(';'),'nouns':n.split(';'),'question':q,'answer':a}
json.dump(out,open(f'{code}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out))
