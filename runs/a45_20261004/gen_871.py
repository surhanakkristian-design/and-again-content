import json
T=[i*0.5 for i in range(21)]
def bx(t,x0,y0,x1,y1): return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
man={0.0:(0,0,.62,.72),0.5:(.05,.33,1,.90),1.0:(0,0,.58,1),1.5:(.03,0,1,.98),2.0:(.20,0,1,.70),2.5:(.08,.07,.97,.79),
3.0:(.07,.18,.67,.90),3.5:(.37,.16,.82,.84),4.0:(.18,.18,.77,.70),4.5:(0,.32,.63,.78),5.0:(.16,.34,.79,.91),5.5:(.04,.33,.61,.88),
6.0:(.32,.39,.80,.84),6.5:(.36,.45,.84,.85),7.0:(.48,.47,1,1),7.5:(.58,.59,1,1),8.0:(.37,.44,.93,.81),8.5:(.50,.34,1,.92),
9.0:(.50,.24,.98,.93),9.5:(.49,.26,.97,.80),10.0:(.74,.23,1,.66)}
ball={0.5:(.08,.05,.50,.33),1.0:(.58,.07,.95,.36),3.0:(.67,.54,.85,.68),3.5:(.82,.50,1,.64),4.0:(.77,.52,.97,.67),4.5:(.63,.53,.84,.68),
5.0:(.79,.46,.99,.61),5.5:(.61,.50,.79,.64),6.5:(.55,.31,.73,.45),7.0:(.46,.08,.64,.22),7.5:(.25,.25,.46,.40),8.0:(.38,.81,.62,.97)}
def keys(d): return [bx(t,*d[t]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":871,"level":"A","keyWord":"wheelchair","defaultVoice":"male",
"taps":[
{"phrase":"to throw the ball","target":"the man with number 12","voice":"male","keys":keys(man)},
{"phrase":"to fall into the basket","target":"the ball","voice":"male","keys":keys(ball)},
{"phrase":"to raise a fist","target":"the man with number 12","voice":"male","keys":keys(man)}],
"stillS":6.5,
"nouns":[{"word":"a basket","x":0.36,"y":0.31,"voice":"male"},{"word":"a ball","x":0.65,"y":0.41,"voice":"male"},
{"word":"a door","x":0.16,"y":0.56,"voice":"male"},{"word":"a wheelchair","x":0.60,"y":0.72,"voice":"male"}],
"question":"What is number 12 doing?",
"answer":["He","is","throwing","the","ball","into","the","basket."],
"answerVoice":"male",
"notes":"Only two targets (number 12 twice, the ball): the referee is visible for only 1.5 s and the second player only in the last 2 s, both too short / not unique for a phrase. The man's box includes his wheelchair. Ball and man overlap while he holds / dribbles the ball: boxes split along the edge of the ball, so the man's box loses his hands (and at 0.5 s his chest, at 8.0 s the bottom of his wheels). Ball off at 6.0 s (almost hidden behind his body) and at 3.5 s it is half out of the frame. 'basket' used for the hoop (A level). The question names 'number 12' because a referee and a second player also appear; 'What is the man with the ball doing?' would be 8 words."}
json.dump(c,open("content/871.json","w"),indent=1)
