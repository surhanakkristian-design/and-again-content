import json
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def write(o):
    json.dump(o, open(f"content/{o['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# 4488
t=T(25)
man={0.0:(0,0.08,1,0.60),0.5:(0,0.10,1,0.60),1.0:(0,0.14,1,0.56),1.5:(0,0.14,1,0.56),2.0:(0,0.14,1,0.54),
2.5:(0,0.13,1,0.57),3.0:(0,0.13,1,0.57),3.5:(0,0.13,1,0.57),4.0:(0,0.12,1,0.56),4.5:(0,0.12,1,0.58),
5.0:(0,0.15,1,0.55),5.5:(0,0.15,1,0.55),6.0:(0,0.13,1,0.56),6.5:(0,0.15,1,0.53),7.0:(0,0.17,0.92,0.50),
7.5:(0,0.18,0.95,0.45),8.0:(0.08,0.0,0.87,0.62),8.5:(0.05,0.14,0.95,0.52),9.0:(0.05,0.17,0.90,0.50),
9.5:(0.05,0.15,0.95,0.52),10.0:(0.05,0.18,0.90,0.50),10.5:(0.05,0.18,0.95,0.50),11.0:(0.05,0.20,0.85,0.48),
11.5:(0.03,0.22,0.90,0.46),12.0:(0.03,0.22,0.85,0.45)}
pile={x:(0.08,0.76,0.72,0.24) for x in t}
mk=keys(t,man); pk=keys(t,pile)
write({"mediaId":4488,"level":"B","keyWord":"document","defaultVoice":"male","taps":[
 {"phrase":"to slam down a stamp","target":"the man in the white shirt","voice":"male","keys":mk},
 {"phrase":"to lose his temper","target":"the man in the white shirt","voice":"male","keys":mk},
 {"phrase":"to lie in a messy pile","target":"the pile of documents","voice":"male","keys":pk}],
 "stillS":12.0,
 "nouns":[{"word":"documents","x":0.42,"y":0.88,"voice":"male"},{"word":"a stamp","x":0.60,"y":0.58,"voice":"male"},
  {"word":"a keyboard","x":0.76,"y":0.76,"voice":"male"},{"word":"a fan","x":0.68,"y":0.10,"voice":"male"}],
 "question":"What is the angry man doing?",
 "answer":["He","is","slamming","a","stamp","onto","a","document."],
 "answerVoice":"male",
 "notes":"Only one clear actor; the stamp sits inside the man's box, so the third target is the static pile of documents at the bottom (a state). Colleagues in the background are small and both on headsets, not used. Papers fly in front of the man 8.5-10.0 s."})

# 4490
w={0.0:(0,0,0.65,0.70),0.5:(0,0,0.65,0.70),1.0:(0,0,0.70,0.80),1.5:(0,0,0.80,0.75),2.0:(0,0,0.75,0.72),
2.5:(0,0,0.75,0.72),3.0:(0,0,0.75,0.72),3.5:(0,0,0.75,0.72),4.0:(0,0,0.75,0.72),4.5:(0,0,0.75,0.72),
5.0:(0,0.25,0.60,0.58),5.5:(0,0.25,0.60,0.55),6.0:(0,0.25,0.60,0.47),6.5:(0,0.22,0.48,0.42),7.0:(0,0.28,0.70,0.54),
7.5:(0,0.24,0.66,0.48),8.0:(0,0.25,0.60,0.38),8.5:(0.05,0.20,0.37,0.38),9.0:(0.07,0.22,0.40,0.46),
9.5:(0.08,0.22,0.40,0.46),10.0:(0,0.21,0.42,0.38),10.5:(0,0.22,0.40,0.40),11.0:(0,0.22,0.38,0.50),
11.5:(0,0.22,0.40,0.50),12.0:(0,0.20,0.40,0.40)}
wk=keys(t,w)
write({"mediaId":4490,"level":"A","keyWord":"prepare","defaultVoice":"female","taps":[
 {"phrase":"to light the candles","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to hold a match","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to sit at the table","target":"the woman","voice":"female","keys":wk}],
 "stillS":12.0,
 "nouns":[{"word":"a woman","x":0.22,"y":0.32,"voice":"female"},{"word":"candles","x":0.65,"y":0.42,"voice":"female"},
  {"word":"a plate","x":0.75,"y":0.68,"voice":"female"},{"word":"a table","x":0.30,"y":0.86,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","lighting","the","candles","on","the","table."],
 "answerVoice":"female",
 "notes":"Only one actor, so all three phrases are on the woman. 5.0-8.0 s show only her hand and arm with the match (box = hand/arm). Several plates on the table at 12.0 s; the pill is on the nearest one. Key word 'prepare' not used in the answer (would need an invented purpose)."})

# 4495
t2=T(19)
ym={0.0:(0.13,0.20,0.87,0.80),0.5:(0.10,0.22,0.90,0.78),1.0:(0.08,0.22,0.92,0.78)}
wo={1.5:(0.46,0.10,0.54,0.90),2.0:(0.46,0.10,0.54,0.90),2.5:(0.45,0.12,0.55,0.88),3.0:(0.46,0.14,0.54,0.86),3.5:(0.62,0.15,0.38,0.85)}
sm={5.0:(0.82,0.07,0.18,0.48),5.5:(0.82,0.05,0.18,0.60),6.0:(0.82,0.05,0.18,0.65),6.5:(0.82,0.08,0.18,0.58),
7.0:(0.75,0.03,0.25,0.84),7.5:(0.62,0.06,0.38,0.84),8.0:(0.55,0.08,0.45,0.82),8.5:(0.48,0.12,0.52,0.88),9.0:(0.44,0.15,0.50,0.85)}
write({"mediaId":4495,"level":"A","keyWord":"cost","defaultVoice":"male","taps":[
 {"phrase":"to touch an old car","target":"the young man","voice":"male","keys":keys(t2,ym)},
 {"phrase":"to open a car door","target":"the woman","voice":"female","keys":keys(t2,wo)},
 {"phrase":"to wear a tie","target":"the man in the suit","voice":"male","keys":keys(t2,sm)}],
 "stillS":0.0,
 "nouns":[{"word":"a car","x":0.25,"y":0.75,"voice":"male"},{"word":"a man","x":0.72,"y":0.50,"voice":"male"},
  {"word":"trees","x":0.24,"y":0.25,"voice":"male"},{"word":"the sky","x":0.28,"y":0.06,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","opening","a","car","door."],
 "answerVoice":"female",
 "notes":"Three shots, one person each. The man in the suit is only partly visible at the right edge 5.0-6.5 s (behind the open Ferrari door); 4.0-4.5 s off. 'to wear a tie' is a state: his only action (walking up to the car) is hard to phrase uniquely in 5 words. Key word 'cost' is only in the captions (500 EUR etc.), not used as a noun. defaultVoice male: mixed group, odd id."})

# 4496
m={0.0:(0.18,0,0.66,0.65),0.5:(0.05,0,0.84,0.65),1.0:(0.20,0,0.64,0.61),1.5:(0.14,0,0.72,0.78),2.0:(0.18,0.04,0.61,0.94),
2.5:(0.13,0.10,0.66,0.90),3.0:(0.23,0.11,0.49,0.37),3.5:(0.17,0.10,0.62,0.42),4.0:(0.13,0.13,0.66,0.43),4.5:(0.11,0.13,0.71,0.47),
5.0:(0.14,0.15,0.66,0.45),5.5:(0.14,0.13,0.68,0.44),6.0:(0.37,0.22,0.28,0.22),6.5:(0.36,0.14,0.28,0.31),7.0:(0.34,0.12,0.30,0.35),
7.5:(0.36,0.11,0.28,0.36),8.0:(0.36,0.10,0.28,0.37),8.5:(0.36,0.08,0.30,0.42),9.0:(0.34,0.07,0.34,0.46),9.5:(0.33,0.05,0.38,0.55),
10.0:(0.32,0.17,0.42,0.48),10.5:(0.31,0.25,0.45,0.42),11.0:(0.21,0.33,0.61,0.30),11.5:(0.14,0.35,0.72,0.30),12.0:(0.16,0.33,0.75,0.35)}
k=keys(t,m)
write({"mediaId":4496,"level":"B","keyWord":"lay","defaultVoice":"male","taps":[
 {"phrase":"to unroll a patterned rug","target":"the man","voice":"male","keys":k},
 {"phrase":"to kneel on the floor","target":"the man","voice":"male","keys":k},
 {"phrase":"to stretch out his arms","target":"the man","voice":"male","keys":k}],
 "stillS":12.0,
 "nouns":[{"word":"a rug","x":0.50,"y":0.80,"voice":"male"},{"word":"a sofa","x":0.74,"y":0.17,"voice":"male"},
  {"word":"an armchair","x":0.26,"y":0.26,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","laying","a","rug","on","the","floor."],
 "answerVoice":"male",
 "notes":"Only one actor; the rug lies under him at the end, so it is not a separate tap target. The rug changes between shots (small runner 4.5-7.0 s, large red rug from 7.5 s). He kneels 3.5-5.5 s, arms stretched out 11.0-12.0 s."})
