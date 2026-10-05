import json,sys
def apply(i,edits,extra=None):
    f=f'content/{i}.json'; c=json.load(open(f)); n=0
    for targ,t,box in edits:
        for tap in c['taps']:
            if tap['target']!=targ: continue
            for j,k in enumerate(tap['keys']):
                if abs(k['t']-t)<1e-6:
                    tap['keys'][j]={'t':k['t'],'off':True} if box is None else {'t':k['t'],'x':box[0],'y':box[1],'w':box[2],'h':box[3]}
        n+=1
    if extra: extra(c)
    json.dump(c,open(f,'w'),indent=1,ensure_ascii=False); print(i,'box edits',n)
if __name__=='__main__':
    apply(443,[
     ('the woman',0.0,(0,0.25,0.24,0.75)),
     ('the woman',5.5,(0,0.15,0.16,0.85)),
     ('the woman',6.5,(0,0.2,0.5,0.8)),
     ('the woman',7.0,(0.03,0.2,0.49,0.8)),
     ('the man',2.5,(0.72,0.06,0.28,0.94)),
     ('the man',7.0,(0.55,0.13,0.45,0.87)),
     ('the toy horse',4.0,(0,0.5,0.2,0.32)),
     ('the toy horse',5.0,(0.18,0.43,0.54,0.53)),
     ('the toy horse',5.5,(0.42,0.48,0.52,0.52)),
     ('the toy horse',9.0,(0.58,0.61,0.22,0.39)),
     ('the toy horse',9.5,(0.58,0.61,0.22,0.39)),
    ])
