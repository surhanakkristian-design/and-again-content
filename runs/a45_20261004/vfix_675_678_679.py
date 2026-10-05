import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(tap,t,b):
    for k in tap['keys']:
        if abs(k['t']-t)<0.01:
            k.clear(); k.update({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
c=load(675)
B={0.0:(0,0,.50,.62),0.5:(0,0,.68,.60),1.0:(0,0,.68,.62),1.5:(0,0,.72,.60),2.0:(0,0,.50,.60),2.5:(0,0,.55,.60),3.0:(0,0,.44,.62),3.5:(0,0,.38,.62),4.0:(.05,0,.95,.50)}
for t,b in B.items(): setk(c['taps'][2],t,b)
setk(c['taps'][0],0.5,(.68,.42,.24,.52))
setk(c['taps'][1],0.5,(.92,.44,.08,.34))
c['answer']=["He","is","painting","the","side","of","the","boat."]
save(675,c)
c=load(678); c['taps'][0]['phrase']="to hold up the silk"; save(678,c)
c=load(679); c['taps'][0]['phrase']="to clean the silver"; c['taps'][2]['phrase']="to hang above her head"; save(679,c)
