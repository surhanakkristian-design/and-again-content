import json
def ed(i,f):
    p=f'content/de/{i}.json'; c=json.load(open(p)); f(c); json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
def f233(c):
    g=c['recall'][3]['parts'][0]; assert g['text']=='hält'; g['accept']=['hält']
def f235(c):
    g=c['recall'][3]['parts'][0]; assert g['text']=='apportiert'; g['accept']=['apportiert','holt']
def f237(c):
    g=c['recall'][0]['parts'][1]; assert g['text']=='Maul'; g['accept']=['Maul']
    g=c['recall'][2]['parts'][1]; assert g['text']=='Futter'; g['accept']=['Futter','Nahrung']
ed(233,f233);ed(235,f235);ed(237,f237)
