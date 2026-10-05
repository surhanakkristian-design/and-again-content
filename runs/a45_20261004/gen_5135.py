import json
T=[i*0.5 for i in range(21)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
woman={0.0:(.25,.23,.20,.18),0.5:(.25,.23,.20,.18),1.0:(.25,.24,.20,.18),1.5:(.26,.24,.21,.18),2.0:(.29,.26,.20,.18),
 2.5:(.33,.28,.24,.18),3.0:(.35,.27,.27,.19),3.5:(.45,.27,.20,.16),4.0:(.45,.27,.20,.15),4.5:(.43,.27,.20,.16),
 5.0:(.40,.28,.20,.16),5.5:(.36,.27,.20,.16),6.0:(.33,.24,.20,.16),6.5:(.34,.24,.20,.16),7.0:(.38,.27,.20,.16),
 7.5:(.36,.29,.20,.37),8.0:(.27,.23,.22,.42),8.5:(.22,.16,.40,.50),9.0:(.11,.25,.42,.43),9.5:(.13,.26,.27,.41),10.0:(0,.16,.34,.48)}
car={0.0:(.18,.41,.82,.37),0.5:(.18,.41,.82,.38),1.0:(.13,.42,.87,.39),1.5:(.12,.42,.88,.40),2.0:(.15,.44,.85,.44),
 2.5:(.17,.46,.83,.48),3.0:(.18,.46,.82,.54),3.5:(.17,.44,.83,.56),4.0:(.17,.43,.83,.57),4.5:(.17,.44,.83,.56),
 5.0:(.18,.45,.82,.53),5.5:(.18,.44,.82,.48),6.0:(.18,.41,.82,.38),6.5:(.18,.41,.82,.38),7.0:(.22,.44,.78,.36),
 7.5:(.57,.25,.43,.58),8.0:(.50,.24,.50,.55),8.5:(.63,.24,.37,.57),9.0:(.54,.29,.46,.53),9.5:(.41,.30,.59,.52),10.0:(.37,.26,.63,.55)}
man={7.0:(0,.19,.12,.27),7.5:(0,.19,.12,.27),8.0:(0,.17,.18,.30),8.5:(0,.19,.18,.28),9.0:(0,.25,.105,.24),9.5:(0,.19,.125,.29)}
c={"mediaId":5135,"level":"B","keyWord":"space","defaultVoice":"female",
"taps":[
 {"phrase":"to lean out of the window","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to squeeze into a tight space","target":"the blue car","voice":"female","keys":K(car)},
 {"phrase":"to read a newspaper","target":"the old man","voice":"male","keys":K(man)}],
"stillS":8.5,
"nouns":[{"word":"an awning","x":0.56,"y":0.09,"voice":"female"},{"word":"a newspaper","x":0.10,"y":0.245,"voice":"female"},
 {"word":"a rear light","x":0.86,"y":0.54,"voice":"female"},{"word":"a drain cover","x":0.22,"y":0.645,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","parking","in","a","tight","space."],"answerVoice":"female",
"notes":"While the woman sits in the car her box (head + arm in the window) and the car box are split horizontally: the car box starts just below her arm, so the car's window/roof strip above is not tappable for the car. From 7.5 s, when she gets out, the car box covers only the rear part right of her. Old man with the newspaper at the left edge 7.0-9.5 s (very narrow at 7.0/7.5/9.0 to stay clear of the woman); off at 10.0 s where the woman covers him. Car may be reversing rather than driving forward into the gap, so the phrase avoids the direction."}
json.dump(c,open('content/5135.json','w'),indent=1)
