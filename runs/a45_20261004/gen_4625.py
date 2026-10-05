import json
times=[i*0.5 for i in range(25)]
M={3.0:(0,.28,.19,.72),3.5:(.02,.25,.41,.75),4.0:(.15,.25,.42,.72),4.5:(0,.10,.80,.90),5.0:(0,.11,.78,.89),5.5:(0,.14,.72,.86),6.0:(.52,.15,.48,.63)}
N={2.5:(0,.27,.21,.47),3.0:(.19,.29,.22,.60),3.5:(.43,.30,.19,.60),4.0:(.57,.31,.18,.48),6.0:(0,.26,.52,.74),6.5:(0,.24,.80,.76),
7.0:(.17,.37,.60,.63),7.5:(.22,.33,.63,.67),8.0:(.50,.25,.50,.75)}
R={8.0:(.22,.27,.28,.60),8.5:(.19,.25,.46,.72),9.0:(.09,.25,.58,.75),9.5:(.03,.19,.74,.81),10.0:(.01,.06,.78,.94),10.5:(0,.11,.83,.89),
11.0:(0,.11,1,.89),11.5:(0,.12,1,.88),12.0:(0,.11,1,.89)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4625,"level":"B","keyWord":"vote","defaultVoice":"male",
"taps":[
 {"phrase":"to lean on a cane","target":"the elderly man","voice":"male","keys":keys(M)},
 {"phrase":"to wear blue scrubs","target":"the nurse","voice":"female","keys":keys(N)},
 {"phrase":"to punch the air","target":"the woman in yellow","voice":"female","keys":keys(R)}],
"stillS":10.0,
"nouns":[{"word":"a ballot box","x":.62,"y":.83,"voice":"male"},{"word":"a raincoat","x":.33,"y":.56,"voice":"male"},
 {"word":"a rosette","x":.90,"y":.44,"voice":"male"},{"word":"windows","x":.72,"y":.12,"voice":"male"}],
"question":"What is the woman in yellow doing?",
"answer":["She","is","punching","the","air","after","voting."],
"answerVoice":"female",
"notes":"Everyone posts a ballot, so no phrase about casting a ballot. Hard hat not used: a second worker in a yellow hard hat stands further back in the queue. Nurse phrase is a state (the only person in scrubs). Nurse and neighbours overlap in the queue shots (3.0-4.0, 6.0, 8.0): boxes split along the line between them. First voter (dark cardigan, 0.5-2.0) is no target. defaultVoice male: mixed group, odd id."}
json.dump(c,open("content/4625.json","w"),indent=1,ensure_ascii=False)
