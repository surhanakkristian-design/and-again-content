import json
times=[i*0.5 for i in range(31)]
def mk(d):
    out=[]
    for t in times:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
S={0.0:(.74,.55,.24,.20),0.5:(.29,.20,.65,.34),1.0:(.08,.16,.80,.39),1.5:(0,.27,.94,.33),2.0:(0,.35,1,.45),2.5:(0,.41,1,.44),
3.0:(.06,.40,.63,.56),3.5:(.16,.40,.52,.55),4.0:(.16,.41,.51,.42),4.5:(.16,.41,.51,.41),5.0:(.14,.42,.52,.40),5.5:(.14,.43,.50,.39),
6.0:(.12,.44,.50,.36),6.5:(.12,.44,.50,.36),7.0:(.12,.46,.50,.35),7.5:(.12,.46,.50,.35),8.0:(.11,.46,.51,.33),8.5:(.11,.46,.51,.33),
9.0:(.11,.46,.51,.33),9.5:(.11,.46,.51,.33),10.0:(.11,.44,.51,.33),10.5:(.11,.44,.51,.33),11.0:(.42,.43,.46,.25),11.5:(.80,.48,.20,.18)}
C={0.0:(.55,.53,.19,.23),0.5:(.53,.55,.20,.22),1.0:(.62,.55,.20,.23),1.5:(.66,.60,.18,.20),
3.0:(.69,.50,.18,.24),3.5:(.68,.49,.18,.24),4.0:(.67,.49,.18,.23),4.5:(.67,.49,.18,.25),5.0:(.66,.49,.18,.26),5.5:(.64,.49,.18,.28),
6.0:(.62,.47,.19,.27),6.5:(.62,.47,.19,.27),7.0:(.62,.47,.19,.28),7.5:(.62,.47,.19,.28),8.0:(.62,.45,.19,.27),8.5:(.62,.45,.19,.27),
9.0:(.62,.45,.19,.27),9.5:(.62,.45,.19,.27),10.0:(.62,.43,.19,.27),10.5:(.62,.43,.19,.27),
11.5:(.64,.43,.16,.29),12.0:(.58,.40,.32,.30),12.5:(.58,.40,.30,.30),13.0:(.55,.53,.26,.20),13.5:(.56,.49,.25,.22),
14.0:(.50,.59,.36,.14),14.5:(.50,.60,.36,.14),15.0:(.50,.61,.36,.14)}
T={11.0:(.22,.48,.20,.24),11.5:(.11,.44,.52,.28),12.0:(.16,.42,.42,.28),12.5:(.20,.42,.38,.28),13.0:(.12,.43,.43,.29),13.5:(.16,.42,.40,.29),
14.0:(.18,.42,.44,.17),14.5:(.18,.43,.44,.17),15.0:(.18,.44,.44,.17)}
c={"mediaId":4110,"level":"A","keyWord":"clown","defaultVoice":"male",
"taps":[{"phrase":"to lie on the ground","target":"the clown","voice":"male","keys":mk(C)},
{"phrase":"to sit next to the clown","target":"the tiger","voice":"male","keys":mk(T)},
{"phrase":"to fall on the elephant","target":"the cloth","voice":"male","keys":mk(S)}],
"stillS":12.5,
"nouns":[{"word":"a clown","x":.72,"y":.48,"voice":"male"},{"word":"a tiger","x":.40,"y":.57,"voice":"male"},{"word":"a phone","x":.70,"y":.83,"voice":"male"}],
"question":"Where is the tiger sitting?",
"answer":["It","is","sitting","next","to","the","clown."],"answerVoice":"male",
"notes":"defaultVoice male: the clown's gender cannot be seen; the only clearly gendered person is the man in the red suit (not a target, he is half hidden behind the clown most of the time). The clown lies on the ground only at 14.0-15.0 s, behind the tiger's stand: there the clown box is the low strip with the body and the tiger box is cut above it (tiger's paws, tail and the stand are outside). Clown off at 2.0-2.5 s and 11.0 s (hidden by the cloth). Cloth off from 12.0 s (small dark heap at the right edge, too close to the clown for a box). Cloth box at 0.0 s is the dark bundle the man holds at the right. Two phones at the still time; the slot is on the right one, no other noun on the left one."}
json.dump(c,open("content/4110.json","w"),indent=1)
