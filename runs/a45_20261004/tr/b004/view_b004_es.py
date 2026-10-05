import json
s=json.load(open('tr/b004/source.json'));t=json.load(open('tr/b004/es.json'))
for k,v in s.items():
    e=t[k]
    print(f"## {k} | {v['about']}")
    for i,p in enumerate(v['phrases']): print(f" P{i} {p['en']} [{p['target']}] => {e['phrases'][i]}")
    print(" N "+" | ".join(f"{a} => {b}" for a,b in zip(v['nouns'],e['nouns'])))
    print(f" Q {v['question']} => {e['question']}")
    print(f" A {v['answer']} => {e['answer']}")
