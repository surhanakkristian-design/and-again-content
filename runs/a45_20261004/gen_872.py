import json
T=[i*0.5 for i in range(21)]
def bx(t,x0,y0,x1,y1): return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
W={0.0:(0,.19,.47,.70),0.5:(0,.21,.47,.70),1.0:(0,.22,.47,.71),1.5:(0,.22,.47,.70),2.0:(0,.22,.47,.70),2.5:(0,.21,.47,.70),
3.0:(0,.22,.47,.71),3.5:(0,.21,.47,.71),4.0:(0,.20,.47,.69),4.5:(0,.21,.48,.70),5.0:(0,.22,.47,.70),5.5:(0,.22,.48,.70),
6.0:(0,.20,.48,.70),6.5:(0,.17,.48,.70),7.0:(0,.12,.44,.70),7.5:(0,.23,.47,.70),8.0:(0,.20,.45,.70),8.5:(0,.20,.48,.70),
9.0:(0,.21,.48,.70),9.5:(0,.22,.48,.70),10.0:(0,.21,.48,.70)}
D={0.0:(.47,.57,.59,.70),0.5:(.47,.57,.59,.70),1.0:(.47,.57,.58,.71),1.5:(.47,.57,.58,.70),2.0:(.47,.55,.59,.70),2.5:(.47,.56,.59,.70),
3.0:(.47,.56,.60,.70),3.5:(.47,.57,.59,.71),4.0:(.47,.56,.61,.70),4.5:(.48,.56,.58,.70),5.0:(.47,.56,.58,.70),5.5:(.48,.55,.58,.70),
6.0:(.48,.54,.58,.69),6.5:(.48,.55,.58,.70),7.0:(.45,.56,.61,.70),7.5:(.47,.58,.59,.70),8.0:(.45,.56,.54,.69),8.5:(.48,.56,.57,.70),
9.0:(.48,.56,.57,.70),9.5:(.48,.55,.56,.70),10.0:(.48,.55,.55,.70)}
M={0.0:(.59,.15,1,.74),0.5:(.59,.16,1,.74),1.0:(.58,.16,1,.74),1.5:(.58,.17,1,.74),2.0:(.49,.12,1,.55),2.5:(.51,.17,1,.56),
3.0:(.49,.18,1,.56),3.5:(.50,.18,1,.57),4.0:(.49,.12,1,.56),4.5:(.58,.15,1,.72),5.0:(.58,.19,1,.72),5.5:(.58,.19,1,.72),
6.0:(.58,.18,1,.72),6.5:(.58,.17,1,.72),7.0:(.44,.08,1,.56),7.5:(.47,.18,1,.58),8.0:(.54,.18,1,.76),8.5:(.57,.14,1,.78),
9.0:(.57,.17,1,.76),9.5:(.56,.17,1,.76),10.0:(.55,.15,1,.78)}
def keys(d): return [bx(t,*d[t]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":872,"level":"A","keyWord":"whistling","defaultVoice":"female",
"taps":[
{"phrase":"to cover her mouth","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to point at his mouth","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to sit between two people","target":"the dog","voice":"female","keys":keys(D)}],
"stillS":0.0,
"nouns":[{"word":"a tree","x":0.30,"y":0.08,"voice":"female"},{"word":"a woman","x":0.22,"y":0.48,"voice":"female"},
{"word":"a man","x":0.76,"y":0.48,"voice":"male"},{"word":"a table","x":0.45,"y":0.82,"voice":"female"}],
"question":"What are they doing?",
"answer":["They","are","whistling","at","the","table."],
"answerVoice":"female",
"notes":"The dog is small and squeezed between the two people (only head and chest visible behind the table), so its box is narrower than 0.18 to avoid overlapping the people; whether it sits is inferred from its upright posture. While the man raises his hand to his mouth (2.0-4.0 s, also 7.0-7.5 s) his box ends above the dog (y about 0.56) and loses his lower body; in the other frames his box starts right of the dog and loses a bit of his forearm. Both people whistle, so whistling is not used as a tap phrase, only in the answer; whistling is seen only as rounded lips without sound. defaultVoice female by evenId (man and woman equally main)."}
json.dump(c,open("content/872.json","w"),indent=1)
