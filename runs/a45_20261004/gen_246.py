import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman={0.0:(0,.62,.78,.38),0.5:(0,.53,.80,.47),1.0:(0,.28,.80,.72),1.5:(0,.42,.74,.58),2.0:(0,.76,.70,.24),2.5:(0,.48,.60,.52),
3.0:(0,.76,.63,.24),3.5:(.38,.73,.24,.27),4.0:(.33,.77,.24,.23),4.5:(0,.50,.60,.50),5.0:(0,.54,.68,.46),5.5:(0,.55,.56,.45),
6.0:(0,.60,.50,.40),6.5:(0,.31,.57,.69),7.0:(0,.36,.46,.64),7.5:(0,.35,.45,.65),8.0:(0,.35,.45,.65),8.5:(0,.33,.45,.67),
9.0:(0,.35,.46,.65),9.5:(0,.28,.48,.72),10.0:(0,.32,.48,.68)}
man={2.5:(.80,.48,.20,.24),3.0:(.80,.44,.20,.24),6.5:(.59,.33,.41,.67),7.0:(.58,.62,.42,.38),7.5:(.58,.31,.42,.69),
8.0:(.57,.32,.43,.68),8.5:(.56,.31,.44,.69),9.0:(.56,.31,.44,.69),9.5:(.56,.36,.44,.64),10.0:(.58,.53,.42,.47)}
c={"mediaId":246,"level":"A","keyWord":"driving","defaultVoice":"female",
"taps":[{"phrase":"to drive the car","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to wear a grey hat","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to smile at the driver","target":"the man","voice":"male","keys":keys(man)}],
"stillS":8.5,
"nouns":[{"word":"a mirror","x":.48,"y":.38,"voice":"female"},{"word":"the sea","x":.45,"y":.46,"voice":"female"},
{"word":"a woman","x":.17,"y":.68,"voice":"female"},{"word":"a man","x":.80,"y":.72,"voice":"male"}],
"question":"What is the woman doing?","answer":["She","is","driving","a","car","by","the","sea."],"answerVoice":"female",
"notes":"Only two targets (driver, passenger). 0.0-6.0 s is the driver's point of view: the woman is only her hands and arms on the wheel (face edge at 1.0-1.5 s); her box covers them. The hand pointing from the right at 2.5-3.0 s is taken as the passenger's (man). Second woman phrase is a state (grey hat, visible from 6.5 s) to keep it clearly different from 'to drive the car'. At 7.0 and 10.0 s the man's head is out of frame; box on his body."}
json.dump(c,open("content/246.json","w"),indent=1)
