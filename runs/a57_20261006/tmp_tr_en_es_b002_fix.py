import json
p='tr/b002/es/en.json'; t=json.load(open(p))
def setv(vid,field,idx,old,new):
    x=t[vid]
    if idx is None:
        assert x[field]==old,(vid,field,x[field]); x[field]=new
    else:
        assert x[field][idx]==old,(vid,field,idx,x[field][idx]); x[field][idx]=new
setv('7239','phrases',2,'to rub its head','to rub his head'); setv('7239','recall',2,'to rub its head','to rub his head')
setv('5594','answer',None,'The magnificent dragon lands on the ridge.','The magnificent dragon is landing on the ridge.')
setv('5594','recall',3,'lands on the ridge','is landing on the ridge')
setv('7835','recall',4,'runs down the slope','is running down the slope')
setv('7835','phrases',0,'to flow down the slope','to run down the slope'); setv('7835','recall',0,'to flow down the slope','to run down the slope')
setv('7453','question',None,'What does the cook do?','What is the cook doing?')
setv('7744','phrases',2,'to stand open-mouthed','to be left open-mouthed'); setv('7744','recall',2,'to stand open-mouthed','to be left open-mouthed')
setv('7154','question',None,'How does the businessman get around?','How is the businessman getting about?')
setv('7154','answer',None,'He gets around on a unicycle.','He is getting about on a unicycle.')
setv('7154','recall',3,'He gets around on a unicycle','He is getting about on a unicycle')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
s=json.load(open('tr/b002/source_es.json'))
print(sum(len(v['phrases'])+len(v['nouns'])+2+len(v['recall']) for v in s.values()))
