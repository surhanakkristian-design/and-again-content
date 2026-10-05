import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
M={0.0:(0,0,1,.70),0.5:(0,0,1,.71),1.0:(0,0,1,.73),1.5:(0,0,1,1),2.0:(0,0,1,1),2.5:(0,0,1,.60),3.0:(0,0,1,.70),3.5:(0,0,1,.65),4.0:(0,0,1,.62),4.5:(0,0,1,.60),5.0:(0,0,1,.62),5.5:(0,0,1,.68),
6.0:None,6.5:None,7.0:None,7.5:None,8.0:None,8.5:None,9.0:None,9.5:None,10.0:None}
W={0.0:None,0.5:None,1.0:None,1.5:None,2.0:None,2.5:None,3.0:None,3.5:None,4.0:None,4.5:None,5.0:None,5.5:None,
6.0:(.30,.05,.70,.90),6.5:(.33,.10,.67,.90),7.0:(.33,.12,.67,.88),7.5:(.31,.10,.69,.90),8.0:(.33,.08,.67,.92),8.5:(.27,.03,.73,.97),9.0:None,9.5:(.20,.17,.80,.83),10.0:(.21,.10,.79,.90)}
D={0.0:(.80,.70,.20,.16),0.5:(.80,.71,.20,.18),1.0:(.80,.73,.20,.22),1.5:None,2.0:None,2.5:None,3.0:None,3.5:None,4.0:None,4.5:None,5.0:None,5.5:None,
6.0:(.10,.40,.20,.14),6.5:(.10,.48,.23,.14),7.0:(.10,.49,.23,.14),7.5:(.09,.49,.22,.14),8.0:(.09,.49,.24,.14),8.5:(.07,.48,.20,.14),9.0:None,9.5:(0,.44,.20,.22),10.0:(0,.45,.21,.18)}
c={"mediaId":206,"level":"A","keyWord":"cucumber","defaultVoice":"male",
"taps":[tap("to cut a cucumber","the man","male",M),tap("to eat some cucumber","the woman","female",W),tap("to look over the table","the dog","male",D)],
"stillS":0.0,
"nouns":[noun("a window",.22,.12,"male"),noun("a cucumber",.50,.50,"male"),noun("a shirt",.45,.68,"male"),noun("a dog",.86,.77,"male")],
"question":"What is the man doing?","answer":["He","is","cutting","a","cucumber."],"answerVoice":"male",
"notes":"Many cuts. Man: face shots 0-2.0, then only torso and hands (peeling 2.5-4.0, cutting 4.5-5.0, picking a slice 5.5); the lower part of his shirt is left out of his box. At 6.0-6.5 two hands (probably his) hold slices on the woman's eyes: he is set off there and the hands lie in the woman's box. 9.0 is a salad bowl with an unidentifiable torso: all off. The woman eats the slice only at 9.5-10. The dog peeks over the worktop behind the man (0-1.5) and behind the woman (6.0-10); the woman's box starts right of the dog, so her left shoulder is cut. 'to look over the table' is the weakest phrase (at 9.5-10 no table edge is seen)."}
json.dump(c,open('content/206.json','w'),indent=1)
