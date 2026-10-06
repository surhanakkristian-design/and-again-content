import json
def load(i): return json.load(open(f'content/es/{i}.json'))
def save(i,d): json.dump(d,open(f'content/es/{i}.json','w'),ensure_ascii=False,indent=1)
# 211
d=load(211)
for r in d['recall']:
    for p in r['parts']:
        if p.get('gap') and p['text']=='registrando': p['accept']=['registrando','inspeccionando','revisando']
ans=d['recall'].pop()
d['recall'].append({"from":"nouns","parts":[{"text":"el agente de"},{"text":"aduanas","gap":True,"accept":["aduanas"]}]})
d['recall'].append(ans)
save(211,d)
# 212
d=load(212)
for r in d['recall']:
    for p in r['parts']:
        if p.get('gap') and p['text']=='bailarina': p['accept']=['bailarina']
save(212,d)
# 213
d=load(213)
d['taps'][0]['phrase']='preparar la comida'
d['recall'][0]={"from":"taps","parts":[{"text":"preparar la"},{"text":"comida","gap":True,"accept":["comida"]}]}
save(213,d)
# 214
d=load(214)
for r in d['recall']:
    for p in r['parts']:
        if p.get('gap') and p['text']=='caminar': p['accept']=['caminar','andar']
save(214,d)
