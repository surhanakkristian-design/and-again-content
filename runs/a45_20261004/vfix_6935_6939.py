import json
def upd(vid, changes):
    p=f'content/{vid}.json'; c=json.load(open(p))
    for n in c['nouns']:
        if n['word'] in changes: n['x'],n['y']=changes[n['word']]
    json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
upd(6935,{'a skylight':(0.43,0.13),'a ladder':(0.79,0.62)})
upd(6939,{'a curtain':(0.90,0.25),'clothes':(0.67,0.36)})
