import json
def keys(rows, n, step=0.5):
    out=[]
    for i in range(n):
        t=round(i*step,1); r=rows.get(t)
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),ensure_ascii=False,indent=1)

# ---------- 4503
W={0.0:(.10,.22,.50,.40),0.5:(.15,.15,.55,.44),1.0:(.13,.20,.68,.51),1.5:(.17,.17,.68,.50),2.0:(.17,.15,.63,.45),
   2.5:(.18,.10,.67,.52),3.0:(.10,.03,.80,.61),3.5:(.05,0,.90,.66),4.0:(.05,0,.93,.66),4.5:(.08,0,.90,.72),
   5.0:(.02,.10,.96,.67),5.5:(.05,0,.93,.85),6.0:(.12,.05,.86,.77),6.5:(.30,.15,.50,.61),7.0:(.45,.28,.32,.40),
   7.5:(.35,.30,.30,.36),8.0:(.28,.25,.34,.37),8.5:(.33,.25,.34,.36),9.0:(.27,.25,.35,.36),9.5:(.27,.25,.36,.34),10.0:(.20,.23,.38,.36)}
C={0.0:(.42,.63,.38,.21),0.5:(.43,.60,.37,.19),1.0:(.30,.72,.50,.26),1.5:(.32,.68,.50,.22),2.0:(.34,.61,.46,.24),
   2.5:(.30,.63,.56,.27),3.0:(.25,.65,.65,.35),3.5:(.10,.67,.85,.33),4.0:(.05,.67,.80,.33),4.5:(.15,.73,.83,.27),
   5.0:(.25,.78,.60,.22),5.5:(.28,.86,.52,.14),6.0:(.32,.83,.46,.17),6.5:(.42,.77,.36,.19),7.0:(.49,.69,.30,.14),
   7.5:(.41,.67,.28,.14),8.0:(.38,.63,.28,.15),8.5:(.42,.62,.28,.15),9.0:(.44,.62,.28,.14),9.5:(.44,.60,.30,.15),10.0:(.37,.60,.30,.16)}
kw=keys(W,21); kc=keys(C,21)
save({"mediaId":4503,"level":"A","keyWord":"wish","defaultVoice":"female",
 "taps":[{"phrase":"to blow out the candles","target":"the woman in the hat","voice":"female","keys":kw},
         {"phrase":"to cover her mouth","target":"the woman in the hat","voice":"female","keys":kw},
         {"phrase":"to have many candles","target":"the cake","voice":"female","keys":kc}],
 "stillS":8.0,
 "nouns":[{"word":"a hat","x":.47,"y":.28,"voice":"female"},{"word":"a cake","x":.52,"y":.66,"voice":"female"},{"word":"a table","x":.62,"y":.77,"voice":"female"}],
 "question":"What is the woman in pink doing?",
 "answer":["She","is","blowing","out","the","candles."],"answerVoice":"female",
 "notes":"Two targets (woman in the party hat, cake); the cake is held in front of her the whole clip, so the boxes are split by a horizontal line at the top of the candles: her box is her head, arms and upper body, the cake's box the candles and the cake. She covers her mouth with both hands at 1.5-2.0 s and blows at 4.0 s. 'to have many candles' is a state: the cake does nothing. Key word 'wish' (verb) is not used: making a wish cannot be seen. At 9.5-10.0 s the candles burn again (generation glitch). Only 3 nouns: the balloons hang far apart, the dresses sit on the people."})

# ---------- 4504
Wm={0.0:(.62,.44,.38,.38),0.5:(.52,.26,.48,.58),1.0:(.50,.17,.47,.80),1.5:(.65,.36,.35,.62),2.0:(.49,.38,.22,.30),2.5:(.27,.35,.27,.47),
    7.0:(.60,.33,.18,.30),7.5:(.58,.33,.20,.40),8.0:(.63,.32,.25,.32),8.5:(.60,.32,.34,.32),9.0:(.66,.28,.28,.42),9.5:(.52,.19,.42,.56),
    10.0:(.45,.15,.47,.54),10.5:(.42,.15,.52,.56),11.0:(.40,.15,.52,.69),11.5:(.40,.15,.48,.69),12.0:(.30,.16,.54,.58)}
S={0.0:(0,.22,.60,.38),0.5:(0,.24,.50,.36),1.0:(0,.26,.48,.47),1.5:(0,.25,.63,.48),2.0:(0,.24,.47,.30),2.5:(0,.25,.26,.22),3.0:(0,.28,.18,.17)}
km=keys(Wm,25)
save({"mediaId":4504,"level":"A","keyWord":"success","defaultVoice":"female",
 "taps":[{"phrase":"to have long purple hair","target":"the woman with purple hair","voice":"female","keys":km},
         {"phrase":"to sit on their arms","target":"the woman with purple hair","voice":"female","keys":km},
         {"phrase":"to show a big number","target":"the screen","voice":"female","keys":keys(S,25)}],
 "stillS":0.0,
 "nouns":[{"word":"a screen","x":.40,"y":.33,"voice":"female"},{"word":"a woman","x":.84,"y":.68,"voice":"female"},
          {"word":"a laptop","x":.55,"y":.83,"voice":"female"},{"word":"a plant","x":.74,"y":.92,"voice":"female"}],
 "question":"What is the screen showing?",
 "answer":["The","screen","is","showing","a","big","number."],"answerVoice":"female",
 "notes":"Crowd clip: only the woman with purple hair and the wall screen can be followed safely. She is off at 3.0-6.5 s: in the wide shots she is hidden in the group (at 3.0 and 5.5 s only the back of her purple hair shows). 'to sit on their arms': two men lift her from 9.0 s. 'to have long purple hair' is a state. The screen's box is cut where the woman stands in front of it (0-2.5 s); the bald man covers part of it. Screen off from 3.5 s. Key word 'success' is abstract and not used. Noun 'a woman' at 0.0 s sits on the woman, the man on the left gets no pill."})

# ---------- 4506
Y={0.0:(.13,0,.87,1.0),0.5:(.05,.13,.93,.87),1.0:(.03,.15,.95,.85),1.5:(.05,.15,.95,.85),2.0:(.03,.08,.97,.92),2.5:(.03,.08,.97,.92),3.0:(.03,.15,.95,.85)}
Wo={3.5:(.05,0,.75,1.0),4.0:(.05,.07,.80,.93),4.5:(.05,.07,.83,.93),5.0:(.05,.08,.85,.92),5.5:(.05,.08,.85,.92),6.0:(.05,.09,.85,.91)}
B={6.5:(0,.10,1.0,.90),7.0:(0,.17,1.0,.83),7.5:(0,.17,1.0,.83)}
for i in range(16,25): B[i*0.5]=(0,.13,1.0,.87)
save({"mediaId":4506,"level":"B","keyWord":"comfort","defaultVoice":"male",
 "taps":[{"phrase":"to frown in discomfort","target":"the man in the white T-shirt","voice":"male","keys":keys(Y,25)},
         {"phrase":"to sit beside a table","target":"the woman","voice":"female","keys":keys(Wo,25)},
         {"phrase":"to sink into an armchair","target":"the bearded man","voice":"male","keys":keys(B,25)}],
 "stillS":8.0,
 "nouns":[{"word":"an armchair","x":.50,"y":.14,"voice":"male"},{"word":"a beard","x":.50,"y":.32,"voice":"male"},
          {"word":"a striped sweater","x":.50,"y":.46,"voice":"male"},{"word":"jeans","x":.50,"y":.68,"voice":"male"}],
 "question":"What is the bearded man doing?",
 "answer":["He","is","sinking","into","a","comfortable","armchair."],"answerVoice":"male",
 "notes":"Three shots, one person each (0-3.0 young man on a hard chair, 3.5-6.0 woman on a wooden chair, 6.5-12.0 bearded man in the armchair), so the boxes never meet. defaultVoice male: two of the three people are men and the bearded man is the main one. 'to sit beside a table' is the weakest phrase for level B (only she has a table; 'to sit upright' would also fit the young man). Key word 'comfort' appears as 'comfortable' in the answer and as 'discomfort' in a phrase. The four pills stand in one column on the bearded man's shot, 0.14-0.22 apart in y; 'an armchair' sits on the back of the chair above his head."})

# ---------- 4508
M={0.0:(.22,.25,.35,.45),0.5:(.26,.30,.40,.43),1.0:(.25,.29,.32,.44),1.5:(.25,.29,.26,.37),2.0:(.20,.28,.44,.36),2.5:(.28,.37,.46,.28),
   3.0:(.20,.33,.34,.33),3.5:(.23,.27,.44,.40),4.0:(.27,.27,.36,.37),4.5:(.16,.32,.34,.31),5.0:(.18,.33,.39,.31),5.5:(.30,.33,.38,.31),
   6.0:(.26,.27,.40,.36),6.5:(.18,.26,.38,.33),7.0:(.20,.37,.36,.24),7.5:(.20,.33,.36,.30),8.0:(.22,.29,.40,.38),8.5:(.22,.27,.52,.43),
   9.0:(.28,.28,.46,.38),9.5:(.23,.29,.50,.40),10.0:(.23,.26,.50,.44),10.5:(.20,.26,.66,.44),11.0:(.10,.44,.90,.52),11.5:(.06,.44,.94,.52),12.0:(.02,.43,.98,.44)}
A={0.0:(.66,.33,.26,.31),0.5:(.68,.34,.24,.31),1.0:(.70,.35,.24,.29),1.5:(.70,.34,.27,.30),2.0:(.73,.33,.27,.29),2.5:(.77,.33,.23,.31),
   3.0:(.70,.35,.27,.30),3.5:(.73,.35,.27,.30),4.0:(.70,.33,.24,.30),4.5:(.68,.31,.25,.32),5.0:(.70,.32,.26,.30),5.5:(.76,.34,.24,.29),
   6.0:(.76,.32,.24,.32),6.5:(.78,.32,.22,.32),7.0:(.78,.33,.22,.30),7.5:(.82,.33,.18,.30),8.0:(.76,.33,.24,.31),8.5:(.77,.33,.23,.30),
   9.0:(.76,.34,.22,.30),9.5:(.76,.35,.22,.27),10.0:(.75,.35,.22,.27),11.0:(.62,.29,.24,.14),11.5:(.60,.28,.24,.15),12.0:(.58,.23,.25,.19)}
km=keys(M,25)
save({"mediaId":4508,"level":"B","keyWord":"load","defaultVoice":"male",
 "taps":[{"phrase":"to load the heavy luggage","target":"the man","voice":"male","keys":km},
         {"phrase":"to lean on the counter","target":"the man","voice":"male","keys":km},
         {"phrase":"to stand behind the counter","target":"the woman in uniform","voice":"female","keys":keys(A,25)}],
 "stillS":4.0,
 "nouns":[{"word":"the ceiling","x":.50,"y":.10,"voice":"male"},{"word":"luggage","x":.17,"y":.62,"voice":"male"},
          {"word":"a passport","x":.82,"y":.76,"voice":"male"},{"word":"a counter","x":.62,"y":.88,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","loading","his","luggage","onto","the","belt."],"answerVoice":"male",
 "notes":"Two targets: the man (passenger) and the airline agent ('the woman in uniform'). At 10.5 s the agent is hidden behind the holdall and the man's arm: off. At 11.5-12.0 s the man leans on the counter in front of her: boxes split by a horizontal line at the top of his head (11.0-12.0 s), so only her head and shoulders are in her box. 'to lean on the counter' happens only at 11.0-12.0 s. The man's box holds the suitcase only where he carries it. Nouns at 4.0 s: 'luggage' sits on the pile on the trolley (left); the suitcase on the belt gets no pill. 'a counter' is on the steel top in the foreground, 'a passport' on the passport lying there (y 0.13 apart)."})
