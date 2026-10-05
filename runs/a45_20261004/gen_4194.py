import json
T=[i*0.5 for i in range(24)]
wo={0.0:(.50,.43,.18,.14),0.5:(.50,.43,.19,.14),1.0:(.49,.43,.19,.15),1.5:(.48,.43,.2,.15),2.0:(.47,.40,.21,.17),2.5:(.47,.40,.22,.17),
3.0:(.45,.40,.23,.18),3.5:(.43,.39,.26,.19),4.0:(.42,.36,.28,.22),4.5:(.41,.35,.34,.25),5.0:(.41,.34,.38,.29),5.5:(.43,.31,.47,.37),
6.0:(.39,.28,.61,.45),6.5:(.17,.27,.83,.49),7.0:(.05,.29,.86,.42),7.5:(.14,.32,.67,.34),8.0:(.30,.34,.49,.28),8.5:(.41,.36,.36,.23),
9.0:(.47,.38,.27,.19),9.5:(.51,.39,.23,.16),10.0:(.54,.39,.19,.14),10.5:(.52,.38,.18,.14),11.0:(.50,.39,.18,.14),11.5:(.48,.39,.18,.14)}
tr={t:(0,0,1,round(wo[t][1],2)) for t in T}
tr[6.0]=(0,.03,1,.25); tr[6.5]=(0,.05,1,.22)
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
v="female"
o={"mediaId":4194,"level":"A","keyWord":"ride","defaultVoice":v,
"taps":[{"phrase":"to drive a pink car","target":"the woman","voice":v,"keys":keys(wo)},
{"phrase":"to grow behind the woman","target":"the trees","voice":v,"keys":keys(tr)},
{"phrase":"to bend her knees","target":"the woman","voice":v,"keys":keys(wo)}],
"stillS":3.0,
"nouns":[{"word":"the sky","x":.82,"y":.10,"voice":v},{"word":"a tree","x":.42,"y":.24,"voice":v},
{"word":"a car","x":.56,"y":.55,"voice":v},{"word":"grass","x":.45,"y":.78,"voice":v}],
"question":"What is the woman doing?","answer":["She","is","going","for","a","ride","in","a","car."],"answerVoice":v,
"notes":"Person taken as a woman from the packet (long hair, sunglasses; could be read as a man - verifier please look at 6.0/6.5). The woman sits in the tiny car, so the car is inside her box and is not a separate tap target. Second target 'the trees' = whatever trees stand behind her in the shot (big oak 0-6.5, poplars and willow 7.0-11.5): its box is the whole band above the woman's box (split on that line), so the oak trunk base and the low willow branches next to her are cut off. Her box is the minimum size 0.18 x 0.14 in the far shots; at 11.5 she is half hidden behind the willow. 'to bend her knees' is clearest 4.0-8.0 (seen from behind after 9.0). Key word 'ride' (noun) is in the answer only; answer has two 'a' chips. Still 3.0: a small orange tree at the left edge besides the oak; the pill is on the oak."}
json.dump(o,open("content/4194.json","w"),indent=1)
