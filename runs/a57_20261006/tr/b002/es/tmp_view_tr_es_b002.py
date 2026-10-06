import json
s=json.load(open('../source_es.json')); t=json.load(open('tr.json'))
n=0
for k in s:
    a=s[k]; b=t[k]
    print(f"=== {k} [{a.get('level')}] {a.get('about','')[:160]}")
    for i,p in enumerate(a['phrases']):
        print(f" P{i}: {p['text']}  ->  {b['phrases'][i]}"); n+=1
    for i,x in enumerate(a['nouns']):
        print(f" N{i}: {x}  ->  {b['nouns'][i]}"); n+=1
    print(f" Q: {a['question']}  ->  {b['question']}")
    print(f" A: {a['answer']}  ->  {b['answer']}"); n+=2
    for i,x in enumerate(a['recall']):
        print(f" R{i}: {x}  ->  {b['recall'][i]}"); n+=1
print("TOTAL",n)
