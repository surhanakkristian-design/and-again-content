import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T21=[i*0.5 for i in range(21)]; T19=[i*0.5 for i in range(19)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 764
man={0.0:(.03,.05,.94,.83),0.5:(.03,.05,.94,.83),1.0:(.18,.30,.82,.70),1.5:(.33,.78,.67,.22)}
for t in (2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5): man[t]=(0,.13,1,.87)
man.update({7.0:(0,.23,.40,.77),7.5:(0,.23,.40,.77),8.0:(0,.23,.40,.77),8.5:(0,.23,.42,.77),9.0:(0,.27,.40,.73)})
cac={7.0:(.41,.07,.36,.44),7.5:(.41,.07,.36,.44),8.0:(.41,.07,.36,.43),8.5:(.43,.07,.33,.40),9.0:(.41,.08,.36,.44)}
m=K(T19,man)
save({"mediaId":764,"level":"A","keyWord":"tablet","defaultVoice":"male","taps":[
{"phrase":"to hold a tablet","target":"the man","voice":"male","keys":m},
{"phrase":"to draw with his finger","target":"the man","voice":"male","keys":m},
{"phrase":"to grow outside the window","target":"the big cactus","voice":"male","keys":K(T19,cac)}],
"stillS":8.0,"nouns":[{"word":"a tablet","x":.74,"y":.50,"voice":"male"},{"word":"a cactus","x":.50,"y":.20,"voice":"male"},
{"word":"a cup","x":.88,"y":.71,"voice":"male"},{"word":"glasses","x":.24,"y":.44,"voice":"male"}],
"question":"What is the man drawing?","answer":["He","is","drawing","a","cactus","on","his","tablet."],"answerVoice":"male",
"notes":"Only two targets (man, big cactus outside); the tablet is not a tap target because the man holds it the whole time, it lies inside his box. At 1.0-6.5 the man is only his hands (1.0-1.5 one finger on the white screen), box = hands + tablet. At 7.0-9.0 the big cactus stands right behind the man's head: split at x=.40/.41, so the man's box holds head and body but not his outstretched arms and the tablet, and the cactus box loses its left arm. Small blurred cacti in the window at 0-0.5 and 5.5-6.5 and a small one at the right at 7-9 are not boxed (the target is 'the big cactus'). The tablet at 8.0 also shows a drawn cactus: the 'a cactus' pill sits on the real one at the top."})

# 766
wo={0.0:(.12,0,.47,1),0.5:(.17,0,.50,1),1.0:(.15,0,.50,1),1.5:(.17,0,.63,1),2.0:(.17,0,.65,1),2.5:(.20,0,.70,1),3.0:(.15,0,.72,1),
3.5:(.15,0,.57,1),4.0:(.07,0,.50,1),4.5:(.02,.05,.47,.95),5.0:(0,.10,.47,.90),5.5:(.05,.13,.47,.87),6.0:(.05,.10,.46,.90),
6.5:(.06,.08,.46,.92),7.0:(.07,.08,.45,.92),7.5:(.08,.08,.46,.92),8.0:(.08,.07,.44,.93),8.5:(0,.07,.51,.93),9.0:(0,.12,.47,.88),
9.5:(0,.18,.46,.82),10.0:(.02,.17,.45,.83)}
ma={0.0:(.60,.42,.40,.58),0.5:(.68,.50,.32,.50),1.0:(.66,.72,.34,.28),1.5:(.82,.84,.18,.16),3.5:(.73,.28,.27,.50),4.0:(.58,0,.42,1),
4.5:(.50,0,.50,1),5.0:(.48,0,.52,1),5.5:(.53,0,.47,1),6.0:(.52,0,.48,1),6.5:(.53,0,.47,1),7.0:(.53,0,.47,1),7.5:(.55,0,.45,1),
8.0:(.53,0,.47,1),8.5:(.52,0,.48,1),9.0:(.48,0,.52,1),9.5:(.47,0,.53,1),10.0:(.48,0,.52,1)}
w=K(T21,wo)
save({"mediaId":766,"level":"A","keyWord":"tattoo","defaultVoice":"female","taps":[
{"phrase":"to look at her arm","target":"the woman","voice":"female","keys":w},
{"phrase":"to touch her chest","target":"the woman","voice":"female","keys":w},
{"phrase":"to hold a piece of paper","target":"the man","voice":"male","keys":K(T21,ma)}],
"stillS":8.0,"nouns":[{"word":"a tattoo","x":.34,"y":.66,"voice":"female"},{"word":"paper","x":.78,"y":.55,"voice":"female"},
{"word":"a plant","x":.66,"y":.31,"voice":"female"},{"word":"glasses","x":.90,"y":.13,"voice":"female"}],
"question":"What is the woman looking at?","answer":["She","is","looking","at","her","new","tattoo."],"answerVoice":"female",
"notes":"At 0-1.5 the man is only his two hands peeling the film off her arm (boxed right of x=.60 and lower, his lower hand at 0.0 reaches under her arm and is cut by the split). At 2.0-3.0 he is not in the picture (3.0: a sliver of his hand at the right edge, left 'off'). From 3.5 the split runs between her body and his hand with the paper; her hand crosses it a little at 6.5-8.0. A cat lies / walks on the window sill in the blurred background (0-3.5, 7.5-9.5), too small and unclear, not used. The hand on the chest shows at 7.5-8.5. The framed pictures on the wall also show birds and roses; the noun is 'paper' (the sheet the man holds), not 'a drawing'. Both give a thumbs up at the end, so no phrase about it."})

# 767
man={0.0:(0,0,.40,.28),0.5:(0,0,.36,.26),1.0:(0,0,.56,.42),1.5:(0,0,.66,.50),2.0:(0,0,.32,.27),2.5:(0,0,.30,.26),3.0:(0,0,.32,.44),
3.5:(0,0,.30,.42),4.0:(0,0,.30,.42),4.5:(0,0,.30,.50),5.0:(0,0,.30,.60),5.5:(0,0,.46,.62),6.0:(0,.02,.46,.58),6.5:(0,.03,.46,.57),
7.0:(0,0,.46,.66),7.5:(0,0,.46,.66),8.0:(0,.17,.48,.48),8.5:(0,.17,.49,.49),9.0:(0,.17,.49,.50),9.5:(0,.18,.49,.50),10.0:(0,.19,.48,.50)}
wo={0.0:(.69,0,.31,.28),0.5:(.70,0,.30,.27),1.0:(.72,0,.28,.33),1.5:(.72,0,.28,.33),2.0:(.64,0,.36,.30),2.5:(.62,0,.38,.31),
3.0:(.66,0,.34,.46),3.5:(.66,0,.34,.44),4.0:(.66,0,.34,.42),4.5:(.68,0,.32,.42),5.0:(.66,0,.34,.52),5.5:(.76,0,.24,.54),
6.0:(.75,.02,.25,.55),6.5:(.75,.08,.25,.52),7.0:(.75,.13,.25,.52),7.5:(.75,.16,.25,.50),8.0:(.50,.19,.50,.47),8.5:(.50,.20,.50,.46),
9.0:(.50,.20,.50,.47),9.5:(.50,.20,.50,.47),10.0:(.49,.18,.51,.50)}
cat={0.0:(.41,0,.27,.14),0.5:(.40,0,.29,.14),5.5:(.48,.31,.27,.14),6.0:(.47,.33,.27,.14),6.5:(.48,.38,.26,.14),7.0:(.47,.42,.27,.14),7.5:(.48,.43,.26,.14)}
save({"mediaId":767,"level":"A","keyWord":"tea","defaultVoice":"male","taps":[
{"phrase":"to pour the tea","target":"the man","voice":"male","keys":K(T21,man)},
{"phrase":"to blow on her tea","target":"the woman","voice":"female","keys":K(T21,wo)},
{"phrase":"to lie on the floor","target":"the cat","voice":"male","keys":K(T21,cat)}],
"stillS":10.0,"nouns":[{"word":"tea","x":.50,"y":.47,"voice":"male"},{"word":"a tray","x":.45,"y":.90,"voice":"male"},
{"word":"a plant","x":.90,"y":.66,"voice":"male"},{"word":"a scarf","x":.82,"y":.24,"voice":"male"}],
"question":"What are the man and woman drinking?","answer":["They","are","drinking","tea","from","small","glasses."],"answerVoice":"male",
"notes":"defaultVoice male: a couple, no single main person, evenId false. At 0-5.0 the two people are only blurred bodies and hands behind the teapot (man = left, green shirt; woman = right, light top). The big hand that drops the mint at 1.0-1.5 comes from the upper left and is boxed as the man's - not certain whose it is; the hands with the spoon (0-0.5) and the water (2.0-2.5) are not assigned. The man pours at 5.5-7.5, his box holds the teapot in his hand but not the stream and the glasses. The woman blows on her glass at 8.0-9.0. The cat is small in the background: sharp at 5.5-7.5, blurred at 0-0.5, hidden / only a white patch at 1.0-5.0 and 8.0-10.0 ('off'); at 5.5-7.5 the woman's box starts right of the cat and loses the tip of her hand. 'tea' pill sits on the two glasses; the teapot also holds tea, so 'a teapot' is not a noun and the 'a tray' pill sits on the front rim of the tray."})

# 768
girl={3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(.39,.46,.19,.15),5.5:(.44,.46,.19,.15),6.0:(.45,.47,.19,.14),6.5:(.38,.47,.18,.14),
7.0:(.42,.43,.19,.17),7.5:(.43,.43,.19,.17),8.0:(.41,.46,.22,.16),8.5:(.42,.48,.18,.15),9.0:(.41,.43,.18,.24),9.5:(.33,.27,.33,.32),10.0:(.30,.23,.38,.39)}
sun={5.0:(.82,.06,.18,.20),5.5:(.80,.04,.20,.20),6.0:(.80,.04,.20,.20),6.5:(.80,.04,.20,.20),7.0:(.72,.04,.28,.20),7.5:(.72,.03,.28,.20),
8.0:(.68,.03,.28,.20),8.5:(.60,.03,.30,.20),9.0:(.56,.03,.30,.19),9.5:(.52,.03,.30,.19),10.0:(.45,.03,.34,.19)}
g=K(T21,girl)
save({"mediaId":768,"level":"A","keyWord":"team","defaultVoice":"female","taps":[
{"phrase":"to wear a white hat","target":"the girl","voice":"female","keys":g},
{"phrase":"to go up in the air","target":"the girl","voice":"female","keys":g},
{"phrase":"to shine over the lake","target":"the sun","voice":"female","keys":K(T21,sun)}],
"stillS":10.0,"nouns":[{"word":"a team","x":.48,"y":.50,"voice":"female"},{"word":"a boat","x":.62,"y":.71,"voice":"female"},
{"word":"the sun","x":.62,"y":.13,"voice":"female"},{"word":"a lake","x":.50,"y":.88,"voice":"female"}],
"question":"What is the team doing?","answer":["The","team","is","rowing","a","boat","on","the","lake."],"answerVoice":"female",
"notes":"defaultVoice female: a mixed group (three men, a woman with a ponytail, the small girl), evenId true. The four rowers all do the same, so no phrase fits only one of them; targets are the girl in the white hat (two phrases, one a state) and the sun. The girl is not identifiable in the first shots (0-3.0, 'off'); she is tiny in the wide shots 5.0-9.0 (minimum-size box that also takes in a bit of her neighbours); at 6.5 she is half hidden by the wooden post. She goes up in the air only at 9.5-10.0. The sun's reflection on the water (7.0-9.0) is not boxed. 'a team' pill sits in the middle of the group at 10.0 (the rowers holding the girl up). 'rowing' in the answer is the least frequent word; the clip ends with the team lifting the girl, the question is about the main action."})
