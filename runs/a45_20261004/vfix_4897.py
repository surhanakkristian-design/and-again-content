import json
p='content/4897.json'; d=json.load(open(p))
times=[k['t'] for k in d['taps'][0]['keys']]
bb={6.5:(0.04,0.53,0.33,0.47),7.0:(0.31,0.54,0.33,0.46),7.5:(0.62,0.47,0.36,0.53)}
keys=[]
for t in times:
    if t in bb:
        x,y,w,h=bb[t]; keys.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    else: keys.append({"t":t,"off":True})
d['taps'][0]={"phrase":"to carry a brown bag","target":"the blonde woman in white","voice":"female","keys":keys}
t1=d['taps'][1]
t1['phrase']="to wear a brown jacket"; t1['target']="the woman with the black bag"
for k in t1['keys']:
    if k['t']==2.5: k.update({"x":0.66,"y":0.49,"w":0.2,"h":0.35})
d['answer']=["They","are","joining","a","big","group","hug."]
d['notes']+=" | VERIFIER: white-T man replaced (other men/women in white T-shirts at 6.5-9.0) by the blonde woman with the unique brown bag (6.5-7.5); 'black bag' not unique (other black bags 4.5-8.5) -> 'to wear a brown jacket'; answer 'a big group hug'."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
