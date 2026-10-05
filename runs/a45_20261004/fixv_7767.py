import json
p='content/7767.json'; c=json.load(open(p))
c['taps'][0]['phrase']='to hold the left handle'
boxes={0.2:None,0.7:None,1.2:(0.55,0.40,0.24,0.40),1.7:(0.48,0.40,0.24,0.41),2.2:(0.44,0.40,0.24,0.41),
       2.7:(0.42,0.40,0.22,0.44),3.2:(0.40,0.40,0.22,0.45),3.7:(0.40,0.40,0.22,0.45)}
keys=[]
for t,b in boxes.items():
    keys.append({'t':t,'off':True} if b is None else {'t':t,'x':b[0],'y':b[1],'w':b[2],'h':b[3]})
c['taps'][1]={'phrase':'to drive across the bridge','target':'the cars','voice':'male','keys':keys}
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
