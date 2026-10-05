import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)}) for t,b in zip(T,l)]
wom=K([(0.31,0.34,0.35,0.39),(0.31,0.34,0.35,0.39),(0.30,0.34,0.35,0.40),(0.38,0.33,0.30,0.43),(0.40,0.20,0.27,0.56),(0.40,0.20,0.28,0.56),(0.40,0.20,0.27,0.56),(0.40,0.20,0.29,0.56)])
sign=K([(0.22,0.19,0.20,0.15),(0.22,0.18,0.20,0.16),(0.21,0.18,0.21,0.16),(0.22,0.17,0.20,0.16),(0.20,0.16,0.20,0.20),(0.20,0.16,0.20,0.20),(0.20,0.15,0.20,0.21),(0.19,0.15,0.21,0.21)])
tyre=K([(0.66,0.24,0.34,0.58),(0.66,0.24,0.34,0.58),(0.65,0.25,0.35,0.58),(0.68,0.22,0.32,0.61),(0.67,0.22,0.33,0.62),(0.68,0.21,0.32,0.63),(0.67,0.22,0.33,0.63),(0.69,0.22,0.31,0.63)])
c={"mediaId":7956,"level":"A","keyWord":"quickly","defaultVoice":"female",
"taps":[{"phrase":"to kneel next to the car","target":"the woman","voice":"female","keys":wom},
{"phrase":"to hold up a round sign","target":"the sign holder","voice":"female","keys":sign},
{"phrase":"to carry an old tyre","target":"the crew member","voice":"female","keys":tyre}],
"stillS":2.7,
"nouns":[{"word":"the sky","x":0.32,"y":0.07,"voice":"female"},{"word":"a sign","x":0.25,"y":0.20,"voice":"female"},{"word":"a wheel","x":0.20,"y":0.57,"voice":"female"},{"word":"the ground","x":0.40,"y":0.90,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","changing","a","car","wheel."],"answerVoice":"female",
"notes":"sign holder and tyre carrier wear helmets, gender unclear -> neutral target names, default voice. Sign holder is partly hidden behind the woman: his box covers the sign + head, split from hers just above her helmet (0.2-1.7) / at x 0.40 (2.2-3.7). Answer describes 0.2-1.7; from 2.2 she raises her arm (not used as a phrase: the sign holder and men at the wall also raise arms)."}
json.dump(c,open('content/7956.json','w'),indent=1)
