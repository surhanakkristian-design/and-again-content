import json
p='content/4008.json'; c=json.load(open(p))
man,dog,tree=c['taps']
def setk(t,tt,b):
    for i,k in enumerate(t['keys']):
        if k['t']==tt: t['keys'][i]={'t':tt,'x':b[0],'y':b[1],'w':b[2],'h':b[3]}
for tt,b in {5.0:(.12,.27,.36,.35),5.5:(.10,.31,.40,.30),9.0:(.50,.14,.50,.46)}.items(): setk(man,tt,b)
for tt,b in {1.0:(.20,.55,.20,.35),1.5:(.20,.52,.23,.38),5.0:(.05,.62,.56,.27),5.5:(.12,.61,.60,.24),9.0:(.34,.60,.49,.28),9.5:(.29,.52,.54,.34)}.items(): setk(dog,tt,b)
def inter(a,b): return a[0]<b[2]-1e-9 and b[0]<a[2]-1e-9 and a[1]<b[3]-1e-9 and b[1]<a[3]-1e-9
for i,k in enumerate(tree['keys']):
    m=man['keys'][i]; d=dog['keys'][i]
    obs=[(o['x'],o['y'],o['x']+o['w'],o['y']+o['h']) for o in (m,d) if not o.get('off')]
    best=None
    xs=sorted({0,.85}|{round(v,2) for o in obs for v in (o[0],o[2]) if 0<v<.85})
    ys=sorted({0,.42,.56}|{round(v,2) for o in obs for v in (o[1],o[3]) if 0<v<.56})
    for x1 in xs:
        for x2 in xs:
            if x2<=x1: continue
            for y2 in ys:
                if y2<=0: continue
                if y2>.42 and x2>.36: continue   # below the crown only the trunk side (left) belongs to the tree
                r=(x1,0,x2,y2)
                if any(inter(r,o) for o in obs): continue
                # weight: must contain crown area; prefer area
                a=(x2-x1)*y2
                if best is None or a>best[0]: best=(a,r)
    r=best[1]
    tree['keys'][i]={'t':k['t'],'x':round(r[0],2),'y':0.0,'w':round(r[2]-r[0],2),'h':round(r[3],2)}
    print(k['t'],tree['keys'][i])
man['phrase']='to reach for an apple'
c['question']='What is the man picking?'
c['answer']=['He','is','picking','apples','off','the','tree.']
for n in c['nouns']:
    if n['word']=='a trunk': n['y']=.51
c['notes']+=" VERIFIER: frames show him picking apples (hands on an apple at 4.5 s, an apple in each hand at 5.0 s), no shaking visible, so phrase 1 and question/answer changed from 'shake' to reach for / pick; tree box enlarged per frame (largest part of the tree clear of man and dog); dog/man splits corrected at 1.0, 1.5, 5.0, 5.5, 9.0, 9.5 s; 'a trunk' pill moved down onto the trunk."
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
