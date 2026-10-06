import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006'
s=json.load(open(f'{R}/tr/b002/source_es.json')); t=json.load(open(f'{R}/tr/b002/es/sk.json'))
ids=list(s)
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
    S=s[i];T=t[i]
    print(f"## {i} [{S.get('about','')[:110]}]")
    for k,(p,q) in enumerate(zip(S['phrases'],T['phrases'])): print(f" P{k} {p['text']} | {q}")
    print(" N", ' ; '.join(f"{x}={y}" for x,y in zip(S['nouns'],T['nouns'])))
    print(" Q", S['question'],'|',T['question']); print(" A", S['answer'],'|',T['answer'])
    for k,(p,q) in enumerate(zip(S['recall'],T['recall'])): print(f" R{k} {p} | {q}")
