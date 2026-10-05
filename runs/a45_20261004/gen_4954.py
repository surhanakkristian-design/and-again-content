import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
B={0.0:(.65,.30,.86,.45),0.5:(.60,.28,.83,.44),1.0:(.58,.29,.82,.46),1.5:(.58,.33,.79,.48),2.0:(.57,.28,.82,.42),
2.5:(.53,.25,.77,.39),3.0:(.65,.28,.92,.43),3.5:(.52,.26,.78,.42),4.0:(.62,.23,.81,.39),4.5:(.57,.26,.76,.41),
5.0:(.59,.23,.79,.39),5.5:(.52,.27,.75,.43),6.0:(.55,.17,.78,.36),6.5:(.42,.07,.69,.32),7.0:(.43,.0,.75,.26),
7.5:(.61,.04,.89,.31),8.0:(.74,.06,1.0,.31),8.5:(.73,.09,1.0,.31),9.0:(.63,.13,.90,.34),9.5:(.47,.19,.73,.39),10.0:(.34,.23,.63,.43)}
W={0.0:(.30,.45,.84,1.0),0.5:(.30,.44,.82,1.0),1.0:(.22,.46,.80,1.0),1.5:(.22,.48,.82,1.0),2.0:(.32,.42,.82,1.0),
2.5:(.32,.39,.83,1.0),3.0:(.33,.43,.80,1.0),3.5:(.28,.42,.84,1.0),4.0:(.30,.40,.82,1.0),4.5:(.35,.41,.86,1.0),
5.0:(.33,.40,.84,1.0),5.5:(.30,.43,.80,1.0),6.0:(.33,.38,.88,1.0),6.5:(.34,.36,1.0,1.0),7.0:(.36,.33,1.0,1.0),
7.5:(.42,.33,1.0,1.0),8.0:(.46,.33,1.0,1.0),8.5:(.47,.32,.98,1.0),9.0:(.52,.35,1.0,1.0),9.5:(.55,.39,1.0,1.0),10.0:(.52,.43,1.0,1.0)}
P={6.5:(.16,.40,.34,.58),7.0:(.13,.40,.34,.60),7.5:(.18,.39,.41,.60),8.0:(.14,.39,.45,.62),8.5:(.10,.40,.40,.64),
9.0:(.05,.40,.36,.68),9.5:(.02,.40,.42,.70),10.0:(.0,.40,.32,.72)}
c={"mediaId":4954,"level":"A","keyWord":"visit","defaultVoice":"female",
"taps":[
 {"phrase":"to carry some flowers","target":"the woman in yellow","voice":"female","keys":K(W)},
 {"phrase":"to clap her hands","target":"the woman in bed","voice":"female","keys":K(P)},
 {"phrase":"to float in the air","target":"the balloon","voice":"female","keys":K(B)}],
"stillS":9.0,
"nouns":[{"word":"a window","x":0.15,"y":0.33,"voice":"female"},
 {"word":"a balloon","x":0.78,"y":0.25,"voice":"female"},
 {"word":"flowers","x":0.50,"y":0.53,"voice":"female"},
 {"word":"a bed","x":0.30,"y":0.76,"voice":"female"}],
"question":"What is the woman in bed doing?",
"answer":["She","is","clapping","her","hands."],
"answerVoice":"female",
"notes":"Woman in yellow box starts below the balloon box (head top slightly cut at 1.0-1.5, 5.5, 9.5-10.0). Woman in bed first seen small through the door window at 6.5 s. Key word visit is not a visible noun. Two nurses at 3.5-4.5 s are not targets."}
json.dump(c,open("content/4954.json","w"),indent=1)
