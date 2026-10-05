import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
N=None

M={0.0:N,0.5:N,1.0:N,1.5:(0,0,1,.12),2.0:(0,0,1,.31),2.5:(0,0,1,.33),3.0:(.15,0,.85,.33),3.5:(.05,0,.95,.34),4.0:(0,.05,1,.28),4.5:(.70,0,.30,.55),5.0:(.63,.15,.37,.63),5.5:(.60,.08,.40,.84),
6.0:(.62,0,.38,.65),6.5:(.67,0,.33,.70),7.0:(.56,0,.44,.75),7.5:(.50,0,.50,.68),8.0:(.55,.22,.45,.70),8.5:(.55,.25,.45,.65),9.0:(.50,.02,.50,.80),9.5:(.53,.06,.47,.80),10.0:(.52,.08,.48,.64)}
S={0.0:(.28,0,.33,.60),0.5:(.32,0,.32,.61),1.0:(.33,0,.30,.62),1.5:(.22,.12,.50,.57),2.0:(.30,.31,.40,.33),2.5:(.30,.33,.42,.30),3.0:(.28,.33,.48,.40),3.5:(.38,.34,.24,.24),4.0:(.32,.33,.24,.24),4.5:(.28,.26,.42,.31),5.0:(.30,.30,.33,.33),5.5:(.35,.18,.25,.45),
6.0:(.34,.04,.28,.42),6.5:(.45,.20,.22,.31),7.0:(.30,.28,.26,.32),7.5:(0,.68,.42,.16),8.0:N,8.5:N,9.0:N,9.5:N,10.0:N}
Wm={t:N for t in M}; Wm.update({9.0:(0,.10,.42,.78),9.5:(0,.14,.42,.72),10.0:(0,.18,.44,.55)})
c={"mediaId":191,"level":"B","keyWord":"corkscrew","defaultVoice":"male",
"taps":[tap("to sniff the cork","the man","male",M),tap("to twist into the cork","the corkscrew","male",S),tap("to wear a long-sleeved shirt","the woman","female",Wm)],
"stillS":5.0,
"nouns":[noun("a corkscrew",.42,.37,"male"),noun("a cork",.44,.53,"male"),noun("a bottle",.42,.72,"male"),noun("a saucepan",.78,.84,"male")],
"question":"How is the man opening the bottle?","answer":["He","is","opening","the","bottle","with","a","corkscrew."],"answerVoice":"male",
"notes":"Close-ups until 5.5: the man is only his hands on the corkscrew (off at 0.0-1.0 where they are a blur behind the spiral); his box and the corkscrew box are split (hand above / beside the tool), at 3.5-4.0 the lever inside his fist falls in his box. He sniffs the cork at 6.5-7.0. The woman is clearly visible only at 9.0-10.0; before that just a blurred sleeve / hand at the left edge (set off). Her phrase is a state because both of them hold a glass, toast and sip; the man wears a short-sleeved T-shirt. Corkscrew off from 8.0 (a dark object on the counter at 9.0-10.0 may be it, not boxed). Still 5.0: the cork is half out under the corkscrew, pills 0.16 apart; the bottle pill sits on the bottle neck below it."}
json.dump(c,open('content/191.json','w'),indent=1)
