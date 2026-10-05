import json
p='content/5312.json'; d=json.load(open(p))
fl=d['taps'][1]['keys']; bk=d['taps'][2]['keys']
blk={6.0:(0,0.27,0.12,0.36),6.5:(0,0.26,0.13,0.36),7.0:(0,0.29,0.11,0.33),7.5:(0,0.27,0.12,0.35)}
for k in fl:
    if k['t'] in blk:
        bx=blk[k['t']]; right=k['x']+k['w']; k['x']=bx[2]; k['w']=round(right-bx[2],2)
for i,k in enumerate(bk):
    if k['t'] in blk:
        x,y,w,h=blk[k['t']]; bk[i]={'t':k['t'],'x':x,'y':y,'w':w,'h':h}
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
