import json,os
H=os.path.dirname(os.path.abspath(__file__))
p=f'{H}/hu.json'; t=json.load(open(p)); raw=open(p).read()
n=sum(3+len(v['nouns'])+2 for v in t.values())
x=t['217']
assert x['phrases'][0]=='a darttáblára célozni' and x['nouns'][1]=='darttábla'
x['phrases'][0]='a dartstáblára célozni'; x['nouns'][1]='dartstábla'
x['answer']=x['answer'].replace('darttáblára','dartstáblára')
y=t['223']; assert 'bukósisakos' in y['answer']
y['answer']=y['answer'].replace('bukósisakos','sisakos')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=2 if '\n  ' in raw else None)
print(n,x,y['answer'])
