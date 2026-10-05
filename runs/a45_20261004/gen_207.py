import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
W={0.0:None,0.5:None,1.0:None,1.5:None,2.0:None,2.5:None,3.0:None,3.5:None,
4.0:(0,0,.51,1),4.5:(0,0,.60,1),5.0:(0,0,.56,1),5.5:(0,.03,.57,.97),6.0:(0,.03,.52,.97),6.5:(0,.03,.46,.97),7.0:(0,.08,.40,.92),7.5:(0,.10,.39,.90),
8.0:(0,.08,.38,.92),8.5:(0,.05,.42,.95),9.0:(0,.06,.46,.94),9.5:(0,.05,.50,.95),10.0:(0,.03,.47,.97)}
M={0.0:None,0.5:None,1.0:(.72,.08,.28,.70),1.5:(.70,.10,.30,.68),2.0:(.62,.15,.38,.58),2.5:(.50,0,.50,.55),3.0:(.52,0,.48,.60),3.5:(.50,0,.50,.60),
4.0:(.67,.26,.33,.31),4.5:(.70,.34,.30,.28),5.0:(.76,.15,.24,.78),5.5:(.76,.10,.24,.70),6.0:(.70,.06,.30,.64),6.5:(.80,.04,.20,.68),7.0:(.74,.03,.26,.84),7.5:(.75,.05,.25,.80),
8.0:(.75,.05,.25,.67),8.5:(.74,.06,.26,.62),9.0:(.70,.05,.30,.78),9.5:(.75,.03,.25,.72),10.0:(.78,.03,.22,.67)}
C={0.0:None,0.5:None,1.0:None,1.5:None,2.0:None,2.5:None,3.0:None,3.5:None,
4.0:(.51,.11,.38,.15),4.5:(.60,.19,.31,.15),5.0:(.56,.26,.20,.14),5.5:(.57,.28,.19,.16),6.0:(.52,.27,.18,.15),6.5:(.46,.28,.34,.14),7.0:(.40,.28,.34,.17),7.5:(.39,.31,.36,.16),
8.0:(.38,.29,.37,.14),8.5:(.42,.31,.32,.15),9.0:(.46,.30,.24,.14),9.5:(.50,.29,.25,.15),10.0:(.47,.26,.18,.14)}
c={"mediaId":207,"level":"A","keyWord":"cup","defaultVoice":"female",
"taps":[tap("to wear a green earring","the woman","female",W),tap("to wear glasses","the man","male",M),tap("to lie on a wall","the orange cat","female",C)],
"stillS":8.0,
"nouns":[noun("a cat",.55,.36,"female"),noun("a cup",.80,.45,"female"),noun("flowers",.20,.53,"female"),noun("a teapot",.25,.75,"female")],
"question":"What is the woman doing?","answer":["She","is","drinking","tea","from","a","cup."],"answerVoice":"female",
"notes":"Both people hold a cup and drink, so the woman and the man get a state phrase (earring / glasses) - weak spot. 0-3.5: only a hand with the cup and the pouring; the woman is set off there (hand not surely hers), the man is a blurred blue shirt at 1.0-2.0 and an arm at 2.5-3.5 (no glasses seen before 5.0). A white cat lies blurred in the background at 1.0-2.0: not the orange cat, off. The orange cat is on the wall outside from 4.0 (standing at 4.0-6.0, lying with a paw hanging down from 6.5), always small and blurred and right next to the man's hand: boxes are tight and split; at 4.0-5.0 the man's box is only his hand/arm, his head is at the frame edge. The woman's box ends where the cat's begins, so her cup hand is sometimes cut. 'a cup' sits on the man's cup; the woman's cup has no noun (too close to the flowers)."}
json.dump(c,open('content/207.json','w'),indent=1)
