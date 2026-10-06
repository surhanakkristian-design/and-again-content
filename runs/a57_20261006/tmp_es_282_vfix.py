import json
def ed(i,f):
    p=f'content/es/{i}.json'; d=json.load(open(p)); f(d); json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
def gap(row): return [x for x in row['parts'] if x.get('gap')][0]
def f282(d):
    gap(d['recall'][0])['accept']=['aplicar','extender','poner']
    gap(d['recall'][3])['accept']=['sombra de ojos','sombra']
def f283(d):
    gap(d['recall'][2])['accept']=['abrazar']
def f284(d):
    gap(d['recall'][0])['accept']=['diadema','cinta']
def f285(d):
    gap(d['recall'][2])['accept']=['escalones']
    gap(d['recall'][3])['accept']=['foto','fotografía']
for i,f in [(282,f282),(283,f283),(284,f284),(285,f285)]: ed(i,f)
