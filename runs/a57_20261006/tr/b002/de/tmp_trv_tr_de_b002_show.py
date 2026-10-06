import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/'
s=json.load(open(R+'source_de.json'));t=json.load(open(R+'de/tr.json'))
ids=list(s)
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
    S=s[i];T=t[i]
    print(f"## {i} | {S['about'][:150]}")
    for k,p in enumerate(S['phrases']): print(f" P{k} {p['text']} => {T['phrases'][k]}")
    print(" N", ' / '.join(S['nouns']),' => ',' / '.join(T['nouns']))
    print(" Q",S['question'],'=>',T['question'])
    print(" A",S['answer'],'=>',T['answer'])
    for k,r in enumerate(S['recall']): print(f" R{k} {r} => {T['recall'][k]}")
