import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(rows): return [dict(t=t,**dict(zip("xywh",r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
man=K([(0.32,0.36,0.63,0.64),(0.36,0.36,0.59,0.64),(0.34,0.37,0.49,0.63),(0.33,0.37,0.45,0.63),
       (0.32,0.36,0.42,0.61),(0.32,0.36,0.40,0.56)])
storm=K([(0.62,0.08,0.38,0.27),(0.60,0.08,0.40,0.27),(0.57,0.16,0.43,0.20),(0.58,0.12,0.42,0.24),
         (0.55,0.10,0.45,0.25),(0.55,0.08,0.45,0.27)])
d={"mediaId":6877,"level":"B","keyWord":"board up","defaultVoice":"male",
 "taps":[{"phrase":"to hammer in a nail","target":"the young man","voice":"male","keys":man},
         {"phrase":"to turn round in alarm","target":"the young man","voice":"male","keys":man},
         {"phrase":"to darken the sky","target":"the dust storm","voice":"male","keys":storm}],
 "stillS":2.2,
 "nouns":[{"word":"a kiosk","x":0.15,"y":0.12,"voice":"male"},
          {"word":"a dust storm","x":0.78,"y":0.20,"voice":"male"},
          {"word":"a hammer","x":0.43,"y":0.47,"voice":"male"},
          {"word":"an elderly man","x":0.82,"y":0.60,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","boarding","up","the","window."],
 "answerVoice":"male",
 "notes":"Only one clear person target; the elderly man in the background is tiny and his action unclear, so the dust storm is the third target (box kept above the young man's head, palm trees inside it). 'board up' in the answer kept as two chips."}
json.dump(d,open("content/6877.json","w"),indent=1)
