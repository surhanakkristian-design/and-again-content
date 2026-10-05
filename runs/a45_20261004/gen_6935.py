import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,boxes)]
W=[(0.33,0.19,0.83,0.42),(0.31,0.08,0.83,0.40),(0.31,0.10,0.83,0.41),(0.32,0.11,0.81,0.41),(0.34,0.12,0.68,0.56),(0.33,0.13,0.77,0.52),(0.32,0.14,0.84,0.45),(0.33,0.15,0.85,0.46)]
R=[(0.02,b[3]+0.01,0.55,0.95) for b in W]
w=K(W); r=K(R)
c={"mediaId":6935,"level":"B","keyWord":"center","defaultVoice":"female",
"taps":[{"phrase":"to hang from the steep wall","target":"the woman","voice":"female","keys":w},
{"phrase":"to swing her legs","target":"the woman","voice":"female","keys":w},
{"phrase":"to dangle below the climber","target":"the rope","voice":"female","keys":r}],
"stillS":0.2,
"nouns":[{"word":"a skylight","x":0.33,"y":0.10,"voice":"female"},{"word":"a café counter","x":0.74,"y":0.50,"voice":"female"},{"word":"a ladder","x":0.82,"y":0.65,"voice":"female"},{"word":"mats","x":0.45,"y":0.92,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","hanging","from","the","steep","wall."],"answerVoice":"female",
"notes":"Key word 'center' (climbing centre) is the whole scene, not placeable as a noun. Rope box starts just below the woman's box to avoid overlap; rope is thin and diagonal."}
json.dump(c,open('content/6935.json','w'),ensure_ascii=False,indent=1)
