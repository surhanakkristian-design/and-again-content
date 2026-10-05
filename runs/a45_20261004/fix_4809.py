import json
p='content/4809.json'; d=json.load(open(p))
for tp in d['taps']:
    for k in tp['keys']:
        if k['t']==3.5:
            if tp['target']=='the woman':
                k.clear(); k.update({"t":3.5,"x":0.45,"y":0.34,"w":0.13,"h":0.28})
            elif tp['target']=='the man in the hoodie':
                k.update({"x":0.08,"w":0.37})
    if tp['target']=='the man with curly hair': tp['phrase']='to have thick curly hair'
d['notes']+=" VERIFIER: phrase 3 was 'to have curly hair' (A2 only) -> 'to have thick curly hair'; at 3.5 s the woman's face is clearly visible between the men: she gets a narrow box (x 0.45-0.58), the hoodie man's box ends at 0.45 (his forearm lies in her box)."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
