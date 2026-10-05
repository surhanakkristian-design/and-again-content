import json
times=[i*0.5 for i in range(26)]
Wm={0.0:(0.42,0.38,0.58,0.58),0.5:(0.46,0.35,0.54,0.61),1.0:(0.56,0.38,0.44,0.60),1.5:(0.53,0.36,0.47,0.62),2.0:(0.24,0.30,0.62,0.63),2.5:(0.44,0.31,0.56,0.65),
3.0:(0.10,0.26,0.80,0.74),3.5:(0.50,0.25,0.47,0.75),4.0:(0.44,0.25,0.40,0.64),4.5:(0.43,0.26,0.28,0.46),5.0:(0.43,0.27,0.30,0.59),5.5:(0.45,0.27,0.33,0.70),
6.0:(0.46,0.26,0.38,0.58),6.5:(0.42,0.14,0.40,0.73),7.0:(0.38,0.25,0.50,0.66),7.5:(0.55,0.51,0.34,0.25),8.0:(0.60,0.65,0.20,0.16)}
Mn={3.5:(0.12,0.38,0.38,0.60),4.0:(0.06,0.32,0.38,0.55),4.5:(0.06,0.33,0.37,0.49),5.0:(0.06,0.34,0.37,0.66),5.5:(0.08,0.34,0.37,0.66),6.0:(0.09,0.32,0.37,0.60),
6.5:(0.0,0.24,0.42,0.76),7.0:(0.0,0.23,0.38,0.77),7.5:(0.0,0.21,0.52,0.79),8.0:(0.0,0.20,0.45,0.78),8.5:(0.06,0.33,0.40,0.62),9.0:(0.11,0.36,0.43,0.60),
9.5:(0.40,0.48,0.24,0.38),10.0:(0.45,0.52,0.18,0.15),10.5:(0.43,0.53,0.18,0.14),11.0:(0.43,0.54,0.18,0.14),11.5:(0.43,0.54,0.18,0.14),12.0:(0.43,0.54,0.18,0.14),12.5:(0.43,0.54,0.18,0.14)}
def keys(T):
    return [({"t":t,"x":T[t][0],"y":T[t][1],"w":T[t][2],"h":T[t][3]} if t in T else {"t":t,"off":True}) for t in times]
d={"mediaId":4070,"level":"B","keyWord":"wing","defaultVoice":"female",
"taps":[
 {"phrase":"to release her grip first","target":"the woman","voice":"female","keys":keys(Wm)},
 {"phrase":"to wear a protective helmet","target":"the man","voice":"male","keys":keys(Mn)},
 {"phrase":"to dangle beside the wheel","target":"the man","voice":"male","keys":keys(Mn)}],
"stillS":4.5,
"nouns":[{"word":"a wing","x":0.55,"y":0.10,"voice":"female"},{"word":"a helmet","x":0.28,"y":0.50,"voice":"female"},{"word":"a wheel","x":0.12,"y":0.63,"voice":"female"},{"word":"the coast","x":0.76,"y":0.80,"voice":"female"}],
"question":"What are the two people doing?",
"answer":["They","are","dangling","under","the","wing."],
"answerVoice":"female",
"notes":"Cabin shot 0-2.5 s is dark and seen from behind: the blond person on the right is boxed as the woman (same blond hair and rig as outside); the man cannot be told apart there, so he is off until 3.5 s (at 3.0 s the woman hides him). Woman is off from 8.5 s (fallen out of sight). The man is a tiny falling speck from 10.5 s (minimum box), hardly visible at 12.0-12.5 s. Both phrases for the man are things only he does or has (helmet; he hangs next to the wheel, the woman on his far side). defaultVoice female by the evenId rule (a man and a woman)."}
json.dump(d,open("content/4070.json","w"),indent=1)
