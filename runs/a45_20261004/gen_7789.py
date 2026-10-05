import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
blo=K([(.01,.25,.26,.56),(.05,.24,.22,.57),(.01,.23,.24,.58),(.04,.23,.23,.58),(0,.21,.30,.62),(0,.21,.22,.62),(0,.30,.21,.58),(0,.35,.22,.53)])
tub=K([(.27,.40,.41,.30),(.27,.40,.42,.30),(.25,.40,.43,.30),(.27,.40,.44,.31),(.30,.38,.41,.33),(.22,.38,.49,.34),(.21,.36,.52,.38),(.22,.37,.52,.38)])
man=K([(.69,.38,.31,.40),(.71,.37,.29,.42),(.69,.38,.31,.39),(.72,.38,.28,.43),(.72,.37,.28,.44),(.72,.36,.28,.45),(.74,.36,.26,.47),(.75,.36,.25,.47)])
d={"mediaId":7789,"level":"B","keyWord":"cooling","defaultVoice":"female",
"taps":[
 {"phrase":"to empty the metal bucket","target":"the blonde woman","voice":"female","keys":blo},
 {"phrase":"to shiver in icy water","target":"the woman in pink","voice":"female","keys":tub},
 {"phrase":"to cool his knees","target":"the man with ice packs","voice":"male","keys":man}],
"stillS":2.7,
"nouns":[{"word":"a skylight","x":0.70,"y":0.06,"voice":"female"},
 {"word":"a bucket","x":0.12,"y":0.59,"voice":"female"},
 {"word":"ice packs","x":0.86,"y":0.62,"voice":"female"},
 {"word":"a tub","x":0.45,"y":0.82,"voice":"female"}],
"question":"Where is the woman in pink sitting?",
"answer":["She","is","sitting","in","a","tub","of","icy","water."],
"answerVoice":"female",
"notes":"Blonde woman and the woman in the tub overlap (bucket/arms over the tub woman's shoulder); boxes split vertically between their bodies, so the bucket above the tub woman's head is not in the blonde's box at 0.2-1.7. Blonde empties the bucket 0.2-1.7 only. 'to cool his knees' = ice packs on his knees (key word cooling); the man in the background gym is not a target."}
json.dump(d,open('content/7789.json','w'),indent=1)
