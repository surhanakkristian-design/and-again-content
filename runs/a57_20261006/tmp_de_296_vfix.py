import json
def upd(i, fn):
    p=f'content/de/{i}.json'; d=json.load(open(p)); fn(d)
    json.dump(d, open(p,'w'), ensure_ascii=False, indent=1); open(p,'a').write('\n')
def f296(d):
    a=d['recall'][2]['parts'][1]['accept']; assert a[0]=='Holzbrett'; a.append('Schneidebrett')
def f297(d):
    a=d['recall'][0]['parts'][1]['accept']; assert a==['Angel']; a.append('Angelrute')
    b=d['recall'][3]['parts'][0]['accept']; assert b==['angeln']; b.append('fischen')
upd(296,f296); upd(297,f297)
