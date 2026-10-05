import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
out={}
# ---- 97
G={0.0:(0,.19,.65,.36),0.5:(0,.19,.65,.36),1.0:(0,.22,.70,.34),1.5:(0,0,1,.22),2.0:(0,0,1,.20),2.5:(0,0,1,.20),3.0:(0,0,1,.32),3.5:(0,0,1,.42),
4.0:(0,0,.80,.47),4.5:(0,.10,1,.44),5.0:(0,.17,.97,.38),5.5:(0,.12,.90,.30),6.0:(0,.12,.92,.30),6.5:(0,.15,1,.38),7.0:(0,.18,.66,.37)}
W={0.0:(.50,.56,.50,.21),0.5:(.50,.56,.50,.21),1.0:(.50,.57,.50,.21),1.5:(0,.24,1,.76),2.0:(0,.21,1,.79),2.5:(0,.21,1,.79),3.0:(0,.33,1,.67),3.5:(0,.43,1,.50),
4.0:(.26,.48,.74,.31),4.5:(.50,.55,.50,.22),5.0:(.50,.56,.50,.22),5.5:(.28,.43,.72,.30),6.0:(.25,.43,.65,.26),6.5:(.50,.54,.50,.22),7.0:(.50,.56,.50,.21)}
F={0.0:(.50,.77,.47,.15),0.5:(.50,.77,.47,.15),1.0:(.48,.78,.47,.15),1.5:None,2.0:None,2.5:None,3.0:None,3.5:None,
4.0:(.30,.79,.70,.21),4.5:(.50,.77,.45,.15),5.0:(.50,.78,.47,.15),5.5:(.55,.74,.42,.18),6.0:(.52,.70,.44,.18),6.5:(.50,.76,.47,.16),7.0:(.48,.77,.47,.15)}
out[97]={"mediaId":97,"level":"A","keyWord":"boil","defaultVoice":"female",
"taps":[tap("to pour hot water","the girl","female",G),tap("to boil in the pot","the water","female",W),tap("to burn under the pot","the fire","female",F)],
"stillS":0.0,
"nouns":[noun("a girl",.40,.33,"female"),noun("a pot",.75,.64,"female"),noun("a fire",.72,.85,"female"),noun("a teapot",.20,.78,"female")],
"question":"What is the girl doing?","answer":["She","is","boiling","water","in","a","pot."],"answerVoice":"female",
"notes":"Target 'the water' = the water in the copper pot; its box is the whole pot (plus the poured stream at 5.5-6.0). Girl and pot overlap in the picture (her hands are on / in front of the pot): the girl's box is head and upper body above the pot rim, her hands at the pot fall into the water box. 1.5-3.5 close-up of the pot: girl = strip of shawl / face above the rim, fire off. 'to pour hot water' is the girl's action at 5.5-6.0 only."}
json.dump(out[97],open('content/97.json','w'),indent=1)
