import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/'
s=json.load(open(R+'source_es.json')); t=json.load(open(R+'es/ua.json'))
for k,v in s.items():
    u=t[k]
    print(f"=== {k} [{v.get('level')}] {v.get('about','')[:160]}")
    for p,q in zip(v['phrases'],u['phrases']): print(f" P {p['text']} | {q}")
    for p,q in zip(v['nouns'],u['nouns']): print(f" N {p} | {q}")
    print(f" Q {v['question']} | {u['question']}")
    print(f" A {v['answer']} | {u['answer']}")
    for p,q in zip(v['recall'],u['recall']): print(f" R {p} | {q}")
