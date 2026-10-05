import json
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),ensure_ascii=False,indent=1)

# 4683
t=T(25)
cook={0.0:(0,0.02,1,0.62),0.5:(0,0,1,0.72),1.0:(0,0,0.98,0.66),1.5:(0,0.02,1,0.66),2.0:(0,0.02,0.95,0.6),2.5:(0,0.02,1,0.62),
3.0:(0,0,0.97,0.64),3.5:(0.02,0,0.98,0.64),4.0:(0,0,1,0.6),4.5:(0,0,1,0.6),5.0:(0,0,1,0.62),5.5:(0,0,1,0.62),6.0:(0,0,1,0.6),
6.5:(0.08,0,0.92,0.62),7.0:(0.08,0,0.92,0.68),7.5:(0.05,0,0.95,0.68),8.0:(0.05,0,0.95,0.6),8.5:(0.05,0,0.95,0.68),9.0:(0,0.02,0.97,0.66),
9.5:(0.08,0.05,0.9,0.66),10.0:(0.1,0.07,0.8,0.55),10.5:(0.02,0.04,0.95,0.58),11.0:(0,0.03,0.9,0.7),11.5:(0,0.03,0.9,0.7),12.0:(0,0.03,0.85,0.6)}
k=keys(t,cook)
save({"mediaId":4683,"level":"A","keyWord":"rice","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the cook","voice":"male","keys":k} for p in ["to fill a big bowl","to pour red sauce","to ring a bell"]],
"stillS":1.0,
"nouns":[{"word":"rice","x":0.50,"y":0.71,"voice":"male"},{"word":"a hat","x":0.52,"y":0.07,"voice":"male"},{"word":"a cook","x":0.62,"y":0.36,"voice":"male"}],
"question":"What is the cook doing?","answer":["He","is","filling","a","big","bowl","with","food."],"answerVoice":"male",
"notes":"Only one clear actor (the cook); the background guests do nothing identifiable, so all three phrases share him. His box includes the ladle and his hands. The bell appears only at 11.0-12.0, the red sauce at 4.0-6.5. Still at 1.0 s: the rice is uncovered only at 0.5-1.0."})

# 4684
t=T(19)
B={0.0:(0,0.2,0.40,0.62),0.5:(0,0.2,0.48,0.62),1.0:(0,0.27,0.29,0.68),6.5:(0,0.15,0.42,0.42),7.0:(0,0.08,0.50,0.68),
7.5:(0,0.12,0.21,0.72),8.0:(0,0.14,0.24,0.64),8.5:(0,0.19,0.22,0.58),9.0:(0,0.12,0.42,0.68)}
W={0.0:(0.40,0.22,0.60,0.60),0.5:(0.48,0.22,0.52,0.60),1.0:(0.30,0.24,0.70,0.70),1.5:(0.08,0.22,0.72,0.74),2.0:(0,0.2,0.41,0.52),
2.5:(0,0.2,0.31,0.52),3.0:(0,0.22,0.32,0.50),3.5:(0,0.24,0.38,0.5),4.0:(0,0.2,0.58,0.52),4.5:(0,0.16,0.24,0.48),5.5:(0,0.17,0.55,0.50),6.0:(0,0.13,0.52,0.55)}
M={2.0:(0.41,0.2,0.59,0.62),2.5:(0.31,0.18,0.69,0.64),3.0:(0.32,0.2,0.68,0.62),3.5:(0.42,0.2,0.58,0.74),4.0:(0.58,0.22,0.42,0.6),
4.5:(0.24,0.30,0.40,0.52),5.0:(0,0.38,0.18,0.54),7.5:(0.21,0.22,0.22,0.16),8.0:(0.24,0.22,0.32,0.28),8.5:(0.22,0.27,0.38,0.27)}
save({"mediaId":4684,"level":"B","keyWord":"elbow","defaultVoice":"female",
"taps":[{"phrase":"to wear a mustard beanie","target":"the man in the beanie","voice":"male","keys":keys(t,B)},
{"phrase":"to have a blonde ponytail","target":"the blonde woman","voice":"female","keys":keys(t,W)},
{"phrase":"to point at his colleague","target":"the man in the blue shirt","voice":"male","keys":keys(t,M)}],
"stillS":0.0,
"nouns":[{"word":"a beanie","x":0.15,"y":0.28,"voice":"female"},{"word":"an elbow","x":0.40,"y":0.61,"voice":"female"},
{"word":"a laptop","x":0.15,"y":0.80,"voice":"female"},{"word":"a mouse","x":0.72,"y":0.87,"voice":"female"}],
"question":"How are the colleagues greeting each other?","answer":["They","are","bumping","elbows","with","each","other."],"answerVoice":"female",
"notes":"Everyone bumps elbows, so two phrases are states (beanie, ponytail); only the pointing (2.0-3.5) is an action unique to one person. People overlap heavily: at 4.0-4.5 the woman's arm crosses the man in the blue shirt, boxes split by a vertical line near the faces. At 5.0 only her arm is left in frame (off); at 5.5-7.0 the man in the blue shirt is mostly hidden behind others (off); at 6.5 his face is inside the beanie man's box. At 7.5-8.5 the beanie man's box is cut to his head/torso column so the bearded man behind him gets his own box; at 9.0 only an arm of the blue shirt shows (off). 'an elbow' pill sits where the two elbows touch; a second laptop is cut off at the right edge of the still."})

# 4686
t=T(19)
Wk={0.0:(0,0.02,0.88,0.95),0.5:(0,0.02,0.88,0.95),1.0:(0,0.02,0.90,0.95),1.5:(0,0.36,0.85,0.64),2.0:(0,0.33,0.80,0.67),2.5:(0,0.36,0.85,0.64),
3.0:(0,0.22,0.90,0.78),3.5:(0,0.25,0.92,0.75),4.0:(0,0.38,0.75,0.62),4.5:(0,0.40,0.68,0.55),5.0:(0.21,0.52,0.50,0.34),
5.5:(0.05,0.18,0.85,0.82),6.0:(0.05,0.18,0.85,0.82),6.5:(0.05,0.18,0.87,0.82),7.0:(0.05,0.18,0.44,0.82),7.5:(0.05,0.18,0.44,0.82),
8.0:(0.03,0.2,0.47,0.80),8.5:(0,0.2,0.52,0.8),9.0:(0,0.2,0.51,0.8)}
By={5.0:(0,0.36,0.20,0.26),7.0:(0.50,0.42,0.15,0.50),7.5:(0.50,0.41,0.16,0.48),8.0:(0.51,0.40,0.16,0.40),8.5:(0.53,0.39,0.16,0.40),9.0:(0.52,0.41,0.16,0.50)}
kw=keys(t,Wk)
save({"mediaId":4686,"level":"A","keyWord":"repair","defaultVoice":"female",
"taps":[{"phrase":"to repair the lights","target":"the woman in the yellow hat","voice":"female","keys":kw},
{"phrase":"to hold some wires","target":"the woman in the yellow hat","voice":"female","keys":kw},
{"phrase":"to hold a small light","target":"the boy","voice":"male","keys":keys(t,By)}],
"stillS":7.5,
"nouns":[{"word":"a hat","x":0.27,"y":0.30,"voice":"female"},{"word":"a man","x":0.63,"y":0.35,"voice":"male"},
{"word":"a boy","x":0.59,"y":0.49,"voice":"male"},{"word":"tools","x":0.28,"y":0.84,"voice":"female"}],
"question":"What is the woman with tools doing?","answer":["She","is","repairing","the","lights."],"answerVoice":"female",
"notes":"Close-ups 1.5-5.0 show only her gloved hands: the box is on the hands. The boy is identifiable at 5.0 and 7.0-9.0; at 0.0-1.0 and 5.5-6.5 the light is held by a dark shape that cannot be told apart (boy off) - weak spot: the torch at 0.0-1.0 seems to be held by an adult silhouette. At 7.0-9.0 her arm reaches across in front of the family; her box is cut at x 0.5 so it does not overlap the boy. The mother stands close to the man and the boy on the still; 'a man' pill is shifted right, away from her."})

# 4688
t=T(25)
F={0.0:(0,0.14,0.56,0.28),0.5:(0,0.14,0.56,0.28),1.0:(0,0.13,0.56,0.30),1.5:(0,0.11,0.57,0.30),2.0:(0,0.06,0.55,0.30),2.5:(0,0.04,0.56,0.28),
3.0:(0,0.02,0.52,0.28),3.5:(0,0.02,0.52,0.25),4.0:(0,0,0.28,0.54),4.5:(0,0,0.30,0.54),5.0:(0,0.03,0.34,0.62),5.5:(0,0.03,0.35,0.66),
6.0:(0,0.06,0.33,0.56),6.5:(0,0.13,0.33,0.52),7.0:(0,0.26,0.28,0.66),7.5:(0,0.35,0.24,0.63),8.0:(0,0.42,0.18,0.54),8.5:(0,0.48,0.18,0.50),
9.0:(0,0.45,0.18,0.55),9.5:(0,0.43,0.17,0.57),10.0:(0,0.4,0.22,0.58),10.5:(0,0.35,0.27,0.63),11.0:(0,0.30,0.38,0.68),11.5:(0,0.22,0.38,0.70),12.0:(0,0.14,0.22,0.48)}
Wh={0.0:(0.27,0.42,0.68,0.58),0.5:(0.27,0.43,0.68,0.57),1.0:(0.27,0.44,0.68,0.56),1.5:(0.25,0.42,0.72,0.58),2.0:(0.22,0.37,0.78,0.63),2.5:(0.2,0.33,0.8,0.67),
3.0:(0.2,0.31,0.8,0.69),3.5:(0.2,0.27,0.8,0.73),4.0:(0.29,0.05,0.71,0.92),4.5:(0.30,0.30,0.70,0.65),5.0:(0.34,0.22,0.66,0.76),5.5:(0.35,0.18,0.65,0.80),
6.0:(0.33,0.2,0.67,0.72),6.5:(0.33,0.18,0.67,0.77),7.0:(0.28,0.1,0.72,0.82),7.5:(0.24,0.04,0.76,0.92),8.0:(0.18,0.02,0.82,0.92),8.5:(0.18,0.03,0.82,0.93),
9.0:(0.18,0.08,0.82,0.9),9.5:(0.17,0.15,0.83,0.82),10.0:(0.22,0.22,0.78,0.70),10.5:(0.27,0.27,0.73,0.55),11.0:(0.38,0.35,0.42,0.32),11.5:(0.40,0.38,0.42,0.22)}
kwh=keys(t,Wh)
save({"mediaId":4688,"level":"B","keyWord":"massive","defaultVoice":"male",
"taps":[{"phrase":"to glide beneath the surface","target":"the whale","voice":"male","keys":kwh},
{"phrase":"to emerge from the sea","target":"the whale","voice":"male","keys":kwh},
{"phrase":"to grip the white rope","target":"the man in front","voice":"male","keys":keys(t,F)}],
"stillS":10.5,
"nouns":[{"word":"the sky","x":0.55,"y":0.10,"voice":"male"},{"word":"a whale","x":0.68,"y":0.48,"voice":"male"},
{"word":"a raincoat","x":0.15,"y":0.64,"voice":"male"},{"word":"foam","x":0.72,"y":0.80,"voice":"male"}],
"question":"What is the whale doing?","answer":["The","massive","whale","is","emerging","from","the","sea."],"answerVoice":"male",
"notes":"Both men lean over the rail and gape, so the man's phrase is the rope: the hand closed round the white line belongs to the front man (clear at 6.0-7.5 and 9.0-11.5; at 0.0-3.5 his hands are hardly in frame). Weak spot for the verifier. The second man behind him is kept out of the box where possible; at 12.0 the two heads cannot be separated cleanly. At 0.0-3.5 the whale is a dark shape under water and the man's box is cut at his chin so it does not overlap it; at 4.5-6.5 the vertical split gives the man the strip up to his face. Whale off at 12.0 (only the splash). Both men wear a raincoat; the pill is on the front man's."})
