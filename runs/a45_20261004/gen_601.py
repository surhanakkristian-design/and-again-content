import json
times=[i*0.5 for i in range(21)]
W={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,.49,1),1.5:(0,0,.67,1),2.0:(0,0,.51,1),2.5:(0,0,.51,1),3.0:(0,0,.67,1),3.5:(0,0,.61,1),4.0:(0,0,1,1),4.5:(0,0,1,1),
5.0:(0,0,.80,1),5.5:(0,0,.69,1),6.0:(0,.05,.63,1),6.5:(0,.05,.58,1),7.0:(0,.10,.51,1),7.5:(0,.10,.54,1),8.0:(0,.07,.55,1),8.5:(0,.15,.54,1),9.0:(0,.24,.55,1),
9.5:(.14,.28,.52,1),10.0:(.60,.29,.86,.57)}
F={1.0:(.50,0,1,.72),1.5:(.68,0,1,.21),2.0:(.52,.03,1,.42),2.5:(.52,0,1,.36),3.0:(.68,.02,1,.30),3.5:(.62,.07,1,.38),5.0:(.81,.18,1,.60),5.5:(.70,.24,1,.40),
6.0:(.64,.28,.95,.50),6.5:(.59,.26,.86,.45),7.0:(.52,.26,.87,.42),7.5:(.55,.27,.87,.64),8.0:(.56,.25,.90,.55),8.5:(.55,.26,.92,.62),9.0:(.56,.30,.92,.67),9.5:(.66,.40,.90,.62)}
C={6.0:(.76,.66,.94,.82),7.0:(.68,.63,.87,.77),7.5:(.70,.65,.88,.79),8.0:(.72,.63,.90,.78),8.5:(.74,.63,.92,.78),9.0:(.72,.68,.90,.82),9.5:(.53,.63,.84,.86),10.0:(.05,.58,.78,.93)}
def keys(d):
    out=[]
    for t in times:
        if t in d:
            a,b,c,e=d[t]; out.append({"t":t,"x":a,"y":b,"w":round(c-a,2),"h":round(e-b,2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":601,"level":"A","keyWord":"razor","defaultVoice":"male",
"taps":[
 {"phrase":"to shave with a razor","target":"the man in white","voice":"male","keys":keys(W)},
 {"phrase":"to hold a green shirt","target":"the man in brown","voice":"male","keys":keys(F)},
 {"phrase":"to walk on the sink","target":"the cat","voice":"male","keys":keys(C)}],
"stillS":6.5,
"nouns":[{"word":"a razor","x":.73,"y":.53,"voice":"male"},{"word":"a lamp","x":.84,"y":.06,"voice":"male"},{"word":"a mirror","x":.86,"y":.64,"voice":"male"},{"word":"a T-shirt","x":.25,"y":.62,"voice":"male"}],
"question":"What is the man in white doing?",
"answer":["He","is","shaving","with","a","razor."],
"answerVoice":"male",
"notes":"Close-ups: the man in white fills the frame, the friend in the brown shirt stands behind him; boxes split at the edge of the front man's face, so the front man's hand with the razor sometimes lies outside his box (in front of the friend). The dark green garment the friend holds is called a shirt in the packet; it could also be read as a jacket. The cat walks on the sink only at 9.5-10.0 (sits in the background before; off at 1.0 and 6.5 where it is blurred/hidden). 'a lamp' = hanging light bulb."}
json.dump(c,open('content/601.json','w'),indent=1,ensure_ascii=False)
