import json,sys
# usage: fixv_149.py <id> ; edits read from fixv_149_edits_<id>.json : {"boxes":[[tapIdxs,t,x,y,w,h | "off"]], ...}
i=sys.argv[1]
p='content/%s.json'%i
d=json.load(open(p))
e=json.load(open('fixv_149_edits_%s.json'%i))
n=0
for idxs,t,*box in e.get('boxes',[]):
    for ix in idxs:
        for k in d['taps'][ix]['keys']:
            if abs(k['t']-t)<1e-6:
                k.clear(); k['t']=t
                if box==['off']: k['off']=True
                else: k.update(dict(zip('xywh',box)))
    n+=1
for k,v in e.get('set',{}).items(): d[k]=v
for ix,v in e.get('nouns',{}).items(): d['nouns'][int(ix)].update(v)
for ix,v in e.get('taps',{}).items(): d['taps'][int(ix)].update(v)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('boxes changed',n)
