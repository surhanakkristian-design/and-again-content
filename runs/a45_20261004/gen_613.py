import json
times=[i*0.5 for i in range(21)]
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
box={0.0:(.28,.40,.50,.46),0.5:(.13,.18,.57,.70),1.0:(0,.16,.87,.78),1.5:(.09,.22,.76,.52),2.0:(.17,.25,.55,.41),2.5:(.14,.30,.50,.36),3.0:(.37,.27,.52,.50),3.5:(.28,.23,.40,.55),
4.0:(.21,.24,.34,.47),4.5:(.07,.27,.50,.46),5.0:(.02,.27,.53,.49),5.5:(.09,.27,.54,.49),6.0:(.02,.29,.56,.50),6.5:(.17,.31,.51,.44),7.0:(.45,.33,.36,.38),7.5:(.37,.33,.41,.33),
8.0:(.12,.30,.50,.50),8.5:(0,.32,.62,.63),9.0:(0,.32,.64,.68),9.5:(0,.30,.81,.70),10.0:(0,.27,.97,.73)}
coach={0.0:(.78,.13,.22,.87),0.5:(.72,.40,.28,.14),7.5:(.82,.42,.18,.20),8.0:(.82,.44,.18,.38),8.5:(.82,.40,.18,.47),9.0:(.64,.33,.36,.67),9.5:(.82,.38,.18,.28)}
c={"mediaId":613,"level":"A","keyWord":"ring","defaultVoice":"male",
"taps":[{"phrase":"to climb into the ring","target":"the man in white","voice":"male","keys":keys(box)},
{"phrase":"to wear blue gloves","target":"the man in white","voice":"male","keys":keys(box)},
{"phrase":"to hold a water bottle","target":"the person in black","voice":"male","keys":keys(coach)}],
"stillS":4.0,
"nouns":[{"word":"a ring","x":.55,"y":.80,"voice":"male"},{"word":"a man","x":.36,"y":.42,"voice":"male"},{"word":"a lamp","x":.28,"y":.08,"voice":"male"},{"word":"a wall","x":.66,"y":.20,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","boxing","in","the","ring."],"answerVoice":"male",
"notes":"Only two usable targets: the boxer (white T-shirt) and the coach in black, whose gender is not clear (hair in a bun, seen only at 0.0 and then as a hand with the bottle at 7.5-9.5) - hence 'the person in black' and the default voice. Coach at 0.0: the arm reaching to the rope lies in the boxer's box. 'a ring' pill sits on the ring floor (the ropes are deliberately not a noun). A child is small in the far background at 5.0-6.5."}
json.dump(c,open('content/613.json','w'),indent=1,ensure_ascii=False)
