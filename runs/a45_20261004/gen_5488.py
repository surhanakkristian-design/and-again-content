import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
fer={0.0:(0,0,.62,.46),0.5:(0,0,.60,.44),1.0:(0,.02,.58,.42),1.5:(0,.17,.92,.58),2.0:(0,.17,.87,.55),2.5:(0,.17,.86,.52),
3.0:(.05,.18,.82,.48),3.5:(.11,.18,.78,.46),4.0:(.17,.20,.72,.44),4.5:(.21,.21,.67,.42),5.0:(.24,.22,.65,.41),5.5:(.26,.24,.62,.39),
6.0:(.36,.34,.29,.21),6.5:(.36,.34,.29,.21),7.0:(.36,.34,.28,.21),7.5:(.37,.34,.27,.21),8.0:(.38,.34,.26,.21),8.5:(.38,.34,.26,.21),
9.0:(.38,.35,.25,.20),9.5:(.38,.35,.25,.20),10.0:(.38,.35,.25,.20)}
wom={0.0:(0,.47,.70,.53),0.5:(0,.45,.68,.55),1.0:(0,.45,.62,.55),4.5:(0,.52,.21,.48),5.0:(0,.52,.24,.48),5.5:(0,.52,.26,.48),
6.0:(0,.43,.30,.55),6.5:(0,.43,.33,.55),7.0:(0,.44,.35,.54),7.5:(0,.46,.36,.52),8.0:(0,.47,.37,.51),8.5:(0,.46,.37,.52),
9.0:(0,.44,.36,.54),9.5:(0,.44,.33,.54),10.0:(0,.45,.33,.53)}
c={"mediaId":5488,"level":"B","keyWord":"farewell","defaultVoice":"female",
"taps":[
 {"phrase":"to pull away from the quay","target":"the ferry","voice":"female","keys":keys(fer)},
 {"phrase":"to wear a flowered headscarf","target":"the old woman","voice":"female","keys":keys(wom)},
 {"phrase":"to leave a foamy wake","target":"the ferry","voice":"female","keys":keys(fer)}],
"stillS":3.0,
"nouns":[{"word":"a flag","x":0.58,"y":0.40,"voice":"female"},
 {"word":"a ferry","x":0.30,"y":0.57,"voice":"female"},
 {"word":"foam","x":0.62,"y":0.78,"voice":"female"},
 {"word":"a bollard","x":0.16,"y":0.83,"voice":"female"}],
"question":"What is the old woman doing?",
"answer":["She","is","waving","farewell","to","the","ferry."],
"answerVoice":"female",
"notes":"Only two targets: waving/grinning/scarf-swinging are shared by many people, so the woman gets a state phrase. Ferry at 0-1 s is the docked ship behind the pair (box cut above the woman's scarf). Woman off at 1.5-4.0 s (at 4.0 only unclear figures at the left edge). Key word 'farewell' is not a visible noun; used in the answer."}
json.dump(c,open('content/5488.json','w'),indent=1)
