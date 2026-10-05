import json
T=[i*0.5 for i in range(24)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(.07,.41,.48,.22),0.5:(.07,.41,.48,.22),1.0:(.07,.41,.48,.22),1.5:(.07,.41,.54,.22),2.0:(.10,.39,.50,.24),
2.5:(.16,.35,.46,.28),3.0:(.16,.35,.47,.28),3.5:(.10,.38,.53,.25),4.0:(.05,.39,.50,.24),4.5:(.05,.39,.50,.24),5.0:(.05,.39,.50,.24),
5.5:(.14,.36,.50,.27),6.0:(.14,.35,.50,.28),6.5:(.04,.38,.52,.25),7.0:(.03,.38,.53,.25),7.5:(.03,.38,.53,.25),8.0:(.03,.38,.53,.25),
8.5:(.13,.35,.53,.28),9.0:(.13,.35,.53,.28),9.5:(.03,.06,.63,.55),10.0:(0,.25,.87,.44),10.5:(.20,.25,.80,.44)}
bl={float(t)/2:(.13,.64,.87,.32) for t in range(0,19)}
bl.update({9.5:(.53,.62,.47,.38),10.0:(0,.03,.94,.21),10.5:(0,.03,.94,.21),11.0:(0,.07,.97,.20),11.5:(0,.58,.72,.20)})
cu={0.0:(.61,.09,.23,.44),0.5:(.61,.09,.23,.44),1.0:(.62,.09,.23,.44),1.5:(.62,.08,.23,.45),2.0:(.62,.07,.24,.45),
2.5:(.63,.06,.23,.46),3.0:(.64,.06,.23,.46),3.5:(.64,.06,.23,.46),4.0:(.63,.05,.25,.46),4.5:(.63,.05,.25,.46),5.0:(.63,.05,.25,.46),
5.5:(.65,.03,.24,.47),6.0:(.65,.03,.24,.47),6.5:(.64,.02,.25,.48),7.0:(.64,.02,.25,.48),7.5:(.64,.02,.25,.48),8.0:(.64,.02,.25,.48),
8.5:(.67,.02,.22,.48),9.0:(.67,.02,.22,.48),9.5:(.67,.0,.23,.25),10.5:(0,.25,.19,.33),11.0:(0,.28,.22,.29),11.5:(0,.14,.24,.43)}
c={"mediaId":4197,"level":"A","keyWord":"late","defaultVoice":"male",
"taps":[{"phrase":"to wake up late","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to fly through the air","target":"the blanket","voice":"male","keys":K(bl)},
{"phrase":"to hang by the window","target":"the curtain","voice":"male","keys":K(cu)}],
"stillS":9.0,
"nouns":[{"word":"a phone","x":.58,"y":.47,"voice":"male"},{"word":"a blanket","x":.60,"y":.75,"voice":"male"},
{"word":"a curtain","x":.76,"y":.25,"voice":"male"},{"word":"a pillow","x":.13,"y":.58,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","waking","up","late."],"answerVoice":"male",
"notes":"Cartoon character in a red cap = 'the man'. Man box = head, cap, arm and phone; his body is under the blanket, so the blanket box starts just below the head (y 0.64). At 9.5 s his raised hand with the phone is in front of the curtain: the man box ends at x 0.66 and the curtain box holds only the curtain top, the hand/phone area belongs to no box. At 10.0-10.5 s the man is the whirl; curtain off at 10.0 s (hidden behind the whirl). The cap also jumps off his head at 9.5 s, but only the blanket flies through the air."}
json.dump(c,open("content/4197.json","w"),indent=1)
