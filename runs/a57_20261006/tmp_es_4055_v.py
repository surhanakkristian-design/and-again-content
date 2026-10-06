import json
def upd(i, f):
    p=f'content/es/{i}.json'; d=json.load(open(p)); f(d); json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
def f4055(d):
    g=[x for x in d['recall'][3]['parts'] if x.get('gap')][0]; assert g['text']=='dinosaurios'; g['accept']=['dinosaurios','juguetes']
def f665(d):
    g=[x for x in d['recall'][2]['parts'] if x.get('gap')][0]; assert g['text']=='caminar'; g['accept']=['caminar','andar']
    g=[x for x in d['recall'][4]['parts'] if x.get('gap')][0]; assert g['text']=='campo'; g['accept']=['campo','prado']
upd(4055,f4055); upd(665,f665)
