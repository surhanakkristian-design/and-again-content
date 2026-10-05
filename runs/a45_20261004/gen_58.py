import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def W(d): json.dump(d, open(f"content/{d['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# ---------- 58
t=T(17)
girl={0.0:(.05,0,.90,1),0.5:(.05,0,.90,1),1.0:(.05,0,.90,1),1.5:(0,0,1,1),2.0:(0,0,1,1),2.5:(0,0,1,1),
 3.0:(.08,.05,.92,.95),3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(.06,.13,.88,.87),5.5:(.10,.21,.90,.79),
 6.0:(.17,.02,.68,.96),6.5:(.15,.03,.63,.86),7.0:(.26,.20,.47,.67),7.5:(.21,.27,.59,.70),8.0:(.20,.27,.60,.68)}
k=K(t,girl)
W({"mediaId":58,"level":"A","keyWord":"backpack","defaultVoice":"female",
 "taps":[{"phrase":"to pack her clothes","target":"the girl","voice":"female","keys":k},
         {"phrase":"to put on a backpack","target":"the girl","voice":"female","keys":k},
         {"phrase":"to walk up the steps","target":"the girl","voice":"female","keys":k}],
 "stillS":0.0,
 "nouns":[{"word":"a girl","x":.50,"y":.20,"voice":"female"},{"word":"clothes","x":.52,"y":.47,"voice":"female"},
          {"word":"a bottle","x":.40,"y":.68,"voice":"female"},{"word":"a backpack","x":.50,"y":.88,"voice":"female"}],
 "question":"What is the girl doing?",
 "answer":["She","is","packing","clothes","into","her","backpack."],"answerVoice":"female",
 "notes":"Only one tap target (the girl, box includes the backpack she packs/wears): the backpack sits inside her outline in the rear views, so a separate backpack box could not be kept apart. Close-ups 3.5-4.5 show only her torso and hands (full frame). Still 0.0: the bottle is partly inside the backpack; pills bottle/backpack are 0.20 apart in y."})

# ---------- 61
t=T(19)
wom={0.0:(0,.22,.46,.73),0.5:(.04,.27,.42,.63),1.0:(.19,.31,.28,.53),1.5:(.19,.33,.29,.45),2.0:(.19,.35,.28,.39),
 2.5:(.22,.36,.27,.35),3.0:(.27,.37,.25,.31),3.5:(.21,.41,.22,.24),4.0:(.19,.41,.21,.26),4.5:(.21,.40,.23,.27),
 5.0:(.28,.39,.22,.27),5.5:(.30,.39,.20,.26),6.0:(.32,.40,.18,.25),6.5:(.32,.41,.18,.22),7.0:(.32,.41,.18,.19),
 7.5:(.32,.42,.18,.18),8.0:(.31,.42,.18,.18),8.5:(.32,.42,.18,.18),9.0:(.32,.39,.18,.20)}
man={0.0:(.46,.15,.54,.80),0.5:(.46,.21,.54,.69),1.0:(.47,.27,.53,.57),1.5:(.48,.29,.48,.49),2.0:(.47,.32,.39,.42),
 2.5:(.49,.33,.36,.38),3.0:(.52,.32,.35,.35),3.5:(.64,.42,.30,.24),4.0:(.62,.41,.31,.26),4.5:(.58,.39,.32,.28),
 5.0:(.50,.37,.27,.29),5.5:(.50,.37,.25,.28),6.0:(.50,.38,.22,.27),6.5:(.50,.39,.21,.24),7.0:(.50,.40,.18,.21),
 7.5:(.50,.41,.18,.19),8.0:(.49,.41,.18,.19),8.5:(.50,.41,.18,.19),9.0:(.50,.40,.18,.19)}
duck={1.0:(.01,.55,.18,.14),1.5:(.01,.55,.18,.14),2.0:(.01,.57,.18,.14),2.5:(.02,.56,.18,.14),3.0:(.03,.55,.18,.14),
 3.5:(.01,.55,.18,.14),4.0:(0,.55,.18,.14)}
W({"mediaId":61,"level":"A","keyWord":"backward","defaultVoice":"male",
 "taps":[{"phrase":"to wear a long scarf","target":"the woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to sit down on a bench","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to watch the people","target":"the duck","voice":"male","keys":K(t,duck)}],
 "stillS":2.0,
 "nouns":[{"word":"a lamp","x":.33,"y":.32,"voice":"male"},{"word":"a man","x":.62,"y":.46,"voice":"male"},
          {"word":"a bench","x":.84,"y":.57,"voice":"male"},{"word":"a duck","x":.14,"y":.64,"voice":"male"}],
 "question":"What are the two people doing?",
 "answer":["They","are","walking","backward."],"answerVoice":"male",
 "notes":"The camera cuts/zooms between frames, so the pair jumps in position. The man drops onto the right bench only at 3.5-4.0 s (short moment). Woman's phrase is a state (both walk backward, no action only she does). Duck is half hidden at 0.5 and nearly out at 4.5: off there. At 1.0-2.0 the woman's box starts at x .18-.19 so it does not touch the duck (her scarf tip is cut). Two benches in the still: the slot is on the right one. Answer kept to 4 chips to avoid a movable adverbial."})

# ---------- 65
t=T(21)
wom={0.0:(0,.31,.80,.69),0.5:(0,.30,.80,.70),1.0:(0,.04,.73,.96),1.5:(0,0,.76,1),2.0:(0,0,.75,1),2.5:(0,0,.93,1),
 3.0:(0,0,.78,.55),3.5:(0,0,.78,.55),4.0:(0,0,.50,.36),4.5:(0,0,.44,.32)}
man={0.0:(.80,.12,.20,.85),0.5:(.80,.12,.20,.88),1.0:(.73,0,.27,1),1.5:(.76,0,.24,1),2.0:(.75,0,.25,1),
 3.0:(.78,0,.22,.55),3.5:(.78,0,.22,.40),4.0:(.50,0,.50,.32),4.5:(.44,0,.56,.22),
 7.0:(.50,0,.50,.48),7.5:(.43,0,.57,.53),8.0:(.36,0,.64,.56),8.5:(.28,0,.72,.62),9.0:(.25,0,.75,.62),
 9.5:(.40,0,.60,.62),10.0:(.34,0,.66,.61)}
dog={7.0:(.12,.19,.37,.18),7.5:(.07,.25,.35,.16),8.0:(.07,.26,.28,.16),8.5:(.05,.29,.22,.16),9.0:(.05,.31,.19,.15),
 9.5:(.07,.32,.32,.15),10.0:(.07,.33,.26,.15)}
W({"mediaId":65,"level":"B","keyWord":"baking sheet","defaultVoice":"male",
 "taps":[{"phrase":"to arrange the vegetables","target":"the woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to taste a roasted potato","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to lie on the wooden floor","target":"the dog","voice":"male","keys":K(t,dog)}],
 "stillS":8.0,
 "nouns":[{"word":"a husky","x":.22,"y":.34,"voice":"male"},{"word":"an oven glove","x":.47,"y":.43,"voice":"male"},
          {"word":"a checked shirt","x":.82,"y":.30,"voice":"male"},{"word":"a baking sheet","x":.64,"y":.87,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","tasting","a","roasted","potato."],"answerVoice":"male",
 "notes":"Woman and man overlap behind the tray in 0-4.5 s: boxes split on a vertical line; the man is only a sliver at 2.5 (off). 5.0-6.5 show only the oven and gloved hands of an unidentifiable person: all off. In 7.5-10.0 the man's glove passes in front of the dog; boxes split so the glove tip may fall outside the man's box. defaultVoice male: two main people (woman first half, man second), evenId false. 'a checked shirt' (plaid flannel) and the pill of 'a baking sheet' on the lower rim/paper are the weakest nouns."})

# ---------- 66
wom={0.0:(.19,.17,.59,.56),0.5:(.21,.17,.59,.62),1.0:(.25,.20,.56,.67),1.5:(.32,.20,.57,.58),2.0:(.18,.02,.80,.72),
 4.0:(0,.26,.52,.33),4.5:(0,.24,.56,.33),5.0:(0,.25,.50,.36),5.5:(0,.24,.58,.34),
 6.0:(.69,.17,.31,.83),6.5:(.65,.18,.35,.82),7.0:(.66,.20,.34,.80),7.5:(.63,.19,.37,.81),8.0:(.57,.17,.43,.83),
 8.5:(.56,.19,.44,.81),9.0:(0,.17,.56,.58),9.5:(0,.25,.51,.42),10.0:(0,.25,.50,.45)}
man={4.0:(.52,.26,.48,.33),4.5:(.56,.24,.44,.34),5.0:(.50,.25,.50,.45),5.5:(.58,.24,.42,.46),
 6.0:(.42,.22,.27,.20),6.5:(.40,.23,.25,.29),7.0:(.38,.24,.28,.34),7.5:(.30,.24,.33,.25),8.0:(.22,.21,.34,.21),
 8.5:(.10,.17,.45,.33),9.0:(.57,.16,.43,.52),9.5:(.51,.24,.49,.45),10.0:(.50,.19,.50,.49)}
cat={0.0:(.01,.38,.18,.14),0.5:(.03,.38,.18,.14),1.0:(.06,.38,.18,.14),1.5:(.08,.38,.23,.14),2.0:(0,.27,.18,.14)}
W({"mediaId":66,"level":"A","keyWord":"baking","defaultVoice":"female",
 "taps":[{"phrase":"to take the bread out","target":"the woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to have a short beard","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to sit by the window","target":"the cat","voice":"female","keys":K(t,cat)}],
 "stillS":10.0,
 "nouns":[{"word":"a window","x":.25,"y":.19,"voice":"female"},{"word":"a man","x":.72,"y":.36,"voice":"male"},
          {"word":"a woman","x":.25,"y":.45,"voice":"female"},{"word":"bread","x":.50,"y":.76,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","baking","bread","in","the","kitchen."],"answerVoice":"female",
 "notes":"2.5-3.5 show only the oven and a hand: all off. The cat is clear only in 0-2.0 s (lying/sitting on the window sill; 'to sit' is loose, it may be lying). Man's phrase is a state: his only own actions (whisper, point) are short and the pointing hand at 5.5 cannot be assigned. In 6.0-8.5 the woman's gloved arm crosses the man: his box is head and shoulders only, her box is the right part; the glove itself may lie outside both. Key word 'baking' is used as a verb form in the answer."})
