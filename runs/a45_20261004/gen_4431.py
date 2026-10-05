import json
T=[i/2 for i in range(19)]
B={0.0:(.46,.16,.35,.49),0.5:(.29,.12,.40,.54),1.0:(.37,.12,.48,.72),1.5:(.44,.10,.50,.84),2.0:(.07,.11,.72,.86),2.5:(0,.15,1,.85),
3.0:(.02,.17,.90,.83),3.5:(.03,.17,.97,.83),4.0:(.09,.14,.86,.86),4.5:(.13,.08,.87,.75),5.0:(.44,.16,.56,.84),5.5:(.50,.17,.50,.83),
6.0:(0,.10,.80,.90),6.5:(.17,.07,.45,.60),7.0:(0,.15,.50,.50),7.5:(0,.22,.47,.41),8.0:(.12,.25,.25,.37),8.5:(.31,.22,.24,.24),9.0:(.22,.25,.27,.27)}
D={4.5:(0,.83,.42,.17),5.0:(0,.57,.44,.43),5.5:(0,.38,.50,.52)}
M={8.0:(0,.27,.12,.35),8.5:(.13,.24,.18,.39),9.0:(.49,.26,.18,.37)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":4431,"level":"B","keyWord":"score","defaultVoice":"male",
"taps":[{"phrase":"to score a goal","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to approach the boy","target":"the dog","voice":"male","keys":keys(D)},
{"phrase":"to lift the boy up","target":"the man","voice":"male","keys":keys(M)}],
"stillS":7.5,
"nouns":[{"word":"clouds","x":.60,"y":.15,"voice":"male"},{"word":"a goal","x":.60,"y":.43,"voice":"male"},
{"word":"a football","x":.61,"y":.56,"voice":"male"},{"word":"a boy","x":.14,"y":.38,"voice":"male"}],
"question":"What is the boy doing?","answer":["He","is","scoring","a","goal","in","the","park."],"answerVoice":"male",
"notes":"The packet says the boy hugs 'another boy' at the end; the frames show a grown man (white t-shirt, denim shorts) who lifts the boy, so the third target is 'the man' (8.0-9.0 s only). He and the boy are intertwined there: at 8.0 s the man is only a strip at the left edge behind the boy (box 0.12 wide), at 8.5 / 9.0 s the boxes are split on a vertical line between the two heads, so the man's box is narrow (0.18) and part of his legs is unowned. The dog is visible only 4.5-5.5 s (at 4.5 s just its back in the bottom left corner; at 6.0 s only a sliver, off). 'a goal' pill on the crossbar, 'a football' pill on the ball inside the goal: 0.13 apart in y, close. The two shirts on the grass are left out (two alike things)."}
json.dump(c,open('content/4431.json','w'),indent=1)
