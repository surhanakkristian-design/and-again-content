import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/'
s=json.load(open(R+'source_de.json')); t=json.load(open(R+'de/en.json'))
for k,v in s.items():
    o=t[k]
    print(f"## {k} | {v.get('about','')[:110]}")
    for p,q in zip(v['phrases'],o['phrases']): print(f" P {p['text']} => {q}")
    print(" N", ' ; '.join(f"{a}={b}" for a,b in zip(v['nouns'],o['nouns'])))
    print(f" Q {v['question']} => {o['question']}")
    print(f" A {v['answer']} => {o['answer']}")
    for p,q in zip(v['recall'],o['recall']): print(f" R {p} => {q}")
