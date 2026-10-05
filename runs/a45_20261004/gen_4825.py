import json
K={0.5:(0.80,0.50,0.20,0.36),1.5:(0,0.46,0.62,0.54),2.0:(0,0,0.90,0.70),2.5:(0,0.06,0.65,0.86),3.0:(0,0.28,0.22,0.50),3.5:(0,0.10,0.78,0.38),4.0:(0,0,1,0.62)}
keys=[]
for i in range(17):
    t=i*0.5
    if t in K: x,y,w,h=K[t]; keys.append(dict(t=t,x=x,y=y,w=w,h=h))
    else: keys.append(dict(t=t,off=True))
d={"mediaId":4825,"level":"B","keyWord":"to wipe","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to wipe down the worktop","to stack dirty bowls","to spray foam on the stove"]],
"stillS":6.0,
"nouns":[{"word":"shelves","x":0.22,"y":0.22,"voice":"female"},{"word":"a tap","x":0.85,"y":0.40,"voice":"female"},
{"word":"a sink","x":0.72,"y":0.57,"voice":"female"},{"word":"floorboards","x":0.30,"y":0.86,"voice":"female"}],
"question":"What is the woman wiping?",
"answer":["She","is","wiping","the","dirty","worktop."],"answerVoice":"female",
"notes":"Only one person; mostly only her hands/arm are visible (0.5 s spray hand, 1.5-2.0 s sponge, 3.5-4.0 s cloth); her whole body at 2.5-3.0 s. She is off at 0, 1.0 and 4.5-8.0 s. At 1.5-2.0 s she uses a sponge, at 3.5-4.0 s a cloth. 'the stove' = the black hob being sprayed at 0.5-1.0 s."}
json.dump(d,open("content/4825.json","w"),indent=1)
