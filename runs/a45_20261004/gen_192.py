import json
def keys(d): return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
T=[i*0.5 for i in range(21)]
W={0.0:(0,.22,.78,.78),0.5:(0,.43,.82,.57),1.0:(0,.63,.80,.37),1.5:(0,.52,.27,.48),2.0:(0,.45,.27,.55),2.5:(0,.45,.27,.55),
3.0:(0,.17,.38,.53),3.5:(0,.17,.42,.53),4.0:(0,.19,.42,.48),4.5:(0,.18,.47,.47),5.0:(0,.20,.48,.47),5.5:(0,.17,.50,.50),
6.5:(0,.53,.18,.30),7.0:(0,.53,.18,.42),7.5:(0,.53,.22,.47),8.0:(0,.51,.43,.49),8.5:(.07,.47,.43,.53),9.0:(.08,.52,.40,.48),9.5:(.10,.52,.39,.48),10.0:(.12,.53,.37,.47)}
M={3.0:(.52,.20,.48,.50),3.5:(.50,.20,.50,.50),4.0:(.50,.20,.50,.47),4.5:(.55,.19,.45,.46),5.0:(.52,.17,.48,.50),5.5:(.50,.17,.50,.50),
7.5:(.78,.52,.22,.48),8.0:(.57,.49,.43,.51),8.5:(.50,.47,.43,.53),9.0:(.50,.51,.42,.49),9.5:(.51,.51,.43,.49),10.0:(.50,.52,.41,.48)}
B={1.5:(.27,.38,.40,.62),2.0:(.27,.37,.37,.63),2.5:(.27,.37,.38,.63),3.0:(.30,.70,.42,.22),3.5:(.30,.71,.44,.22),4.0:(.33,.67,.36,.20),
4.5:(.30,.65,.44,.21),5.0:(.30,.67,.42,.21),5.5:(.30,.67,.44,.21)}
c={"mediaId":192,"level":"A","keyWord":"corner","defaultVoice":"female",
"taps":[tap("to fit into the corner","the board","female",B),tap("to wear orange clothes","the woman","female",W),tap("to wear glasses","the man","male",M)],
"stillS":10.0,
"nouns":[noun("the sky",.20,.06,"female"),noun("a corner",.50,.32,"female"),noun("a woman",.30,.72,"female"),noun("a man",.70,.82,"male")],
"question":"Where are they putting the board?","answer":["They","are","putting","it","in","the","corner."],"answerVoice":"female",
"notes":"Both people do the same actions (touch the pillar, hold a board, high five), so the two person phrases are states. 0.0-2.5 only the woman's hands and orange sleeves are in the picture: boxed as the woman. 1.5-2.5 her hands lie on the board: split at x 0.27. 3.0-5.5 the people's boxes end above the board box, so their legs beside the board are outside. Board = one board at 1.5-2.5, the two triangle boards at 3.0-5.5. 6.0 only a sliver of orange at the left edge: off. Corner pill sits on the line where the two walls meet."}
json.dump(c,open('content/192.json','w'),indent=1)
