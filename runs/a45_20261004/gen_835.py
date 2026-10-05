import json
T=[i*0.5 for i in range(31)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2],2),"h":round(d[t][3],2)} if t in d else {"t":t,"off":True}) for t in T]
b={0.0:(.14,.45,.21,.29),0.5:(.09,.44,.30,.36),1.0:(0,.38,.38,.6),1.5:(0,.36,.42,.6),2.0:(0,.28,.45,.55),2.5:(0,.27,.49,.6),
3.0:(0,.3,.52,.68),3.5:(0,.26,.53,.72),
7.0:(.04,.26,.59,.72),7.5:(.1,.18,.54,.8),8.0:(.08,.13,.59,.78),8.5:(.08,.12,.59,.8),9.0:(.06,.12,.62,.86),9.5:(.08,.11,.6,.87),
10.0:(.05,.2,.4,.65),10.5:(.08,.2,.35,.65),11.0:(.06,.2,.37,.77),11.5:(.06,.19,.37,.78),12.0:(.03,.17,.36,.7),12.5:(0,.16,.41,.7),
13.0:(.03,.18,.97,.82),13.5:(.05,.18,.95,.82),14.0:(.03,.2,.97,.8),14.5:(.05,.36,.95,.64),15.0:(.03,.38,.92,.62)}
for t in (4.0,4.5,5.0,5.5,6.0,6.5): b[t]=(0,0,1,1)
w={0.0:(.57,.1,.43,.9),0.5:(.59,.18,.41,.82),1.0:(.52,.23,.48,.77),1.5:(.6,.23,.4,.77),2.0:(.62,.18,.38,.82),2.5:(.69,.08,.31,.92),
3.0:(.74,.03,.26,.97),3.5:(.74,.03,.26,.75),7.0:(.86,0,.14,.22)}
p={0.0:(.37,.45,.19,.14),0.5:(.40,.45,.18,.14),1.0:(.39,.42,.12,.14),1.5:(.43,.39,.16,.12),2.0:(.46,.37,.15,.14),2.5:(.5,.36,.18,.14),
3.0:(.53,.36,.2,.18),3.5:(.54,.36,.19,.18),7.0:(.64,.38,.2,.16),7.5:(.65,.37,.2,.16),8.0:(.68,.35,.22,.16),8.5:(.68,.35,.24,.16),
9.0:(.69,.36,.22,.17),9.5:(.69,.36,.23,.17),
10.0:(.46,0,.54,.44),10.5:(.44,0,.56,.44),11.0:(.44,0,.56,.43),11.5:(.44,0,.56,.43),12.0:(.4,0,.6,.42),12.5:(.42,0,.58,.44)}
c={"mediaId":835,"level":"B","keyWord":"plumber","defaultVoice":"male",
"taps":[{"phrase":"to grip a large wrench","target":"the man in the blue polo","voice":"male","keys":keys(b)},
{"phrase":"to gesture with both hands","target":"the man in the white T-shirt","voice":"male","keys":keys(w)},
{"phrase":"to leak under the sink","target":"the pipe","voice":"male","keys":keys(p)}],
"stillS":12.0,
"nouns":[{"word":"a pipe","x":.80,"y":.20,"voice":"male"},{"word":"a plumber","x":.20,"y":.30,"voice":"male"},
{"word":"a wrench","x":.50,"y":.42,"voice":"male"},{"word":"a toilet","x":.82,"y":.52,"voice":"male"}],
"question":"What is the plumber doing?","answer":["He","is","gripping","a","wrench","under","the","sink."],"answerVoice":"male",
"notes":"The man in the blue polo is labelled 'a plumber' (key word; in the transcript he admits he is an electrician, but the picture shows a tradesman with tool belt and toolbox). The pipe: visibly dripping only in the under-sink shots 10.0-12.5; in the wide shots (0-3.5, 7.0-9.5) it is small, its box is squeezed between the two men and smaller than 0.18 wide at 1.0-2.0; the men's hands are cut by a few hundredths there to avoid overlaps. 10.0-12.5: the man is partly behind the pipe; split on a vertical line, his box holds head and left body only. White-T-shirt man at 7.0 is only a head at the top right edge; OFF at 7.5 (a sliver). 'wrench' is AmE (BrE spanner). Pill 'a wrench' is on the shaft above his fist."}
json.dump(c,open('content/835.json','w'),indent=1)
