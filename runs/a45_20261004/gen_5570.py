import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ {"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,boxes)]
wl=[0.41,0.42,0.41,0.40,0.40,0.40,0.38,0.35]; wt=[0.15,0.15,0.15,0.15,0.14,0.13,0.14,0.11]
wom=[(l,t,1.0,1.0) for l,t in zip(wl,wt)]
man=[(0.16,0.40,0.40,0.71),(0.15,0.40,0.41,0.72),(0.15,0.40,0.40,0.73),(0.13,0.40,0.40,0.73),(0.11,0.40,0.39,0.75),(0.10,0.40,0.39,0.75),(0.09,0.39,0.38,0.74),(0.09,0.39,0.34,0.74)]
man=[(a,b,min(c,l),d) for (a,b,c,d),l in zip(man,wl)]
mg=[(0.12,0.76,0.41,0.90),(0.11,0.76,0.42,0.91),(0.11,0.77,0.41,0.93),(0.10,0.78,0.40,0.93),(0.08,0.78,0.40,0.94),(0.07,0.78,0.40,0.94),(0.06,0.79,0.38,0.96),(0.06,0.78,0.35,0.97)]
c={"mediaId":5570,"level":"B","keyWord":"ashamed","defaultVoice":"female",
"taps":[{"phrase":"to pull a guilty face","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to clutch his head","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to spill from a basket","target":"the mangoes","voice":"female","keys":K(mg)}],
"stillS":2.2,
"nouns":[{"word":"a scooter","x":0.28,"y":0.75,"voice":"female"},{"word":"mangoes","x":0.26,"y":0.88,"voice":"female"},
{"word":"a hoodie","x":0.72,"y":0.62,"voice":"female"},{"word":"a hoop earring","x":0.76,"y":0.45,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","pulling","a","guilty","face."],"answerVoice":"female",
"notes":"Man clutches his head only 0.2-1.2 s, then puts his hands on his hips. 'spill from a basket' describes the already-spilled mangoes (result state). At 3.7 s the woman's waving hand lies over the man's legs; her box starts at 0.35 so it does not overlap his."}
json.dump(c,open('content/5570.json','w'),indent=1)
