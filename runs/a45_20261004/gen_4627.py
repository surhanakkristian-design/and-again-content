import json
times=[i*0.5 for i in range(25)]
M={0.0:(.52,.27,.36,.53),0.5:(.50,.26,.38,.54),1.0:(.48,.28,.40,.65),1.5:(.46,.25,.40,.69),2.0:(.42,.25,.44,.56),
2.5:(.53,.31,.33,.42),3.0:(.55,.33,.33,.41),3.5:(.51,.32,.37,.44),4.0:(.47,.31,.43,.49),4.5:(.45,.32,.43,.50),5.0:(.49,.33,.41,.51),5.5:(.43,.32,.43,.50),
6.0:(.67,.44,.26,.33),6.5:(.66,.48,.25,.28),7.0:(.68,.50,.22,.26),7.5:(.66,.51,.21,.24),8.0:(.64,.53,.21,.21),8.5:(.61,.54,.24,.19),
9.0:(.60,.55,.21,.16),9.5:(.60,.55,.20,.16),10.0:(.60,.55,.20,.16),10.5:(.60,.55,.20,.16),11.0:(.59,.55,.20,.16),11.5:(.59,.55,.20,.16),12.0:(.58,.55,.20,.15)}
T={2.5:(0,.08,.53,.75),3.0:(0,.15,.55,.75),3.5:(0,.10,.51,.80),4.0:(0,.08,.47,.78),4.5:(0,.08,.45,.78),5.0:(0,.10,.49,.80),5.5:(0,.10,.43,.80)}
S={6.0:(0,0,1,.44),6.5:(0,0,1,.48),7.0:(0,0,1,.50),7.5:(0,.02,1,.49),8.0:(.02,.03,.98,.50),8.5:(.05,.05,.95,.49),9.0:(.08,.08,.92,.47),
9.5:(.10,.09,.88,.46),10.0:(.12,.10,.86,.45),10.5:(.15,.11,.80,.44),11.0:(.16,.12,.78,.43),11.5:(.18,.14,.76,.41),12.0:(.20,.16,.74,.39)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4627,"level":"A","keyWord":"leave","defaultVoice":"male",
"taps":[
 {"phrase":"to wave goodbye","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to leave the station","target":"the train","voice":"male","keys":keys(T)},
 {"phrase":"to sail on the sea","target":"the ship","voice":"male","keys":keys(S)}],
"stillS":10.0,
"nouns":[{"word":"a ship","x":.52,"y":.35,"voice":"male"},{"word":"the sea","x":.25,"y":.82,"voice":"male"},
 {"word":"the sky","x":.50,"y":.07,"voice":"male"},{"word":"a man","x":.70,"y":.63,"voice":"male"}],
"question":"What is the ship doing?",
"answer":["The","ship","is","leaving","the","port."],
"answerVoice":"male",
"notes":"First vehicle (0-2.0 s) looks like a bus although the description says tram: not used as a target. Train and ship boxes are cut where the man stands in front of them (train box ends at the man's left side, ship box ends above his raised hand), so the far end of the train / the bottom of the hull is outside the box. Man is small in the last shot (box 0.20 x 0.16). 'to wave goodbye' is 3 words incl. 'to'."}
json.dump(c,open("content/4627.json","w"),indent=1,ensure_ascii=False)
