import json
times=[i*0.5 for i in range(30)]
def mk(d):
    out=[]
    for t in times:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
sheet={1.0:(.30,0,.40,.18),1.5:(.25,0,.47,.14),2.0:(.23,0,.54,.23),2.5:(.16,.02,.68,.35),3.0:(.04,.18,.90,.33),3.5:(0,.32,.94,.32),
4.0:(0,.44,1,.30),4.5:(0,.47,1,.32),5.0:(.09,.43,.91,.45),5.5:(.18,.41,.72,.42),6.0:(.19,.40,.38,.42),6.5:(.19,.39,.40,.44),
7.0:(.19,.39,.39,.44),7.5:(.19,.39,.37,.44),8.0:(.19,.37,.37,.44),8.5:(.21,.37,.69,.44),9.0:(.23,.38,.69,.43),9.5:(.18,.29,.50,.17),
10.0:(0,.28,.29,.19),10.5:(0,.38,.20,.24)}
man={6.0:(.57,.42,.23,.28),6.5:(.59,.41,.23,.32),7.0:(.58,.42,.23,.31),7.5:(.56,.42,.25,.31),8.0:(.56,.39,.22,.33),
10.0:(.29,.35,.20,.14),10.5:(.35,.34,.20,.14),11.0:(.36,.33,.22,.15),11.5:(.31,.32,.28,.15),12.0:(.31,.30,.27,.16),
12.5:(.30,.27,.27,.17),13.0:(.30,.20,.27,.19),13.5:(.23,0,.32,.30)}
tiger={9.5:(.42,.47,.28,.29),10.0:(.41,.49,.29,.28),10.5:(.32,.48,.39,.28),11.0:(.29,.48,.43,.26),11.5:(.29,.47,.45,.29),
12.0:(.30,.46,.41,.30),12.5:(.29,.44,.44,.30),13.0:(.29,.39,.47,.36),13.5:(.16,.30,.84,.66),14.0:(.08,0,.92,.92),14.5:(0,0,1,.95)}
c={"mediaId":4107,"level":"A","keyWord":"cover","defaultVoice":"male",
"taps":[{"phrase":"to cover the elephant","target":"the sheet","voice":"male","keys":mk(sheet)},
{"phrase":"to wave his hand","target":"the man","voice":"male","keys":mk(man)},
{"phrase":"to show its teeth","target":"the tiger","voice":"male","keys":mk(tiger)}],
"stillS":12.0,
"nouns":[{"word":"a tiger","x":.50,"y":.55,"voice":"male"},{"word":"a man","x":.46,"y":.41,"voice":"male"},{"word":"a phone","x":.80,"y":.88,"voice":"male"}],
"question":"What is covering the elephant?",
"answer":["A","sheet","is","covering","the","elephant."],"answerVoice":"male",
"notes":"The man is mostly hidden behind the elephant / the sheet before 6.0 s and at 8.5-9.5 s (keys off there). Where the man stands behind the tiger (10.0-13.5 s) his box is only the upper body, split from the tiger box along a horizontal line. Sheet box at 6.0-8.0 s is cut at the man's left edge, so the sheet's train under his feet is outside. Sheet off at 0.0-0.5 s (only a thin streak) and from 11.0 s (dark blob on the floor at the far left). Key word is a verb, used in phrase 1 and the answer; no noun slot for it."}
json.dump(c,open("content/4107.json","w"),indent=1)
