import json
out={};cur=None
for line in open('tmp_tr_cz_es_b001.txt',encoding='utf-8'):
    line=line.rstrip('\n')
    if line.startswith('## '): cur=line[3:].strip(); out[cur]={'captions':{}}; continue
    if not line.strip(): continue
    k,v=line[0],line[2:]
    sp=lambda s:[x.strip() for x in s.split('|')]
    if k=='P': out[cur]['phrases']=sp(v)
    elif k=='N': out[cur]['nouns']=sp(v)
    elif k=='Q': out[cur]['question']=v.strip()
    elif k=='A': out[cur]['answer']=v.strip()
    elif k=='R': out[cur]['recall']=sp(v)
src=json.load(open('tr/b001/source_es.json'))
res={i:{'phrases':out[i]['phrases'],'nouns':out[i]['nouns'],'question':out[i]['question'],'answer':out[i]['answer'],'captions':{},'recall':out[i]['recall']} for i in src}
json.dump(res,open('tr/b001/es/cz.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
