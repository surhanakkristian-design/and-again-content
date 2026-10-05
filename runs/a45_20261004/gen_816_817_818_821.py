import json
def K(T,d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=v; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def save(c): json.dump(c,open("content/%d.json"%c["mediaId"],"w"),indent=1,ensure_ascii=False)
T21=[i*0.5 for i in range(21)]; T11=T21[:11]; T19=T21[:19]

# 816
W={0.0:(0,.30,.47,1),0.5:(0,.30,.44,1),1.0:(0,.30,.43,1),1.5:(0,.30,.40,1),2.0:(0,.28,.36,1),2.5:(0,.28,.38,1),
3.0:(0,.30,.38,1),3.5:(0,.30,.37,1),4.0:(0,.28,.37,1),4.5:(0,.28,.30,1),5.0:(0,.28,.24,1),5.5:(0,.28,.30,1),
6.0:(.17,.26,.40,1),6.5:(.38,.27,.56,.95),7.0:(.37,.28,.55,.95),7.5:(.42,.28,.60,.95),8.0:(.43,.27,.61,.90),
8.5:(.45,.27,.63,.88),9.0:(.43,.28,.61,.90)}
M={0.0:(.47,.20,1,1),0.5:(.44,.20,1,1),1.0:(.43,.20,1,1),1.5:(.40,.20,1,1),2.0:(.36,.18,1,1),2.5:(.38,.17,1,1),
3.0:(.38,.20,1,1),3.5:(.37,.20,1,1),4.0:(.37,.18,1,1),4.5:(.30,.17,1,1),5.0:(.24,.20,1,1),5.5:(.30,.20,.95,1),
6.0:(.40,.17,1,1),6.5:(0,0,.38,1),7.0:(0,.08,.37,1),7.5:(0,0,.42,1),8.0:(0,.03,.43,1),8.5:(0,.03,.45,1),
9.0:(0,.07,.43,1),9.5:(.08,.08,.97,1),10.0:(.18,.12,.88,.98)}
save({"mediaId":816,"level":"B","keyWord":"tuxedo","defaultVoice":"male","taps":[
{"phrase":"to button up a jacket","target":"the man","voice":"male","keys":K(T21,M)},
{"phrase":"to admire his own reflection","target":"the man","voice":"male","keys":K(T21,M)},
{"phrase":"to wear an emerald gown","target":"the woman","voice":"female","keys":K(T21,W)}],
"stillS":6.0,
"nouns":[{"word":"a mirror","x":.60,"y":.09,"voice":"male"},{"word":"a bow tie","x":.65,"y":.37,"voice":"male"},
{"word":"a tuxedo","x":.68,"y":.55,"voice":"male"},{"word":"a gown","x":.30,"y":.66,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","admiring","his","tuxedo","in","the","mirror."],"answerVoice":"male",
"notes":"From 6.5 s the man is seen twice (real, from behind, in the foreground + his reflection) with the woman's reflection between them: 6.5-9.0 s the man's box is the REAL man in the foreground only (the reflection cannot be included without covering the woman); at 6.0 s only the reflection is in the picture (box on it); 9.5-10.0 s box = man + reflection, woman hidden (off). Woman phrase is a state: her only action (helping with the bow tie) is something the man also does himself. The still at 6.0 s is a mirror view; 'a mirror' pill sits on the top of the mirror glass."})

# 817
WC={t:(.24,.47,.52,.97) for t in T11}; WC[5.0]=(.24,.47,.53,.97)
BC={t:(.52,.48,.82,1) for t in T11}; BC[5.0]=(.53,.48,.82,1)
L={t:(0,.15,1,.29) for t in T11}
save({"mediaId":817,"level":"B","keyWord":"side by side","defaultVoice":"male","taps":[
{"phrase":"to have fluffy white fur","target":"the white cat","voice":"male","keys":K(T11,WC)},
{"phrase":"to swish a black tail","target":"the black cat","voice":"male","keys":K(T11,BC)},
{"phrase":"to glimmer on the horizon","target":"the lights","voice":"male","keys":K(T11,L)}],
"stillS":2.5,
"nouns":[{"word":"the sky","x":.50,"y":.08,"voice":"male"},{"word":"the horizon","x":.50,"y":.22,"voice":"male"},
{"word":"waves","x":.16,"y":.56,"voice":"male"},{"word":"a concrete block","x":.25,"y":.95,"voice":"male"}],
"question":"What are the two cats doing?",
"answer":["They","are","sitting","side by side."],"answerVoice":"male",
"notes":"Both cats do the same thing, so the cat phrases separate them by colour (state for the white cat; the black cat's tail visibly swings, the white tail hardly moves). Third target = the row of lights on the horizon. 'side by side.' kept as one chip. 'the horizon' pill lies on the line of lights."})

# 818
Wm={0.0:(0,.12,.47,.72),0.5:(0,.17,.53,.68),1.0:(0,.08,.50,.72),1.5:(0,.08,.50,.72),2.0:(0,.05,.49,.72),2.5:(0,.07,.50,.72),
3.0:(0,.08,.49,.75),3.5:(0,.08,.50,.75),4.0:(0,.07,.50,.72),4.5:(0,.07,.50,.72),5.0:(0,.08,.49,.75),5.5:(0,.08,.50,.75),
6.0:(0,.08,.49,.72),6.5:(0,.10,.50,.72),7.0:(0,.12,.48,.75),7.5:(0,.17,.50,.78),8.0:(0,.17,.47,.68),8.5:(0,.13,.48,.70),
9.0:(0,.13,.47,.75),9.5:(0,.13,.48,.75),10.0:(0,.13,.50,.68)}
Mm={0.0:(.47,.21,1,.54),0.5:(.53,.18,1,.52),1.0:(.50,.21,1,.57),1.5:(.50,.20,1,.57),2.0:(.49,.15,.77,.52),2.5:(.50,.17,.76,.55),
3.0:(.49,.19,.75,.57),3.5:(.50,.18,.73,.58),4.0:(.50,.19,.73,.55),4.5:(.50,.19,.72,.55),5.0:(.49,.19,.74,.60),5.5:(.50,.19,.76,.60),
6.0:(.49,.19,.78,.52),6.5:(.50,.19,.79,.52),7.0:(.48,.20,.82,.62),7.5:(.50,.20,.82,.62),8.0:(.47,.20,.82,.52),8.5:(.48,.21,.80,.53),
9.0:(.47,.22,.80,.62),9.5:(.48,.22,.80,.62),10.0:(.50,.21,.82,.55)}
Cm={2.0:(.77,.22,.96,.38),2.5:(.76,.23,.95,.39),3.0:(.75,.25,.94,.41),3.5:(.73,.25,.93,.41),4.0:(.73,.23,.93,.39),4.5:(.72,.23,.92,.39),
5.0:(.74,.24,.94,.40),5.5:(.76,.24,.95,.40),6.0:(.78,.24,.97,.40),6.5:(.79,.24,.98,.40),7.0:(.82,.29,1,.43),7.5:(.82,.29,1,.43),
8.0:(.82,.27,1,.41),8.5:(.82,.27,1,.41),9.0:(.82,.28,1,.42),9.5:(.82,.28,1,.42),10.0:(.82,.25,1,.39)}
save({"mediaId":818,"level":"A","keyWord":"typing","defaultVoice":"female","taps":[
{"phrase":"to throw both arms up","target":"the woman","voice":"female","keys":K(T21,Wm)},
{"phrase":"to have a dark beard","target":"the man","voice":"male","keys":K(T21,Mm)},
{"phrase":"to walk by the window","target":"the cat","voice":"female","keys":K(T21,Cm)}],
"stillS":4.0,
"nouns":[{"word":"a window","x":.72,"y":.10,"voice":"female"},{"word":"a cat","x":.82,"y":.32,"voice":"female"},
{"word":"a keyboard","x":.58,"y":.63,"voice":"female"},{"word":"a table","x":.40,"y":.86,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","typing","on","a","keyboard."],"answerVoice":"female",
"notes":"Woman / man boxes are split along a vertical line: the woman's hands on the keyboard (right of the line, below the man) and, at 7.0-8.0 s, her outstretched arm in front of the man fall outside her box. The man's box is cut on the right where the cat walks behind him (his far arm is outside). The cat is small in the background (from 2.0 s; at 0-1.5 s not yet clearly visible -> off; 9.0-10.0 s only half in the picture at the right edge). 'to type' was not used as a tap phrase because the man also has his hands on a laptop at the start; the man's phrase is a state for the same reason (both look, both open their mouths)."})

# 821
Mn={0.0:(0,0,1,1),0.5:(.02,.15,1,.86),1.0:(.08,.10,.92,.80),1.5:(.03,.08,.97,.80),2.0:(.03,.07,.98,.80),2.5:(.08,.07,.92,.80),
3.0:(.02,.08,.98,.80),3.5:(0,.08,1,.80),4.0:(0,.05,1,.80),4.5:(0,.09,1,.80),5.0:(.02,.10,1,.90),5.5:(.22,.18,.98,.74),
6.0:(.17,.10,1,.90),6.5:(.17,.10,1,.90),7.5:(.14,.14,.88,.74),8.0:(.05,.13,.95,.68),8.5:(.08,.12,.92,.72),9.0:(.08,.10,.92,.72)}
ph=["to put on a white shirt","to zip up a blue jacket","to give two thumbs up"]
save({"mediaId":821,"level":"A","keyWord":"underwear","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":K(T19,Mn)} for p in ph],
"stillS":2.0,
"nouns":[{"word":"a window","x":.78,"y":.25,"voice":"male"},{"word":"underwear","x":.50,"y":.62,"voice":"male"},
{"word":"a drawer","x":.50,"y":.88,"voice":"male"}],
"question":"What is the man putting on?",
"answer":["He","is","putting","on","warm","clothes."],"answerVoice":"male",
"notes":"Cartoon with one character only: all three phrases have the man as target. 7.0 s shows only the closed door (off). From 7.5 s the heap of taken-off clothes in front of him is not inside his box. 'underwear' labels the white undershirt he holds up at 2.0 s."})
