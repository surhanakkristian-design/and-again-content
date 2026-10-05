import json
def K(times, spec):
    out=[]
    for t in times:
        v=spec.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def dump(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), indent=1, ensure_ascii=False)

# ---------- 272
t=T(11)
woman={0.0:(.42,.06,.58,.49),0.5:(.40,.07,.60,.48),1.0:(.42,0,.58,.57),1.5:(.40,0,.60,.46),2.0:(.38,0,.62,.55),2.5:(.48,0,.52,.46),
       3.0:(.10,0,.90,.62),3.5:(.05,.08,.95,.62),4.0:(.06,.02,.94,.66),4.5:(.04,.01,.96,.72),5.0:(.04,.02,.96,.72)}
water={0.0:(.15,.56,.65,.11),0.5:(.15,.56,.68,.13),1.0:(.10,.58,.80,.16),1.5:(.14,.52,.72,.21),2.0:(.27,.56,.46,.14)}
stove={0.0:(.03,.68,.90,.24),0.5:(.02,.70,.90,.24),1.0:(0,.76,1,.24),1.5:(0,.80,1,.20),2.0:(0,.80,1,.20),2.5:(0,.80,1,.20),
       3.0:(0,.86,1,.14),3.5:(.02,.71,.96,.27),4.0:(.02,.70,.92,.24),4.5:(.02,.74,.92,.20),5.0:(.02,.75,.92,.23)}
dump({"mediaId":272,"level":"B","keyWord":"evaporate","defaultVoice":"female",
 "taps":[{"phrase":"to tilt the empty pan","target":"the woman","voice":"female","keys":K(t,woman)},
         {"phrase":"to evaporate from the pan","target":"the water","voice":"female","keys":K(t,water)},
         {"phrase":"to burn with a blue flame","target":"the camping stove","voice":"female","keys":K(t,stove)}],
 "stillS":0.0,
 "nouns":[{"word":"goggles","x":.62,"y":.23,"voice":"female"},{"word":"steam","x":.22,"y":.43,"voice":"female"},
          {"word":"a frying pan","x":.45,"y":.62,"voice":"female"},{"word":"a camping stove","x":.42,"y":.80,"voice":"female"}],
 "question":"What is happening to the water?",
 "answer":["It","is","evaporating","from","the","hot","pan."],"answerVoice":"female",
 "notes":"Water lies inside the pan, so the pan itself is not a tap target; water is off from 2.5 s (gone). Stove is only partly visible (dark burner at the bottom edge) from 1.5 to 3.0 s; the flame is hidden there. Woman's box ends above the pan in the early frames (her lower body is behind it)."})

# ---------- 273
t=T(21)
ww={0.0:.39,0.5:.39,1.0:.39,1.5:.39,2.0:.39,2.5:.39,7.0:.52,7.5:.56,8.0:.57,8.5:.57,9.0:.52,9.5:.52}
mx={0.0:.64,0.5:.64,1.0:.63,1.5:.61,2.0:.60,2.5:.60,7.5:.58,8.0:.58,8.5:.58,9.0:.58,9.5:.58}
woman={x:(0,.34,ww.get(x,.51),.66) for x in t}
man={x:(mx.get(x,.59),.29,round(1-mx.get(x,.59),2),.71) for x in t}
sun={x:(.40,.40,.18,.14) for x in (0.0,0.5,1.0,1.5,2.0,2.5)}
dump({"mediaId":273,"level":"A","keyWord":"evening","defaultVoice":"male",
 "taps":[{"phrase":"to go down behind the hills","target":"the sun","voice":"male","keys":K(t,sun)},
         {"phrase":"to have long hair","target":"the woman","voice":"female","keys":K(t,woman)},
         {"phrase":"to wear a green sweater","target":"the man","voice":"male","keys":K(t,man)}],
 "stillS":1.5,
 "nouns":[{"word":"the sky","x":.35,"y":.15,"voice":"male"},{"word":"the sun","x":.52,"y":.46,"voice":"male"},
          {"word":"houses","x":.55,"y":.56,"voice":"male"},{"word":"a woman","x":.20,"y":.72,"voice":"female"}],
 "question":"What is the sun doing?",
 "answer":["It","is","going","down","behind","the","hills."],"answerVoice":"male",
 "notes":"Both people do the same things (hold a cup, clink, watch), so woman and man get state phrases; the man's sweater is dark green and hard to see after about 4 s. While the sun is visible (0-2.5 s) the woman's box is cut at x 0.39 so it does not overlap the sun's box: her outstretched arm and cup are outside it. Sun off from 3.0 s (only a glow). Key word 'evening' is not a placeable thing and is not in the texts."})

# ---------- 274
t=T(21)
man={0.0:(0,.42,.68,.58),0.5:(0,.13,.73,.87),1.0:(0,.25,.71,.75),1.5:(.02,.41,.96,.59),2.0:(.04,.56,.60,.44),2.5:(.04,.73,.76,.27)}
boy={0.0:(.69,.33,.25,.36),0.5:(.74,.31,.20,.17),1.0:(.72,.36,.20,.20),2.0:(.65,.49,.20,.30),2.5:(.58,.58,.20,.14),3.0:(.58,.75,.20,.20)}
lh={0.0:.15,0.5:.12,1.0:.14,1.5:.15,2.0:.15,2.5:.15,8.0:.17,8.5:.17,9.0:.17,9.5:.17,10.0:.17}
lights={x:(0,0,1,lh.get(x,.14)) for x in t}
dump({"mediaId":274,"level":"A","keyWord":"everyone","defaultVoice":"male",
 "taps":[{"phrase":"to hold up a scarf","target":"the man with the scarf","voice":"male","keys":K(t,man)},
         {"phrase":"to sit on someone's shoulders","target":"the boy","voice":"male","keys":K(t,boy)},
         {"phrase":"to shine from the roof","target":"the lights","voice":"male","keys":K(t,lights)}],
 "stillS":0.0,
 "nouns":[{"word":"lights","x":.55,"y":.07,"voice":"male"},{"word":"a boy","x":.80,"y":.46,"voice":"male"},
          {"word":"a scarf","x":.50,"y":.76,"voice":"male"}],
 "question":"What is everyone doing?",
 "answer":["Everyone","is","shouting","in","the","stadium."],"answerVoice":"male",
 "notes":"The camera pulls back: the man with the scarf leaves the picture after 2.5 s, the boy after 3.0 s (boy hidden behind the man's arm at 1.5 s -> off). The man's box is cut on the right where the boy sits, so his right hand is outside it. From 2.0 s tiny fans far behind also wave rainbow flags/scarves. Only 3 nouns: everything else is the crowd."})

# ---------- 275
t=T(27)
ww={0.0:.55,0.5:.59,1.0:.57,1.5:.58,2.0:.57,2.5:.56,3.0:.56,3.5:.55,4.0:.55,4.5:.55,5.0:.55,5.5:.55}
mx={0.0:.58,0.5:.61,1.0:.59,1.5:.60,2.0:.59,2.5:.58,3.0:.57,3.5:.57,4.0:.57,4.5:.57,5.0:.57,5.5:.57}
woman={x:(0,.18,ww.get(x,.53),.82) for x in t}
man={x:(mx.get(x,.54),.07,round(1-mx.get(x,.54),2),.93) for x in t}
dump({"mediaId":275,"level":"A","keyWord":"argue","defaultVoice":"male",
 "taps":[{"phrase":"to point a finger","target":"the woman","voice":"female","keys":K(t,woman)},
         {"phrase":"to look up and think","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to smile at the man","target":"the woman","voice":"female","keys":K(t,woman)}],
 "stillS":4.0,
 "nouns":[{"word":"curtains","x":.33,"y":.20,"voice":"male"},{"word":"a sofa","x":.46,"y":.42,"voice":"male"},
          {"word":"a table","x":.44,"y":.57,"voice":"male"},{"word":"a man","x":.80,"y":.75,"voice":"male"}],
 "question":"What are the man and woman doing?",
 "answer":["They","are","arguing","in","the","living","room."],"answerVoice":"male",
 "notes":"defaultVoice male: a mixed couple, evenId false. 'to look up and think': the thinking is read from his face (eyes up, mouth open, 5.5-11.5 s). The two stand very close; boxes are split at about x 0.55."})
