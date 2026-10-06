import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/'
s=json.load(open(P+'source_es.json')); t=json.load(open(P+'es/ua.json'))
log=[]
def rep(k,field,old,new,why):
    v=t[k][field]
    if isinstance(v,list):
        for i,x in enumerate(v):
            if x==old: v[i]=new; log.append(f"- {k} {field}: {old} -> {new} ({why})")
    elif v==old: t[k][field]=new; log.append(f"- {k} {field}: {old} -> {new} ({why})")
fx=[('7996','стояти, притулившись до поруччя','стояти прихиленим до поруччя','the bicycle is leaned against the rail; the gerund implies a living agent'),
('7844','бути вдягненою в сорочку з коміром','носити сорочку з коміром','gendered, clumsy entry form; neutral natural infinitive'),
('5458','мати етикетку з вітамінами','мати вітамінну етикетку','"etiqueta de vitaminas" is a vitamin label, not a label with vitamins'),
('5517','тримати вудку','нести вудку','llevar here = carry (the man walks along the waves with the rod)')]
for k,o,n,w in fx:
    rep(k,'phrases',o,n,w); rep(k,'recall',o,n,w+'; same fix in recall row')
rep('8028','nouns','стрічка','пов\'язка на голову','la cinta is the chef\'s white headband; bare "стрічка" reads as ribbon')
# recall rows: source has no final period
for k,v in s.items():
    for i,(a,b) in enumerate(zip(v['recall'],t[k]['recall'])):
        if b.endswith('.') and not a.endswith('.'):
            t[k]['recall'][i]=b[:-1]; log.append(f"- {k} recall: {b} -> {b[:-1]} (source recall row has no final period)")
json.dump(t,open(P+'es/ua.json','w'),ensure_ascii=False,indent=1)
open(P+'es/tmp_fixlog_ua_es_b002.txt','w').write('\n'.join(log))
print(len(log))
