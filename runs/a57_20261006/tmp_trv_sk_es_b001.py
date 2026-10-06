import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b001/'
s=json.load(open(R+'source_es.json')); t=json.load(open(R+'es/sk.json'))
ids=list(s)
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
    S=s[i];T=t[i]
    print(f"## {i} [{S.get('about','')[:110]}]")
    for k,(p,q) in enumerate(zip(S['phrases'],T['phrases'])): print(f" p{k}: {p['text']} | {q}")
    for k,(p,q) in enumerate(zip(S['nouns'],T['nouns'])): print(f" n{k}: {p} | {q}")
    print(f" Q: {S['question']} | {T['question']}")
    print(f" A: {S['answer']} | {T['answer']}")
    for k,(p,q) in enumerate(zip(S['recall'],T['recall'])): print(f" r{k}: {p} | {q}")
print(len(ids))
