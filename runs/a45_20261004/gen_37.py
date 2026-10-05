import json
T=[i*0.5 for i in range(11)]
def b(t,v):
    if v is None: return {"t":t,"off":True}
    x0,y0,x1,y1=v; return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
R={0.0:(0,0,.55,.78),0.5:(.08,.03,.58,.75),1.0:(.06,.15,.70,.76),1.5:(.08,.27,.56,.83),2.0:(.14,.33,.54,.80),2.5:(.20,.50,.60,.84),
3.0:(.25,.61,.56,.90),3.5:(.41,.47,.68,.85),4.0:(.51,.39,.73,.75),4.5:(.52,.35,.78,.74),5.0:(.52,.35,.79,.85)}
B={0.0:(.56,.32,.76,.54),0.5:(.59,.32,.77,.54),1.5:(.57,.34,.75,.54),2.0:(.55,.35,.73,.55),2.5:(.38,.35,.60,.49),
3.0:(.22,.46,.47,.60),3.5:(.21,.47,.40,.87),4.0:(.33,.41,.50,.74),4.5:(.34,.37,.51,.74),5.0:(.33,.36,.51,.85)}
F={0.0:(.77,.32,.95,.46),0.5:(.78,.31,.96,.45),1.0:(.75,.30,.93,.45),1.5:(.76,.29,.94,.44),2.0:(.74,.27,.92,.42),2.5:(.66,.25,.88,.45),
3.0:(.57,.21,.80,.55),3.5:(.40,.12,.76,.46),4.0:(.40,.12,.74,.38),4.5:(.38,.12,.74,.34),5.0:(.40,.12,.74,.34)}
c={"mediaId":37,"level":"B","keyWord":"advance","defaultVoice":"male",
"taps":[{"phrase":"to flutter on the summit","target":"the flag","voice":"male","keys":[b(t,F[t]) for t in T]},
{"phrase":"to grasp the flagpole","target":"the climber in red","voice":"male","keys":[b(t,R[t]) for t in T]},
{"phrase":"to have a bushy beard","target":"the climber in blue","voice":"male","keys":[b(t,B.get(t)) for t in T]}],
"stillS":5.0,
"nouns":[{"word":"a flag","x":.55,"y":.20,"voice":"male"},{"word":"peaks","x":.18,"y":.34,"voice":"male"},
{"word":"goggles","x":.63,"y":.44,"voice":"male"},{"word":"a rope","x":.35,"y":.83,"voice":"male"}],
"question":"What are the three climbers doing?",
"answer":["They","are","advancing","towards","the","flag","on","the","summit."],
"answerVoice":"male",
"notes":"The three climbers overlap a lot; only red and blue are targets, the yellow climber is not (she sometimes lies inside the red box). Blue is almost fully hidden behind red at 1.0 s (off). The climber in red grasps the flagpole only at 3.5-4.0 s; gender of the climber in red is unclear, so default voice. The blue climber's beard is visible only from 3.0 s. Two ropes are visible at 5.0 s; the 'a rope' pill sits on the left one. Answer describes the main action (they reach the top in the last second)."}
json.dump(c,open('content/37.json','w'),indent=1,ensure_ascii=False)
