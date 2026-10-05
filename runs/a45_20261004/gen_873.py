import json
T=[i*0.5 for i in range(21)]
def bx(t,x0,y0,x1,y1): return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
W={0.0:(.46,.19,1,.70),0.5:(.47,.26,1,1),1.0:(.51,.15,1,1),1.5:(.44,.16,1,1),2.0:(.41,.21,1,1),2.5:(.39,.19,1,1),
3.0:(.04,.71,.42,1),3.5:(0,.70,.30,1),4.5:(0,.29,.60,1),5.0:(0,.28,.42,1),5.5:(.30,.29,.88,1),6.0:(0,.38,.50,1),
6.5:(0,0,.42,1),7.0:(0,.08,.64,1),7.5:(0,.03,.37,1),8.0:(0,.10,.50,.93),8.5:(.03,.23,.52,.62),9.0:(.03,.23,.55,.67),
9.5:(.12,.17,.56,.68),10.0:(.10,.16,.56,.69)}
M={0.0:(.08,.18,.46,.70),0.5:(.07,.23,.47,.90),1.0:(.10,.17,.51,.67),1.5:(.05,.17,.44,.77),2.0:(0,.18,.41,.71),2.5:(0,.18,.39,.74),
3.0:(.42,0,1,1),3.5:(.30,0,1,1),4.0:(.03,0,1,1),4.5:(.60,0,1,1),5.0:(.42,0,1,1),5.5:(0,0,1,.29),6.0:(.50,0,1,1),
6.5:(.72,0,1,1),7.0:(.64,.39,1,.65),7.5:(.57,.10,1,1),8.0:(.54,.11,1,.92),8.5:(.52,.19,1,.63),9.0:(.55,.31,1,.92),
9.5:(.56,.31,1,.92),10.0:(.56,.31,1,.84)}
P={0.0:(.37,.70,.70,.84),0.5:(.20,0,.58,.17),1.0:(.14,.67,.48,.80),1.5:(.04,.77,.38,.91),2.0:(0,.82,.33,.96),2.5:(0,.87,.30,1)}
def keys(d): return [bx(t,*d[t]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":873,"level":"A","keyWord":"wife","defaultVoice":"female",
"taps":[
{"phrase":"to hold a pan","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to clap his hands","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to fly in the air","target":"the pancake","voice":"female","keys":keys(P)}],
"stillS":10.0,
"nouns":[{"word":"a wife","x":0.35,"y":0.47,"voice":"female"},{"word":"a husband","x":0.78,"y":0.47,"voice":"male"},
{"word":"a sofa","x":0.14,"y":0.60,"voice":"female"},{"word":"a table","x":0.50,"y":0.86,"voice":"female"}],
"question":"Who is holding a pan?",
"answer":["The","wife","is","holding","a","pan."],
"answerVoice":"female",
"notes":"Four shots (cuts at about 3.0, 6.5, 8.0 s). All three tap actions happen in the first shot (0-2.5 s); the pancake is only there, off afterwards. In the close shots 3.0-6.0 s only the woman's hand / arm is visible on the man's chest: her box is the hand and arm, his box the largest free rest of his torso (5.5 s: only the band above her hand), so both boxes are rough there; 4.0 s woman off. On the sofa (9.0-10.0 s) her legs lie over his lap and his feet reach under her box: split at x 0.55. In shot 1 the woman's box at 0.0 s ends at y 0.70 above the pancake. Nouns 'a wife' / 'a husband' (key word) label the woman and the man; that they are married is shown only by the rings. Two cups stand apart, so no 'a cup'."}
json.dump(c,open("content/873.json","w"),indent=1)
