import json
def keys(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def mk(ts, boxes): return keys([(t,)+tuple(b) if b else (t,None) for t,b in zip(ts,boxes)])

# 644
w=mk(T(21),[(0.14,0.25,0.70,0.75),(0.19,0.26,0.74,0.74),(0.17,0.25,0.68,0.75),(0.15,0.27,0.70,0.73),(0.19,0.27,0.69,0.73),
(0.19,0.29,0.68,0.71),(0.25,0.29,0.70,0.71),(0.19,0.29,0.74,0.71),(0.21,0.30,0.76,0.70),(0.22,0.29,0.78,0.71),(0.35,0.29,0.65,0.71),
(0.0,0.14,1.0,0.86),(0.02,0.25,0.98,0.75),(0.19,0.24,0.81,0.76),(0.09,0.24,0.91,0.76),(0.07,0.22,0.93,0.78),(0.02,0.17,0.98,0.83),
(0.02,0.15,0.98,0.85),(0.12,0.15,0.88,0.85),(0.09,0.15,0.91,0.85),(0.05,0.15,0.95,0.85)])
d={"mediaId":644,"level":"A","keyWord":"scared","defaultVoice":"female",
"taps":[{"phrase":"to cover her mouth","target":"the woman","voice":"female","keys":w},
{"phrase":"to carry a white bag","target":"the woman","voice":"female","keys":w},
{"phrase":"to hold a bright phone","target":"the woman","voice":"female","keys":w}],
"stillS":0.0,
"nouns":[{"word":"glasses","x":0.40,"y":0.37,"voice":"female"},{"word":"hair","x":0.68,"y":0.46,"voice":"female"},
{"word":"a bag","x":0.45,"y":0.80,"voice":"female"},{"word":"the floor","x":0.85,"y":0.56,"voice":"female"}],
"question":"What is the scared woman doing?",
"answer":["She","is","covering","her","mouth."],"answerVoice":"female",
"notes":"Only one possible target (the woman), used for all three phrases. Phone is lit only 3.0-4.5 s, mouth covered from 6.0 s, bag carried throughout. Key word 'scared' is in the question. Cars in the background are small and several, not used."}
json.dump(d,open("content/644.json","w"),indent=1,ensure_ascii=False)

# 645
m=mk(T(11),[(0.14,0.20,0.86,0.80),(0.07,0.17,0.93,0.83),(0.17,0.21,0.83,0.79),(0.32,0.24,0.68,0.76),(0.32,0.25,0.68,0.75),
(0.39,0.25,0.61,0.75),(0.32,0.25,0.68,0.75),(0.30,0.24,0.70,0.76),(0.27,0.23,0.73,0.77),(0.55,0.22,0.45,0.78),(0.47,0.25,0.53,0.75)])
d={"mediaId":645,"level":"A","keyWord":"schedule","defaultVoice":"male",
"taps":[{"phrase":"to draw a circle","target":"the man","voice":"male","keys":m},
{"phrase":"to hold a black pen","target":"the man","voice":"male","keys":m},
{"phrase":"to wear a watch","target":"the man","voice":"male","keys":m}],
"stillS":5.0,
"nouns":[{"word":"a schedule","x":0.24,"y":0.20,"voice":"male"},{"word":"a man","x":0.75,"y":0.60,"voice":"male"},
{"word":"a notebook","x":0.38,"y":0.79,"voice":"male"},{"word":"folders","x":0.14,"y":0.70,"voice":"male"}],
"question":"What is the man drawing?",
"answer":["He","is","drawing","a","circle","on","the","schedule."],"answerVoice":"male",
"notes":"Only one possible target (the man). 'to wear a watch' is a state. The schedule is the wall planner; pill near its top, away from the drawn circle. 'folders' and 'a notebook' are close: 0.10 apart in y."}
json.dump(d,open("content/645.json","w"),indent=1,ensure_ascii=False)

# 647
M=[None,None,(0,0,1,0.55),(0,0,1,0.39),(0,0,1,0.36),(0,0,1,0.32),(0,0,1,0.28),(0,0,1,0.27),(0,0,1,0.19),(0,0,1,0.17),(0,0,1,0.19),
(0,0,1,0.26),(0,0,1,0.29),(0,0,1,0.25),(0,0,1,0.20),(0,0,0.27,0.62),(0,0,0.36,0.58),(0,0,0.43,0.49),(0.05,0,0.75,0.30),(0.08,0,0.74,0.31),(0.08,0.04,0.54,0.29)]
G=[None,None,(0.22,0.56,0.58,0.44),(0,0.40,1,0.60),(0.05,0.37,0.90,0.63),(0,0.33,1,0.67),(0,0.29,1,0.71),(0,0.28,1,0.72),(0,0.20,1,0.80),(0,0.18,1,0.82),(0,0.20,1,0.80),
(0.05,0.27,0.90,0.73),(0,0.30,1,0.70),(0,0.26,1,0.74),(0,0.21,1,0.79),(0.28,0.14,0.72,0.86),(0.37,0.17,0.63,0.83),(0.44,0.24,0.56,0.76),(0.05,0.31,0.95,0.69),(0.05,0.32,0.95,0.68),(0.03,0.34,0.97,0.66)]
M=mk(T(21),M); G=mk(T(21),G)
d={"mediaId":647,"level":"A","keyWord":"scissors","defaultVoice":"female",
"taps":[{"phrase":"to cut hair with scissors","target":"the woman in glasses","voice":"female","keys":M},
{"phrase":"to look in a mirror","target":"the woman with long hair","voice":"female","keys":G},
{"phrase":"to sit on a chair","target":"the woman with long hair","voice":"female","keys":G}],
"stillS":2.5,
"nouns":[{"word":"scissors","x":0.30,"y":0.49,"voice":"female"},{"word":"a comb","x":0.76,"y":0.44,"voice":"female"},
{"word":"a towel","x":0.50,"y":0.80,"voice":"female"},{"word":"glasses","x":0.50,"y":0.15,"voice":"female"}],
"question":"What is the woman in glasses doing?",
"answer":["She","is","cutting","hair","with","scissors."],"answerVoice":"female",
"notes":"The two women overlap (one stands behind the other): boxes are split by a horizontal line at the top of the seated woman's hair, so the standing woman's hands (with comb and scissors) fall inside the seated woman's box in 1.0-7.0 s. 0.0-0.5 s shows only a hand with scissors: both off. 7.5-8.5 s split vertically. The seated one is called 'girl/daughter' in the description but looks like a young adult, so named 'the woman with long hair'. The chair is only partly visible (back posts). A cat appears 9.0-10.0 s, not used."}
json.dump(d,open("content/647.json","w"),indent=1,ensure_ascii=False)

# 649
W=[(0.0,0.20,0.45,0.63),(0.0,0.23,0.48,0.60),(0.02,0.22,0.50,0.63),(0.07,0.22,0.47,0.66),(0.04,0.19,0.47,0.64),(0.02,0.19,0.47,0.64),
(0.0,0.20,0.48,0.67),(0.0,0.20,0.47,0.67),(0.0,0.19,0.41,0.69),(0.0,0.19,0.37,0.71),(0.0,0.20,0.36,0.75),(0.0,0.21,0.40,0.74),
(0.0,0.20,0.45,0.63),(0.07,0.21,0.40,0.62),(0.05,0.22,0.41,0.71)]
Mn=[(0.50,0.08,0.48,0.75),(0.51,0.09,0.49,0.74),(0.53,0.08,0.45,0.77),(0.55,0.08,0.45,0.77),(0.52,0.03,0.46,0.80),(0.50,0.11,0.48,0.74),
(0.49,0.11,0.48,0.76),(0.48,0.12,0.49,0.75),(0.42,0.14,0.48,0.72),(0.38,0.17,0.60,0.68),(0.37,0.17,0.50,0.76),(0.41,0.17,0.25,0.21),
(0.46,0.22,0.29,0.17),(0.57,0.24,0.27,0.15),(0.68,0.27,0.22,0.15)]
W=mk(T(15),W); Mn=mk(T(15),Mn)
d={"mediaId":649,"level":"B","keyWord":"scold","defaultVoice":"female",
"taps":[{"phrase":"to scold the young man","target":"the old woman","voice":"female","keys":W},
{"phrase":"to clutch a straw hat","target":"the young man","voice":"male","keys":Mn},
{"phrase":"to fold her arms","target":"the old woman","voice":"female","keys":W}],
"stillS":6.0,
"nouns":[{"word":"a headscarf","x":0.24,"y":0.26,"voice":"female"},{"word":"an apron","x":0.24,"y":0.60,"voice":"female"},
{"word":"a gate","x":0.65,"y":0.47,"voice":"female"},{"word":"cabbages","x":0.55,"y":0.88,"voice":"female"}],
"question":"What is the old woman doing?",
"answer":["She","is","scolding","the","young","man."],"answerVoice":"female",
"notes":"defaultVoice female: the scolding old woman is the main person (mixed pair; evenId false would give male). 1.5-2.5 s her pointing finger reaches into the man's box (split at his body). From 5.5 s only the man's head shows behind the gate. Arms folded only 6.0-7.0 s; hat clutched 2.5-4.5 s. Geese (0-2.5 s) only stand, not used."}
json.dump(d,open("content/649.json","w"),indent=1,ensure_ascii=False)
