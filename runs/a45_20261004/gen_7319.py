import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
off=None
top=[(0.34,0.20,0.38,0.80),(0.38,0.21,0.32,0.64),(0.40,0.22,0.30,0.47),(0.44,0.22,0.25,0.37),(0.45,0.21,0.20,0.31),(0.48,0.21,0.18,0.27),(0.48,0.22,0.18,0.26),(0.48,0.22,0.18,0.25)]
man=[off,off,off,(0.0,0.80,0.18,0.20),(0.01,0.64,0.33,0.36),(0.0,0.58,0.36,0.42),(0.03,0.56,0.34,0.43),(0.03,0.54,0.34,0.45)]
gate=[off,off,(0.30,0.86,0.22,0.14),(0.33,0.74,0.25,0.26),(0.35,0.62,0.22,0.20),(0.37,0.57,0.21,0.17),(0.38,0.55,0.20,0.17),(0.38,0.55,0.19,0.16)]
k=lambda L:[({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,L)]
c={"mediaId":7319,"level":"A","keyWord":"make a mistake","defaultVoice":"female",
"taps":[{"phrase":"to cover her mouth","target":"the woman on top","voice":"female","keys":k(top)},
{"phrase":"to hold two suitcases","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to wear a red headband","target":"the woman at the gate","voice":"female","keys":k(gate)}],
"stillS":3.2,
"nouns":[{"word":"the sky","x":0.12,"y":0.15,"voice":"female"},{"word":"a pink house","x":0.56,"y":0.12,"voice":"female"},
{"word":"a man","x":0.21,"y":0.68,"voice":"male"},{"word":"flowers","x":0.75,"y":0.76,"voice":"female"}],
"question":"What is the woman on top doing?","answer":["She","is","covering","her","mouth."],"answerVoice":"female",
"notes":"Key word is a phrase, not used as noun. Third phrase is a state (red headband) because the woman at the gate does nothing only she does (she and the man both look up at the house). Man's box stops at x0.37 to stay off the gate woman, so his brown suitcase (x0.33-0.51) is mostly outside his box at 2.7-3.7. Man only a hat edge at 1.7 s."}
json.dump(c,open('content/7319.json','w'),indent=1)
