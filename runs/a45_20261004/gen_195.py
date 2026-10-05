import json
def keys(d): return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
T=[i*0.5 for i in range(21)]
W={0.0:(.46,.17,.54,.83),0.5:(.40,.14,.60,.86),1.0:(.45,.17,.55,.83),1.5:(.23,.20,.77,.80),2.0:(.19,.17,.81,.83),2.5:(.17,.17,.83,.83),
3.0:(.38,.22,.62,.78),3.5:(.57,.28,.43,.72),4.0:(.50,.24,.50,.76),4.5:(.37,.12,.63,.88),5.0:(.29,.07,.71,.93),5.5:(.25,.07,.75,.93),
6.0:(0,0,1,1),6.5:(0,0,1,1),7.0:(0,.02,1,.98),7.5:(0,.06,1,.94),8.0:(0,.08,1,.92),8.5:(0,.10,1,.90),9.0:(0,.12,1,.88),
9.5:(0,.10,1,.72),10.0:(.08,.15,.90,.44)}
M={0.0:(.03,.16,.42,.26),0.5:(.03,.15,.36,.27),1.0:(0,.17,.44,.28),1.5:(0,.02,.22,.50),2.0:(0,0,.18,.60),2.5:(0,0,.16,.62),
3.0:(0,0,.36,.62),3.5:(0,0,.56,.58),4.0:(0,0,.49,.47),4.5:(0,0,.36,.42),5.0:(0,.20,.28,.66),5.5:(0,.27,.24,.20)}
C={9.5:(.15,.83,.75,.17),10.0:(.02,.60,.74,.40)}
c={"mediaId":195,"level":"A","keyWord":"coughing","defaultVoice":"female",
"taps":[tap("to cough into her hand","the woman","female",W),tap("to bring hot tea","the man","male",M),tap("to walk on the blanket","the cat","female",C)],
"stillS":10.0,
"nouns":[noun("plants",.36,.14,"female"),noun("a cup",.50,.55,"female"),noun("a blanket",.78,.68,"female"),noun("a cat",.25,.80,"female")],
"question":"What is the sick woman doing?","answer":["She","is","coughing","into","her","hand."],"answerVoice":"female",
"notes":"The woman coughs into her hand at 1.5-2.0 only (later she drinks). The man sits in the background at 0.0-1.0, then leans over her: boxes split by x so her head is always in her box; parts of her blanket on the left and his hand at the cup fall outside or into his box at 3.0-5.5. 5.0-5.5 only his arm/hand is in the picture. The cat is clear only at 9.5-10.0 (9.0 shows just two ear tips at the bottom edge: off); it stands on the blanket on her legs, 'to walk on the blanket' is the weakest phrase. 'sick' in the question is read from the picture (coughing, blankets)."}
json.dump(c,open('content/195.json','w'),indent=1)
