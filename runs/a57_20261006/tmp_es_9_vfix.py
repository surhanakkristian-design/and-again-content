import json
def load(i): return json.load(open(f'content/es/{i}.json'))
def save(i,d): json.dump(d,open(f'content/es/{i}.json','w'),ensure_ascii=False,indent=1)
d=load(9); d['recall'][1]['parts'][0]['accept']=["examinar","observar","mirar"]; save(9,d)
d=load(11); d['recall'][3]['parts'][1]['accept']=["mirando","observando"]; save(11,d)
d=load(14); d['taps'][2]['phrase']="pasar sobre las hojas verdes"
d['recall'][2]['parts'][0]['text']="pasar sobre las"; save(14,d)
