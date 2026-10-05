import json
p='content/5467.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to rub his face': t['phrase']='to hug his blanket'
c['answer']=['He','is','hugging','his','blanket.']
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
