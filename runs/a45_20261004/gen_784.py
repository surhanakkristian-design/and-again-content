import json
def K(ts, rows):
    out=[]
    for t,r in zip(ts,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def dump(d): json.dump(d, open(f"content/{d['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# 784
ts=T(9)
woman=K(ts,[(0.34,0.30,0.52,0.70),(0.34,0.30,0.52,0.70),(0.08,0.31,0.70,0.69),(0.08,0.31,0.75,0.69),(0.08,0.30,0.74,0.70),(0.08,0.30,0.78,0.70),(0.27,0.47,0.73,0.53),(0.27,0.47,0.73,0.53),(0.27,0.47,0.73,0.53)])
umb=K(ts,[(0,0,1,0.30),(0,0,1,0.30),(0,0,1,0.31),(0,0,1,0.31),(0,0,1,0.30),(0,0,1,0.30),(0,0,1,0.45),(0,0,1,0.45),(0,0,1,0.45)])
dump({"mediaId":784,"level":"B","keyWord":"tilt","defaultVoice":"female",
"taps":[{"phrase":"to tilt the beach umbrella","target":"the woman","voice":"female","keys":woman},
{"phrase":"to settle into a deck chair","target":"the woman","voice":"female","keys":woman},
{"phrase":"to provide some shade","target":"the umbrella","voice":"female","keys":umb}],
"stillS":2.5,
"nouns":[{"word":"a beach umbrella","x":0.45,"y":0.12,"voice":"female"},{"word":"sunglasses","x":0.48,"y":0.47,"voice":"female"},{"word":"a jumpsuit","x":0.48,"y":0.64,"voice":"female"},{"word":"a deck chair","x":0.80,"y":0.80,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","tilting","the","beach","umbrella."],"answerVoice":"female",
"notes":"Only two targets (woman, umbrella). Umbrella box = the canopy only (the pole runs through the woman's hands and is left out so the boxes do not overlap); the split line is the top of her headwrap. 'to provide some shade' is a function rather than a visible action."})

# 786
ts=T(21)
man=K(ts,[(0.31,0.22,0.40,0.18),(0.30,0.20,0.40,0.19),(0.28,0.19,0.46,0.22),(0.28,0.19,0.48,0.22),(0.28,0.21,0.55,0.23),(0.15,0.19,0.48,0.20),(0.12,0.20,0.54,0.35),(0.05,0.15,0.55,0.29),(0.04,0.21,0.76,0.33),(0.0,0.07,0.90,0.43),
(0.02,0.02,0.48,0.96),(0.0,0.29,0.92,0.28),(0.0,0.07,0.67,0.93),(0.08,0.12,0.92,0.40),(0.0,0.25,0.62,0.75),(0.0,0.20,0.80,0.80),(0.0,0.20,0.77,0.80),(0.0,0.19,0.81,0.81),(0.0,0.19,0.81,0.81),(0.0,0.19,0.81,0.81),(0.0,0.17,0.81,0.83)])
box=K(ts,[(0.30,0.40,0.35,0.18),(0.26,0.39,0.42,0.21),(0.25,0.41,0.43,0.24),(0.19,0.41,0.50,0.24),(0.24,0.44,0.53,0.29),(0.38,0.39,0.57,0.33),(0.27,0.55,0.68,0.36),(0.24,0.44,0.76,0.47),(0.22,0.54,0.78,0.45),(0.23,0.50,0.77,0.50),
(0.50,0.40,0.50,0.60),(0.58,0.57,0.42,0.33),(0.68,0.44,0.32,0.38),(0.64,0.52,0.36,0.20),(0.63,0.51,0.37,0.24),(0.80,0.50,0.20,0.16),(0.78,0.50,0.22,0.19),(0.82,0.49,0.18,0.18),(0.82,0.48,0.18,0.16),(0.82,0.46,0.18,0.14),(0.82,0.47,0.18,0.16)])
dump({"mediaId":786,"level":"A","keyWord":"tired","defaultVoice":"male",
"taps":[{"phrase":"to carry a heavy box","target":"the man","voice":"male","keys":man},
{"phrase":"to sit down and rest","target":"the man","voice":"male","keys":man},
{"phrase":"to be made of wood","target":"the box","voice":"male","keys":box}],
"stillS":7.0,
"nouns":[{"word":"a wall","x":0.45,"y":0.12,"voice":"male"},{"word":"sand","x":0.78,"y":0.45,"voice":"male"},{"word":"a man","x":0.33,"y":0.56,"voice":"male"},{"word":"a box","x":0.80,"y":0.63,"voice":"male"}],
"question":"How does the man feel?","answer":["He","is","very","tired."],"answerVoice":"male",
"notes":"Man and box overlap for most of the clip (he carries it in front of his body): while he carries it the man's box is the part of him above the box lid (head, shoulders), at 5.0 and 6.0 the part of him left of the box. A small boy is visible for one frame at 0.5 s on the right; no phrase fits him. 'to be made of wood' is a state: the box does nothing by itself."})

# 787
ts=T(11)
full=(0.0,0.03,1.0,0.97)
white=K(ts,[(0.12,0.17,0.74,0.47),(0.32,0.16,0.55,0.48),(0.27,0.20,0.56,0.60),None,None,None,None,None,(0.05,0.19,0.57,0.52),(0.05,0.18,0.56,0.55),(0.0,0.14,0.63,0.80)])
black=K(ts,[(0.44,0.64,0.56,0.33),(0.40,0.64,0.60,0.33),(0.36,0.80,0.64,0.20),full,full,full,full,full,(0.62,0.19,0.38,0.81),(0.62,0.18,0.38,0.82),(0.63,0.14,0.37,0.86)])
dump({"mediaId":787,"level":"B","keyWord":"to judge","defaultVoice":"female",
"taps":[{"phrase":"to raise her eyebrows","target":"the woman in black","voice":"female","keys":black},
{"phrase":"to wear a white blouse","target":"the woman in white","voice":"female","keys":white},
{"phrase":"to wear a wristwatch","target":"the woman in white","voice":"female","keys":white}],
"stillS":4.5,
"nouns":[{"word":"a pillar","x":0.30,"y":0.08,"voice":"female"},{"word":"sunglasses","x":0.33,"y":0.26,"voice":"female"},{"word":"a bracelet","x":0.56,"y":0.55,"voice":"female"},{"word":"a wristwatch","x":0.36,"y":0.66,"voice":"female"}],
"question":"What is the woman in black doing?","answer":["She","is","raising","her","eyebrows","at","her","friend."],"answerVoice":"female",
"notes":"The key word 'to judge' is not visible, so it is not used. Both women smile and clink glasses, so the woman in white only gets states (blouse, wristwatch). In the first shot (0-1.0 s) the woman in black is only an arm and a hand holding the glass at the bottom right: boxed there. In the last shot her reaching hands left of x 0.62 are outside her box (split between the two women). Bracelet and wristwatch pills are fairly close (0.11 in y)."})

# 789
ts=T(21)
toaster=K(ts,[(0.12,0.50,0.78,0.50),(0.07,0.46,0.86,0.54),(0.07,0.38,0.84,0.62),(0.05,0.14,0.83,0.60),(0.06,0.14,0.84,0.65),(0.09,0.28,0.77,0.62),(0.18,0.57,0.61,0.43),(0.20,0.57,0.58,0.43),(0.20,0.49,0.60,0.51),(0.18,0.49,0.64,0.51),
(0.16,0.59,0.66,0.41),(0.16,0.58,0.68,0.42),(0.16,0.49,0.68,0.51),(0.14,0.49,0.72,0.51),(0.18,0.74,0.61,0.26),None,(0.25,0.70,0.50,0.30),(0.22,0.72,0.56,0.28),(0.22,0.75,0.52,0.25),(0.26,0.75,0.52,0.25),(0.22,0.75,0.53,0.25)])
man=K(ts,[(0.0,0.0,0.50,0.50),(0.0,0.0,0.50,0.46),(0.0,0.0,0.48,0.38),None,None,(0.0,0.0,0.48,0.28),(0.0,0.01,0.50,0.56),(0.0,0.11,0.50,0.46),(0.0,0.10,0.51,0.39),(0.0,0.09,0.51,0.40),
(0.0,0.09,0.51,0.50),(0.0,0.07,0.53,0.51),(0.0,0.05,0.53,0.44),(0.0,0.04,0.55,0.45),(0.0,0.17,0.53,0.57),(0.0,0.36,0.61,0.46),(0.0,0.17,0.53,0.39),(0.0,0.15,0.50,0.43),(0.0,0.11,0.49,0.50),(0.0,0.16,0.50,0.45),(0.0,0.18,0.47,0.43)])
dog=K(ts,[None]*15+[(0.40,0.82,0.22,0.16),(0.38,0.56,0.24,0.14),(0.39,0.58,0.22,0.14),(0.37,0.61,0.22,0.14),(0.43,0.61,0.20,0.14),(0.41,0.61,0.22,0.14)])
dump({"mediaId":789,"level":"A","keyWord":"toaster","defaultVoice":"male",
"taps":[{"phrase":"to bite into his toast","target":"the man with the beard","voice":"male","keys":man},
{"phrase":"to make the bread hot","target":"the toaster","voice":"male","keys":toaster},
{"phrase":"to sit on the floor","target":"the dog","voice":"male","keys":dog}],
"stillS":4.0,
"nouns":[{"word":"a beard","x":0.26,"y":0.42,"voice":"male"},{"word":"jam","x":0.12,"y":0.65,"voice":"male"},{"word":"bread","x":0.86,"y":0.73,"voice":"male"},{"word":"a toaster","x":0.48,"y":0.84,"voice":"male"}],
"question":"What are the men looking at?","answer":["They","are","looking","at","the","toaster."],"answerVoice":"male",
"notes":"The dog is small and in the background, visible only from 7.5 s; its box is the minimum size and sits between the bearded man's box (cut off above it) and the toaster. Bearded man is off at 1.5 and 2.0 (only shirt and unidentifiable hands in the picture); toaster off at 7.5 (only its top edge at the very bottom). The man with long hair has no phrase and no box. The bitten-into toast is clear only at 9.5-10 s."})
