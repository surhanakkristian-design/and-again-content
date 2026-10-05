import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4550
t=T(25)
w={0.0:(.66,.22,1,.84),0.5:(.50,.20,1,.86),1.0:(.46,.17,1,.95),1.5:(.43,.12,1,.95),2.0:(.39,.04,1,.86),2.5:(.39,.03,1,.88),
   3.0:(.41,.03,1,.97),3.5:(.41,.03,1,.97),4.0:(.43,.02,1,.92),4.5:(.43,.02,1,.92)}
m={0.0:(0,.40,.47,.94),0.5:(0,.40,.49,.94),1.0:(0,.53,.45,.97),1.5:(0,.53,.42,.97),2.0:(0,.42,.38,.96),2.5:(0,.42,.38,.96),
   3.0:(0,.55,.40,.98),3.5:(0,.50,.40,.98),4.0:(0,.46,.42,.96),4.5:(0,.46,.42,.96)}
for x in (5.0,5.5,6.0,6.5,7.0): w[x]=(.48,.10,1,.74); m[x]=(0,.28,.47,.98)
for x in (7.5,8.0,8.5,9.0): w[x]=(0,0,1,.74); m[x]=(0,.76,.18,.96)
w[9.5]=(.10,.06,.97,.82); m[9.5]=(0,.33,.09,.97)
for x in (10.0,10.5,11.0,11.5,12.0): w[x]=(.08,.02,.97,.84); m[x]=(0,.28,.07,.97)
save({"mediaId":4550,"level":"A","keyWord":"finally","defaultVoice":"female",
 "taps":[{"phrase":"to wait for her coffee","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to drink from a mug","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to fill the glass jug","target":"the coffee machine","voice":"female","keys":K(t,m)}],
 "stillS":6.0,
 "nouns":[{"word":"a woman","x":0.70,"y":0.30,"voice":"female"},{"word":"a coffee machine","x":0.22,"y":0.40,"voice":"female"},
          {"word":"coffee","x":0.24,"y":0.74,"voice":"female"},{"word":"a mug","x":0.74,"y":0.84,"voice":"female"}],
 "question":"What is the woman waiting for?",
 "answer":["She","is","waiting","for","her","coffee."],"answerVoice":"female",
 "notes":"Key word 'finally' is an adverb, left out of the chips (free position). Third target = the coffee machine incl. its glass jug; from 7.5 s only its base is in the picture (bottom left), from 9.5 s only a strip at the left edge (box narrower than the minimum so it does not cut into the woman). The woman's box is cut on the left where she reaches over the machine (2.0-4.5 s). The mug was not used as a target because she holds it in front of her face at the end."})

# ---------- 4551
man={0.0:(0,.15,.39,.62),0.5:(0,.16,.39,.66),1.0:(0,.18,.42,.78),1.5:(0,.25,.46,.60),2.0:(0,.44,.56,.95),2.5:(0,.48,.54,.95),
 3.0:(0,.67,.68,.97),3.5:(0,.63,.82,1.0),4.0:(.24,.56,.68,.94),4.5:(.28,.57,.70,.88),5.0:(.34,.66,.66,.82),5.5:(.33,.64,.68,.80),
 6.0:(.26,.62,.62,.86),6.5:(.27,.56,.78,.89),7.0:(.20,.66,.68,.95),7.5:(.12,.73,.78,.90),8.0:(.12,.63,.80,.82),8.5:(.08,.75,.86,.90),
 9.0:(.08,.75,.86,.90),9.5:(.08,.75,.86,.90),10.0:(.08,.75,.86,.90),10.5:(.08,.75,.86,.90),11.0:(.26,.42,.74,.60),11.5:(.30,.42,.78,.59),12.0:(.26,.43,.72,.57)}
ot={0.0:(.40,.50,1,1),0.5:(.40,.49,1,1),1.0:(.43,.51,1,1),1.5:(.47,.52,1,1),2.0:(.57,.38,1,1),2.5:(.55,.34,1,1),
 3.0:(.39,.36,1,.66),3.5:(.39,.34,1,.62),4.0:(.37,.31,1,.55),4.5:(.38,.31,1,.56),5.0:(.36,.31,1,.65),5.5:(.41,.31,1,.63),
 6.0:(.41,.28,1,.61),6.5:(.38,.32,1,.55),7.0:(.38,.33,1,.65),7.5:(0,.50,1,.72),8.0:(0,.48,1,.62),8.5:(0,.48,1,.74),
 9.0:(0,.48,1,.74),9.5:(0,.48,1,.74),10.0:(0,.48,1,.74),10.5:(0,.53,1,.74),11.0:(0,.61,1,.76),11.5:(0,.60,1,.76),12.0:(0,.58,1,.77)}
gt={0.0:(.40,.37,.60,.49),0.5:(.40,.37,.60,.48),1.0:(.43,.38,.58,.50),1.5:(.47,.40,.60,.51),2.0:(.28,.33,.49,.43),2.5:(.15,.33,.38,.47),
 3.0:(.15,.33,.38,.47),3.5:(.15,.33,.38,.47),4.0:(.15,.28,.36,.43),4.5:(.13,.29,.37,.44),5.0:(.13,.28,.35,.42),5.5:(.18,.28,.40,.42),
 6.0:(.13,.27,.40,.43),6.5:(.10,.28,.37,.44),7.0:(.12,.28,.37,.45),7.5:(.11,.27,.50,.47),8.0:(.11,.26,.51,.45),8.5:(.11,.25,.52,.44),
 9.0:(.12,.25,.52,.45),9.5:(.12,.25,.52,.45),10.0:(.12,.25,.52,.45),10.5:(.12,.25,.52,.45),11.0:(.11,.25,.51,.41),11.5:(.11,.25,.52,.41),12.0:(.11,.26,.51,.42)}
save({"mediaId":4551,"level":"A","keyWord":"camp","defaultVoice":"male",
 "taps":[{"phrase":"to crawl into a tent","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to fall on the man","target":"the orange tent","voice":"male","keys":K(t,ot)},
         {"phrase":"to stand by the lake","target":"the green tent","voice":"male","keys":K(t,gt)}],
 "stillS":12.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"male"},{"word":"a lake","x":0.60,"y":0.33,"voice":"male"},
          {"word":"a man","x":0.55,"y":0.50,"voice":"male"},{"word":"boots","x":0.45,"y":0.83,"voice":"male"}],
 "question":"Where is the man camping?",
 "answer":["He","is","camping","by","a","lake."],"answerVoice":"male",
 "notes":"Man and orange tent overlap for most of the clip, boxes are split: 0-2.5 s man left / tent right; 3.0-10.5 s the man's box is the part of him sticking out of the tent (back, then boots), the tent box is the strip above; from 11.0 s the man's box is his upper body above the tent, his boots are in no box. At 10.5 s only the top of his head shows behind the tent (in no box). Green tent is small and partly behind the man in 0-1.5 s (boxes there below the minimum size). 'to stand by the lake': the green tent is right on the shore; the people in the background sit / stand there too but are people, not tents - verifier please judge. No 'a tent' noun because three tents are visible."})

# ---------- 4553
t=T(21)
w={};d={}
for x in (0.0,0.5,2.0,2.5,4.0,4.5): w[x]=(0,0,1,.77); d[x]=(.48,.78,1,1)
for x in (1.0,1.5,3.0,3.5,5.0,5.5): w[x]=(0,0,1,.77); d[x]=(.48,.78,1,1)
w.update({6.0:(0,.30,.55,1.0),6.5:(0,.22,.85,.63),7.0:(0,.13,.75,.60),7.5:(0,.08,.72,.55),8.0:(0,.06,.40,.80),8.5:(0,.05,.40,.75),
          9.0:(0,.08,.85,.49),9.5:(0,.18,.95,.43),10.0:(0,.14,.92,.41)})
d.update({6.0:(.56,.74,1,1),6.5:(.50,.64,1,1),7.0:(.42,.61,1,1),7.5:(.42,.56,1,1),8.0:(.41,.43,1,1),8.5:(.41,.42,1,1),
          9.0:(.40,.50,.95,1),9.5:(.38,.44,1,1),10.0:(.36,.42,.95,1)})
save({"mediaId":4553,"level":"A","keyWord":"hair","defaultVoice":"female",
 "taps":[{"phrase":"to brush her long hair","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to hold a brush","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to sit by the woman","target":"the dog","voice":"female","keys":K(t,d)}],
 "stillS":10.0,
 "nouns":[{"word":"hair","x":0.76,"y":0.34,"voice":"female"},{"word":"a brush","x":0.28,"y":0.27,"voice":"female"},
          {"word":"a dog","x":0.60,"y":0.60,"voice":"female"},{"word":"a rug","x":0.30,"y":0.85,"voice":"female"}],
 "question":"What is the woman holding?",
 "answer":["She","is","holding","a","brush."],"answerVoice":"female",
 "notes":"Only two targets (woman, dog). 0-5.5 s the dog is only a blurred golden back at the bottom right. From 6.5 s woman and dog overlap: the woman's box is her upper body, the dog's box the dog; her legs on the left are in no box (8.0-8.5 s split left/right instead). At 6.0 s a large fluffy shape behind the woman (generation glitch) is in no box. Dog phrase is a state because nothing the dog does is unique and clear."})

# ---------- 4554
t=T(19)
ms={0.0:(0,0,.75,.62),0.5:(0,.02,.70,.58),1.0:(0,.24,.46,.55),1.5:(0,.20,.36,.48),2.0:(0,.22,.24,.46)}
to={1.0:(0,.68,1,1),1.5:(.08,.54,1,1),2.0:(.04,.49,.83,1),2.5:(0,.60,.18,1),3.0:(0,.57,.12,.84),3.5:(0,.56,.12,.82),4.0:(0,.57,.13,.83),
    4.5:(0,.59,.13,.86),5.0:(0,.61,.18,.87),5.5:(0,.61,.17,.87),6.0:(0,.60,.10,.87),6.5:(0,.61,.10,.87),7.0:(0,.58,.10,.86),7.5:(0,.61,.12,.86),
    8.0:(0,.60,.15,.86),8.5:(0,.60,.15,.86),9.0:(0,.60,.17,.87)}
mn={1.5:(.88,0,1,.35),2.0:(.84,0,1,.68),2.5:(.36,0,1,.68),3.0:(.20,0,.88,.80),3.5:(.23,.06,.90,.80),4.0:(.22,.13,.88,.72),4.5:(.20,.18,.80,.74),
    5.0:(.19,.18,.74,.82),5.5:(.18,.18,.76,.80),6.0:(.11,.18,.76,.72),6.5:(.11,.15,.73,.72),7.0:(.11,.15,.74,.86),7.5:(.13,.15,.78,.82),
    8.0:(.16,.15,.73,.74),8.5:(.16,.18,.72,.76),9.0:(.18,.16,.78,.86)}
save({"mediaId":4554,"level":"B","keyWord":"flame","defaultVoice":"male",
 "taps":[{"phrase":"to turn sausages with tongs","target":"the bearded man","voice":"male","keys":K(t,mn)},
         {"phrase":"to char on a stick","target":"the marshmallow","voice":"male","keys":K(t,ms)},
         {"phrase":"to scorch the toast","target":"the toaster","voice":"male","keys":K(t,to)}],
 "stillS":7.0,
 "nouns":[{"word":"an apron","x":0.33,"y":0.44,"voice":"male"},{"word":"flames","x":0.62,"y":0.53,"voice":"male"},
          {"word":"tongs","x":0.30,"y":0.63,"voice":"male"},{"word":"sausages","x":0.78,"y":0.80,"voice":"male"}],
 "question":"What is the bearded man doing?",
 "answer":["He","is","turning","sausages","over","the","flames."],"answerVoice":"male",
 "notes":"Marshmallow box includes its flame and stick; it leaves the picture after 2.0 s. The toaster is large at 1.0-2.0 s, then a small strip at the left edge. At 1.5-2.0 s only the man's arm / side is in the picture at the right edge. The man's box also covers parts of the relatives behind him (not targets). He holds tongs in both hands; the 'tongs' pill is on the left pair."})
