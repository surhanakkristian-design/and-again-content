import json
p='content/7449.json'; c=json.load(open(p))
w=c['taps'][0]['keys']
upd={0.2:dict(x=0.23,w=0.51),0.7:dict(x=0.23,w=0.52),1.2:dict(w=0.44),1.7:dict(x=0.45,w=0.47),2.2:dict(w=0.45),2.7:dict(w=0.40),3.7:dict(w=0.40)}
for k in w:
    for t,d in upd.items():
        if abs(k['t']-t)<.01: k.update(d)
c['taps'][1]['keys']=json.loads(json.dumps(w))
c['taps'][1]['phrase']='to make a pained face'
qx={0.2:0.22,0.7:0.22,1.2:0.31,1.7:0.32,2.2:0.33,2.7:0.34,3.2:0.32,3.7:0.32}
c['taps'][2]={'phrase':'to queue for the toilet','target':'the people in the queue','voice':'female',
 'keys':[dict(t=t,x=0.0,y=0.27,w=v,h=0.60) for t,v in qx.items()]}
c['question']='What is the red-haired woman doing?'
c['answer']=['She','is','making','a','pained','face.']
json.dump(c,open(p,'w'),indent=1)
