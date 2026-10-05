import json
OFF='off'
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t,OFF)
        out.append({"t":t,"off":True} if v==OFF else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1,ensure_ascii=False)

# ---- 847
t=T(21)
bow1=(.15,.41,.72,.59); bow2=(.10,.41,.80,.59)
row={0.0:(0,.15,1,.55),0.5:(0,.20,1,.52),1.0:(0,.02,1,.98),1.5:(0,.02,1,.98),
     3.0:bow1,3.5:bow1,4.0:bow2,4.5:bow2,5.0:bow2,5.5:bow2,
     6.0:(.13,.50,.74,.50),6.5:(.18,.46,.66,.32),7.0:(.30,.47,.42,.27),7.5:(.32,.46,.42,.26),
     8.0:(.34,.48,.32,.20),8.5:(.34,.48,.32,.20),9.0:(.08,.12,.84,.83),9.5:(0,.02,1,.98),10.0:(0,.02,1,.98)}
crowd={2.0:(0,.20,1,.20),2.5:(0,.21,1,.25),3.0:(0,.10,1,.14),3.5:(0,.10,1,.14),4.0:(0,.11,1,.14),4.5:(0,.11,1,.14),
       5.0:(0,.13,1,.14),5.5:(0,.13,1,.14),6.0:(0,.33,1,.13),6.5:(0,.32,1,.14),7.0:(0,.34,1,.13),7.5:(0,.33,1,.13),
       8.0:(0,.34,1,.14),8.5:(0,.34,1,.14)}
rk=keys(t,row)
save({"mediaId":847,"level":"B","keyWord":"victory","defaultVoice":"female",
 "taps":[{"phrase":"to cross the finish line","target":"the rowers","voice":"female","keys":rk},
         {"phrase":"to lift a teammate up","target":"the rowers","voice":"female","keys":rk},
         {"phrase":"to cheer from the riverbank","target":"the crowd","voice":"female","keys":keys(t,crowd)}],
 "stillS":8.0,
 "nouns":[{"word":"lanterns","x":.50,"y":.13,"voice":"female"},{"word":"spectators","x":.22,"y":.42,"voice":"female"},
          {"word":"a rowing boat","x":.50,"y":.68,"voice":"female"},{"word":"a river","x":.50,"y":.88,"voice":"female"}],
 "question":"What are the rowers celebrating?",
 "answer":["They","are","celebrating","their","victory."],"answerVoice":"female",
 "notes":"Target 'the rowers' = the crew as a group (individuals cannot be followed across the cuts; a 4th crew member appears at 9.0). At 3.0-5.5 only the bow of their boat is in the picture: the box is on the bow, because that is where the learner taps for 'to cross the finish line'. Crowd and rowers overlap slightly at 6.5-7.5 (raised oars): split at the horizontal line, oar tips fall into the crowd box. Crowd is OFF at 9.0-10.0 (tiny blurred figures behind the crew on both sides, cannot be boxed without overlapping the rowers). Key word 'victory' is abstract, so it is in the answer, not in the nouns."})

# ---- 848
cat={7.0:(0,.02,.25,.14),7.5:(0,.02,.30,.14),8.0:(.06,.03,.38,.14),8.5:(.08,.03,.38,.14),9.0:(.12,.03,.38,.14),9.5:(.14,.03,.36,.13),10.0:(.14,.04,.36,.14)}
wom={2.0:(0,.03,.57,.97),2.5:(0,.03,.58,.97),3.0:(0,.05,.56,.95),3.5:(0,.08,.58,.92),4.0:(0,.10,.46,.90),4.5:(0,.10,.44,.90),5.0:(0,.12,.50,.88),
     5.5:(0,.14,.44,.60),6.0:(0,.14,.42,.56),6.5:(0,.14,.44,.56),7.0:(0,.17,.50,.63),7.5:(0,.17,.49,.60),8.0:(0,.18,.50,.50),8.5:(0,.17,.50,.52),
     9.0:(0,.18,.50,.52),9.5:(0,.18,.50,.52),10.0:(0,.18,.50,.52)}
man={2.0:(.58,.12,.42,.88),2.5:(.59,.12,.41,.88),3.0:(.57,.15,.43,.85),3.5:(.59,.20,.41,.80),4.0:(.47,.07,.53,.83),4.5:(.45,.05,.55,.90),5.0:(.51,.08,.49,.82),
     5.5:(.50,.10,.50,.64),6.0:(.52,.12,.48,.58),6.5:(.52,.12,.48,.58),7.0:(.51,.12,.49,.63),7.5:(.50,.12,.50,.62),8.0:(.51,.14,.49,.54),8.5:(.51,.14,.49,.55),
     9.0:(.51,.14,.49,.56),9.5:(.51,.15,.49,.55),10.0:(.51,.18,.49,.50)}
save({"mediaId":848,"level":"B","keyWord":"vinegar","defaultVoice":"female",
 "taps":[{"phrase":"to chew a spinach leaf","target":"the woman","voice":"female","keys":keys(t,wom)},
         {"phrase":"to pour vinegar over tomatoes","target":"the man","voice":"male","keys":keys(t,man)},
         {"phrase":"to stroll along the fence","target":"the cat","voice":"female","keys":keys(t,cat)}],
 "stillS":6.0,
 "nouns":[{"word":"vinegar","x":.70,"y":.29,"voice":"female"},{"word":"braids","x":.17,"y":.47,"voice":"female"},
          {"word":"cherry tomatoes","x":.50,"y":.73,"voice":"female"},{"word":"a fence","x":.25,"y":.17,"voice":"female"}],
 "question":"What is the man doing?",
 "answer":["He","is","pouring","vinegar","over","the","tomatoes."],"answerVoice":"male",
 "notes":"0.0-1.5: only a hand with the cruet / a finger, owner not identifiable -> both people OFF. Woman's outstretched hand crosses into the man's half at 2.0-5.0 and 10.0: split on a vertical line, her fingertips are cut. The man pours from above his own head (odd generation) but the stream into the bowl is clearly visible at 6.0. 'vinegar' pill sits on the cruet at 6.0. 'to chew a spinach leaf': she puts a green leaf in her mouth at 8.0 and chews at 8.5-9.5; the man never eats salad (he only licks a finger at 4.5)."})

# ---- 849
t=T(19)
man={0.0:(.22,.12,.66,.58),0.5:(.17,.07,.70,.62),1.0:(.17,.11,.70,.66),3.5:(0,0,1,1),4.0:(0,0,1,1),7.0:(.12,0,.88,.62),
     7.5:(.07,.02,.86,.80),8.0:(.05,.07,.84,.68),8.5:(.38,.17,.62,.60),9.0:(.22,.14,.56,.76)}
wom={0.0:(0,.74,.22,.26),0.5:(0,.76,.22,.24),1.0:(0,.86,.36,.14),1.5:(0,0,1,.82),2.0:(0,.02,1,.92),2.5:(0,.02,1,.92),3.0:(0,.02,1,.92),
     4.5:(0,.05,1,.55),5.0:(0,.15,1,.45),5.5:(0,.15,1,.62),6.0:(0,.15,1,.50),7.0:(0,.70,1,.30)}
mk=keys(t,man)
save({"mediaId":849,"level":"B","keyWord":"visa","defaultVoice":"male",
 "taps":[{"phrase":"to hand over his passport","target":"the man","voice":"male","keys":mk},
         {"phrase":"to pump his fist","target":"the man","voice":"male","keys":mk},
         {"phrase":"to issue a visa","target":"the woman","voice":"female","keys":keys(t,wom)}],
 "stillS":5.0,
 "nouns":[{"word":"a visa","x":.50,"y":.57,"voice":"male"},{"word":"a thumb","x":.80,"y":.44,"voice":"male"},
          {"word":"pens","x":.20,"y":.87,"voice":"male"},{"word":"a rubber stamp","x":.66,"y":.13,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","sticking","a","visa","into","the","passport."],"answerVoice":"female",
 "notes":"Only two targets (man, woman): two phrases share the man. Woman at 0.0-1.0 and 7.0 is only a blurred purple shoulder/arm in the foreground; at 4.5-6.0 only her hands are in the picture (box spans both hands, the visa lies between them). 6.5 shows the stamped page without anybody -> both OFF. Still 5.0: a second visa sticker lies behind (at .70/.25), the 'a visa' pill is on the one being stuck in; the rubber stamp at the top is slightly out of focus."})

# ---- 850
t=T(21)
W={0.5:(.16,.05,.32,.52),1.0:(.19,.27,.29,.56),1.5:(.21,.38,.29,.55),2.0:(.22,.44,.28,.50),2.5:(.23,.47,.28,.50),3.0:(.22,.49,.29,.49),3.5:(.22,.49,.29,.49),
   4.0:(.22,.50,.29,.48),4.5:(.22,.50,.29,.48),5.0:(.22,.50,.29,.48),5.5:(.22,.50,.29,.45),6.0:(.22,.50,.28,.38),6.5:(.23,.55,.27,.33),7.0:(.23,.60,.27,.32)}
M={0.5:(.49,0,.34,.57),1.0:(.49,.23,.32,.60),1.5:(.51,.33,.31,.60),2.0:(.51,.39,.32,.55),2.5:(.52,.42,.31,.55),3.0:(.52,.44,.31,.54),3.5:(.52,.44,.31,.54),
   4.0:(.52,.45,.31,.53),4.5:(.52,.45,.31,.53),5.0:(.52,.45,.31,.53),5.5:(.52,.48,.31,.47),6.0:(.51,.52,.31,.36),6.5:(.51,.56,.31,.32),7.0:(.51,.59,.32,.33)}
S={1.0:(.33,0,.34,.22),1.5:(.32,0,.38,.33),2.0:(.32,0,.38,.36),2.5:(.31,0,.40,.39),3.0:(.31,.02,.40,.39),3.5:(.31,.02,.40,.39),4.0:(.31,.03,.40,.39),4.5:(.31,.03,.40,.39),
   5.0:(.31,.05,.40,.37),5.5:(.31,.05,.40,.37),6.0:(.30,.03,.40,.38),6.5:(.30,.03,.40,.38),7.0:(.30,.02,.40,.38)}
for x in [7.5,8.0,8.5,9.0,9.5,10.0]:
    W[x]=(.23,.63,.27,.30); M[x]=(.51,.59,.32,.34); S[x]=(.30,0,.40,.38)
save({"mediaId":850,"level":"A","keyWord":"volcano","defaultVoice":"female",
 "taps":[{"phrase":"to rise into the sky","target":"the smoke","voice":"female","keys":keys(t,S)},
         {"phrase":"to have long hair","target":"the woman","voice":"female","keys":keys(t,W)},
         {"phrase":"to have short hair","target":"the man","voice":"male","keys":keys(t,M)}],
 "stillS":4.0,
 "nouns":[{"word":"a volcano","x":.50,"y":.45,"voice":"female"},{"word":"smoke","x":.50,"y":.15,"voice":"female"},
          {"word":"the sky","x":.80,"y":.28,"voice":"female"},{"word":"grass","x":.15,"y":.78,"voice":"female"}],
 "question":"What are they looking at?",
 "answer":["They","are","looking","at","a","volcano."],"answerVoice":"female",
 "notes":"The man and the woman do exactly the same (stand, watch), so their phrases are states (hair) that fit only one of them; both are dark silhouettes from 5.5 on, the hair outline stays readable. 0.0 is almost black (only legs at the top edge) -> all OFF. The camera pulls back: the people shrink and sink to the lower third. Smoke box ends at the crater; the volcano itself is not a tap target."})
