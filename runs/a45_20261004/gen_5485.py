import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
can={0.5:(0,.33,.18,.15),1.0:(0,.36,.18,.14),1.5:(0,.37,.18,.15),2.0:(0,.36,.27,.18),2.5:(0,.33,.37,.21),
3.0:(0,.37,.47,.33),3.5:(0,.37,.65,.40),4.0:(0,.43,.75,.40),4.5:(.13,.46,.65,.35),5.0:(.22,.48,.60,.30),
5.5:(.33,.48,.67,.32),6.0:(.47,.45,.43,.25),6.5:(.47,.46,.43,.25),7.0:(.42,.46,.33,.25),7.5:(.44,.44,.32,.22),
8.0:(.39,.41,.36,.21),8.5:(.33,.41,.34,.22),9.0:(.34,.41,.36,.21),9.5:(.34,.40,.36,.20),10.0:(.36,.44,.33,.18),
10.5:(.33,.48,.37,.21),11.0:(.22,.59,.43,.24),11.5:(.03,.76,.55,.24),12.0:(0,.86,.30,.14)}
wom={4.5:(0,.18,.13,.80),5.0:(0,.21,.22,.79),5.5:(0,.25,.33,.75),6.0:(0,.30,.47,.70),6.5:(0,.34,.47,.66),
7.0:(0,.39,.42,.61),7.5:(0,.40,.44,.60),8.0:(0,.41,.39,.59),8.5:(0,.41,.33,.59),9.0:(0,.40,.34,.60),9.5:(0,.40,.34,.60),
10.0:(0,.39,.36,.60),10.5:(0,.39,.33,.61),11.0:(0,.39,.22,.61),11.5:(0,.39,.30,.37),12.0:(0,.36,.36,.50)}
c={"mediaId":5485,"level":"B","keyWord":"watering can","defaultVoice":"female",
"taps":[
 {"phrase":"to tend her balcony garden","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to spray water from its spout","target":"the watering can","voice":"female","keys":keys(can)},
 {"phrase":"to smile with delight","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":10.0,
"nouns":[{"word":"a lamp","x":0.40,"y":0.12,"voice":"female"},
 {"word":"a fern","x":0.30,"y":0.28,"voice":"female"},
 {"word":"a watering can","x":0.50,"y":0.52,"voice":"female"},
 {"word":"a flowerpot","x":0.78,"y":0.75,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","tending","her","plants","with","a","watering","can."],
"answerVoice":"female",
"notes":"Only two tap targets (woman, can); the woman enters at 4.5 s (only her hand at 4.0 -> off). Can box at 0.5-1.5 s is just the spout tip at the left edge. Woman/can boxes split where her hands hold the can."}
json.dump(c,open('content/5485.json','w'),indent=1)
