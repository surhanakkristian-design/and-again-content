import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(0.0,0.0,0.74,0.80),(0.0,0.0,0.94,0.82),(0.16,0.10,0.78,0.70),(0.14,0.38,0.44,0.34),(0.10,0.43,0.48,0.25),(0.14,0.27,0.49,0.41),(0.15,0.20,0.53,0.48)])
stew=K([None,None,(0.0,0.24,0.15,0.40),(0.0,0.27,0.13,0.40),(0.0,0.27,0.18,0.16),(0.0,0.27,0.13,0.36),(0.0,0.25,0.14,0.38)])
c={"mediaId":7094,"level":"B","keyWord":"extract","defaultVoice":"female",
"taps":[{"phrase":"to wrench her boot free","target":"the woman","voice":"female","keys":woman},
{"phrase":"to land in a muddy puddle","target":"the woman","voice":"female","keys":woman},
{"phrase":"to wear a high-visibility vest","target":"the steward","voice":"male","keys":stew}],
"stillS":2.2,
"nouns":[{"word":"a steward","x":0.12,"y":0.36,"voice":"male"},{"word":"a tent","x":0.72,"y":0.28,"voice":"female"},
{"word":"a puddle","x":0.45,"y":0.72,"voice":"female"},{"word":"a bucket hat","x":0.27,"y":0.81,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","wrenching","her","boot","out","of","the","mud."],"answerVoice":"female",
"notes":"Woman pulls boot 0.2-1.2 s, falls into the puddle 1.7 s, holds boot up 2.7-3.2 s; answer describes the first half. Steward (orange vest) appears from 1.2 s at the left edge, his box overlaps her in the picture at 2.2 s so it is cut at y 0.43. Friends in ponchos not used as a target (a group). Key word 'extract' is a verb, not placed."}
json.dump(c,open('content/7094.json','w'),indent=1)
