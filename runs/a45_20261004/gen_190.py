import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
N=None

Wm={0.0:N,0.5:N,1.0:(.32,0,.68,.42),1.5:(0,0,.46,.66),2.0:(0,0,.50,.75),2.5:(0,0,.53,.74),3.0:(0,.02,.54,.85),3.5:(0,0,.52,.62),4.0:(0,0,.48,.58),4.5:(0,0,.50,.62),5.0:(0,0,.50,.70),5.5:(0,.02,.45,.76),
6.0:(0,.20,.32,.52),6.5:(0,.21,.32,.52),7.0:(0,.22,.31,.60),7.5:(0,.22,.31,.60),8.0:(0,.22,.30,.55),8.5:(0,.23,.31,.54),9.0:(0,.24,.30,.64),9.5:(0,.24,.30,.64),10.0:(0,.24,.29,.56)}
M={0.0:N,0.5:N,1.0:N,1.5:N,2.0:N,2.5:N,3.0:N,3.5:N,4.0:(.67,.12,.33,.30),4.5:(.58,.32,.42,.14),5.0:(.55,.41,.45,.14),5.5:(.46,.49,.54,.14),
6.0:(.64,.20,.36,.53),6.5:(.65,.21,.35,.52),7.0:(.64,.22,.36,.62),7.5:(.65,.22,.35,.62),8.0:(.64,.22,.36,.60),8.5:(.64,.23,.36,.52),9.0:(.63,.25,.37,.63),9.5:(.63,.25,.37,.63),10.0:(.62,.25,.38,.54)}
C={0.0:N,0.5:N,1.0:N,1.5:(.46,.23,.50,.19),2.0:(.51,.29,.47,.19),2.5:(.54,.33,.46,.18),3.0:(.55,.45,.41,.18),3.5:(.53,.23,.42,.19),4.0:(.48,.17,.18,.16),4.5:(.50,.17,.38,.15),5.0:(.51,.27,.36,.14),5.5:(.46,.35,.40,.14),
6.0:(.32,.39,.32,.15),6.5:(.32,.40,.33,.15),7.0:(.31,.41,.33,.15),7.5:(.32,.41,.33,.15),8.0:(.30,.40,.34,.15),8.5:(.31,.41,.33,.15),9.0:(.30,.44,.33,.14),9.5:(.30,.44,.33,.14),10.0:(.29,.44,.33,.14)}
c={"mediaId":190,"level":"A","keyWord":"cookie","defaultVoice":"female",
"taps":[tap("to eat a big cookie","the woman","female",Wm),tap("to hold a spoon","the man","male",M),tap("to lie by the window","the cat","female",C)],
"stillS":8.0,
"nouns":[noun("a window",.45,.18,"female"),noun("a cat",.47,.49,"female"),noun("cookies",.33,.65,"female"),noun("a table",.55,.90,"female")],
"question":"What is the woman eating?","answer":["She","is","eating","a","big","cookie."],"answerVoice":"female",
"notes":"0.0/0.5: only oven gloves, woman off; 1.0 her arm and side. The man is fully visible from 6.0; at 4.0-5.5 only his hand/arm in a grey sweater reaches in from the right (thin boxes, split from the cat behind it). He holds the spoon at 8.5-10.0 (at 6.0 he dips a cookie in his cup, he never eats). Key word as the plural 'cookies' on the tray, so the single cookie in her hand is not a second slot. Two cups on the table, so no 'a cup' noun."}
json.dump(c,open('content/190.json','w'),indent=1)
