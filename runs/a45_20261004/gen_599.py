import json
times=[i*0.5 for i in range(31)]
A={0.0:(.11,.24,.50,.67),0.5:(.23,.31,.57,.63),1.0:(.31,.31,.59,.65),1.5:(.15,.30,.47,.61),2.0:(.24,.29,.49,.57),2.5:(.04,.27,.50,.65),
3.0:(.16,.36,.35,.64),3.5:(.50,.29,.86,.62),4.0:(.51,.29,.89,.65),4.5:(.31,.28,.89,.72),5.0:(.24,.30,.54,.65),5.5:(.11,.29,.46,.67),
6.0:(.05,.29,.40,.62),6.5:(.37,.30,.65,.45),9.5:(.14,.29,.50,.67),10.0:(.26,.33,.54,.64),10.5:(.13,.29,.50,.67),11.0:(.12,.32,.45,.58),11.5:(.49,.30,.79,.60)}
D={0.0:(.68,.30,1.0,.65),0.5:(.66,.28,.94,.63),1.0:(.60,.29,.95,.63),1.5:(.48,.27,.79,.63),2.0:(.50,.29,.74,.60),2.5:(.56,.24,.86,.64),
3.0:(.36,.29,.64,.67),3.5:(.16,.28,.50,.63),4.0:(.13,.34,.50,.63),5.0:(.55,.27,.86,.65),5.5:(.53,.27,.94,.65),
6.0:(.41,.28,.87,.65),6.5:(.01,.46,.60,.63),9.5:(.68,.29,1.0,.66),10.0:(.55,.28,.79,.64),10.5:(.51,.31,.89,.65),11.0:(.46,.31,.76,.67),11.5:(.08,.38,.48,.66)}
T={7.0:(.10,.24,.45,.66),7.5:(.16,.29,.50,.64),8.0:(.26,.28,.60,.66),8.5:(.47,.28,.87,.64),9.0:(.55,.32,.87,.62),
12.0:(.05,.25,.41,.67),12.5:(.13,.26,.46,.64),13.0:(.21,.31,.62,.67),13.5:(.12,.31,.52,.65),14.0:(.44,.33,.68,.59),14.5:(.54,.33,.92,.58),15.0:(.75,.33,1.0,.55)}
def keys(d):
    out=[]
    for t in times:
        if t in d:
            a,b,c,e=d[t]; out.append({"t":t,"x":a,"y":b,"w":round(c-a,2),"h":round(e-b,2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":599,"level":"B","keyWord":"rapid","defaultVoice":"male",
"taps":[
 {"phrase":"to dribble a colourful ball","target":"the man in orange boots","voice":"male","keys":keys(A)},
 {"phrase":"to defend in white boots","target":"the man in white boots","voice":"male","keys":keys(D)},
 {"phrase":"to control a white ball","target":"the man in turquoise shorts","voice":"male","keys":keys(T)}],
"stillS":5.5,
"nouns":[{"word":"a goal","x":.86,"y":.36,"voice":"male"},{"word":"a football","x":.26,"y":.58,"voice":"male"},{"word":"turf","x":.55,"y":.85,"voice":"male"},{"word":"a roof","x":.35,"y":.08,"voice":"male"}],
"question":"What are the two men doing?",
"answer":["They","are","competing","for","the","ball."],
"answerVoice":"male",
"notes":"Quick-cut compilation, indoor shots (man in black with orange boots vs navy defender in white boots) and outdoor shots (attacker in blue top + turquoise shorts vs defender in black shorts, not a target). Targets are OFF in the other location's shots. Frames 3.0 and 11.0: the two indoor players overlap, boxes split roughly. 4.5: defender almost hidden behind the attacker -> off. Key word 'rapid' is an adjective, not used in the answer."}
json.dump(c,open('content/599.json','w'),indent=1,ensure_ascii=False)
