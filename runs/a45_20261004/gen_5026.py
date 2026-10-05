import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
blue={0.0:(.37,.19,.63,.80),0.5:(.36,.19,.64,.80),1.0:(.32,.19,.68,.80),1.5:(.36,.19,.64,.80),2.0:(.40,.19,.60,.80),
 2.5:(.50,.19,.50,.80),3.0:(.58,.20,.42,.79),3.5:(.58,.22,.42,.77),4.0:(.60,.26,.40,.73),4.5:(.52,.29,.48,.70),
 5.0:(.54,.31,.46,.68),5.5:(.50,.34,.50,.65),6.0:(.48,.38,.52,.62),6.5:(.50,.39,.50,.61),7.0:(.48,.40,.52,.60),
 7.5:(.50,.40,.50,.60),8.0:(.50,.31,.50,.69),8.5:(.50,.29,.50,.71),9.0:(.47,.27,.53,.73),9.5:(.40,.25,.60,.75),10.0:(.31,.22,.69,.78)}
black={0.0:(.02,.24,.34,.30),0.5:(.02,.25,.34,.30),1.0:(.02,.26,.30,.30),1.5:(.02,.27,.34,.30),2.0:(.02,.26,.37,.32),
 4.0:(.18,.29,.42,.30),4.5:(.02,.43,.48,.27),5.0:(.02,.37,.52,.34),5.5:(.0,.41,.48,.37),6.0:(.0,.57,.46,.24),
 6.5:(.0,.58,.48,.26),7.0:(.0,.60,.44,.26),7.5:(.0,.57,.30,.20),8.0:(.05,.54,.43,.22),8.5:(.20,.50,.28,.21),
 9.0:(.13,.36,.33,.22),9.5:(.0,.35,.38,.24),10.0:(.0,.36,.30,.25)}
girl={2.5:(.0,.29,.50,.65),3.0:(.02,.29,.56,.67),3.5:(.0,.31,.58,.65),4.0:(.0,.60,.34,.36)}
c={"mediaId":5026,"level":"B","keyWord":"hilarious","defaultVoice":"male",
"taps":[
 {"phrase":"to wipe away tears","target":"the man with blue hair","voice":"male","keys":K(blue)},
 {"phrase":"to throw his head back","target":"the man in black","voice":"male","keys":K(black)},
 {"phrase":"to stare with wide eyes","target":"the girl with braids","voice":"female","keys":K(girl)}],
"stillS":4.0,
"nouns":[{"word":"a whiteboard","x":.50,"y":.25,"voice":"male"},{"word":"a laptop","x":.28,"y":.60,"voice":"male"},
 {"word":"a hoodie","x":.80,"y":.74,"voice":"male"},{"word":"a smartphone","x":.42,"y":.88,"voice":"male"}],
"question":"What is the blue-haired student doing?",
"answer":["He","is","wiping","away","tears","of","laughter."],"answerVoice":"male",
"notes":"Man in black hidden 2.5-3.5; from 8.5 he has fallen back and only his raised legs/feet show (boxes on the legs). Girl with braids only partly at left edge at 2.0 (off) and 4.0 (braid + shoulder). Blue man's box starts right of his neighbours, so his phone hand at lower left is outside the box in some frames."}
json.dump(c,open('content/5026.json','w'),indent=1)
