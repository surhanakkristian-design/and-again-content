import json,glob,collections
d=json.load(open('det2.json'))
J={};V={}
for f in sorted(glob.glob('elig/judge_output_*.json')):
    for x in json.load(open(f)): J[str(x['id'])]=x
for f in sorted(glob.glob('elig/verify_output_*.json')):
    for x in json.load(open(f)): V[str(x['id'])]=x
assert set(V)==set(d), (len(V),len(d))
first={}
for k,v in d.items():
    if v['det'] is not None: first[k]=(v['det'],'deterministic: '+v['det_reason'],None)
    else: first[k]=(J[k]['full'],'judge',J[k]['sentence'])
agree=[k for k in d if first[k][0]==V[k]['full']]; dis=[k for k in d if first[k][0]!=V[k]['full']]
print('agree',len(agree),'of',len(d),'disagree',len(dis))
c=collections.Counter((first[k][1].split(':')[0],first[k][0],V[k]['full']) for k in dis); print(c)
json.dump([{'id':int(k),'sentences':d[k]['speech_sentences']} for k in sorted(dis,key=int)],open('elig/tiebreak_input.json','w'),ensure_ascii=False,indent=0)
json.dump({k:{'first':first[k][0],'first_path':first[k][1],'judge_sentence':first[k][2],'verifier':V[k]['full'],'verifier_sentence':V[k]['sentence']} for k in d},open('elig/merged_pre_tiebreak.json','w'),ensure_ascii=False,indent=0)
for k in sorted(dis,key=int)[:400]: print(k,first[k][0],first[k][1][:30],V[k]['full'],d[k]['speech_sentences'])
