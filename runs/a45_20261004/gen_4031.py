import json
times=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in times:
        if t in d:
            x1,y1,x2,y2=d[t]; out.append({"t":t,"x":round(x1,2),"y":round(y1,2),"w":round(x2-x1,2),"h":round(y2-y1,2)})
        else: out.append({"t":t,"off":True})
    return out
O={0.0:(.04,.19,.36,.52),0.5:(.05,.19,.37,.52),1.0:(.04,.20,.36,.52),1.5:(.04,.22,.36,.52),2.0:(.04,.22,.36,.52),2.5:(.04,.23,.36,.52),
3.0:(.02,.24,.36,.52),3.5:(.02,.24,.36,.52),4.0:(.02,.24,.36,.52),4.5:(.02,.24,.36,.52),5.0:(.02,.24,.36,.52),5.5:(.02,.24,.36,.52),
6.0:(.0,.24,.36,.52),6.5:(.0,.11,.36,.52),7.0:(.0,.12,.39,.52),7.5:(.0,.11,.38,.52),8.0:(.0,.08,.35,.52),8.5:(.0,.08,.32,.52),
9.0:(.0,.10,.33,.52),9.5:(.0,.14,.33,.52),10.0:(.0,.16,.36,.52)}
C={0.0:(.37,.22,.65,.52),0.5:(.38,.22,.65,.52),1.0:(.37,.23,.65,.52),1.5:(.37,.23,.65,.52),2.0:(.37,.25,.66,.52),2.5:(.37,.26,.66,.52),
3.0:(.37,.27,.65,.52),3.5:(.37,.27,.65,.52),4.0:(.37,.27,.66,.52),4.5:(.37,.27,.66,.52),5.0:(.37,.27,.66,.52),5.5:(.37,.27,.66,.52),
6.0:(.37,.26,.66,.52),6.5:(.37,.22,.65,.52),7.0:(.40,.23,.70,.52),7.5:(.39,.22,.66,.52),8.0:(.36,.23,.63,.52),8.5:(.33,.23,.62,.52),
9.0:(.34,.23,.58,.52),9.5:(.34,.22,.65,.52),10.0:(.37,.21,.68,.52)}
B={t:(.38,.59,.62,.84) for t in times}
def inter(a,b): return min(a[2],b[2])-max(a[0],b[0])>0.001 and min(a[3],b[3])-max(a[1],b[1])>0.001
for t in times:
    for n1,n2,a,b in (("O","C",O,C),("O","B",O,B),("C","B",C,B)):
        if inter(a[t],b[t]): print("OVERLAP",t,n1,n2,a[t],b[t])
c={"mediaId":4031,"level":"B","keyWord":"top","defaultVoice":"male",
"taps":[
 {"phrase":"to toss a tennis ball","target":"the man in orange","voice":"male","keys":keys(O)},
 {"phrase":"to clutch his head","target":"the man in the cap","voice":"male","keys":keys(C)},
 {"phrase":"to support the tennis balls","target":"the plastic bottle","voice":"male","keys":keys(B)}],
"stillS":5.0,
"nouns":[{"word":"a baseball cap","x":0.50,"y":0.31,"voice":"male"},
 {"word":"tennis balls","x":0.50,"y":0.44,"voice":"male"},
 {"word":"a net","x":0.80,"y":0.53,"voice":"male"},
 {"word":"a plastic bottle","x":0.50,"y":0.70,"voice":"male"}],
"question":"Where does the tennis ball land?",
"answer":["It","lands","on","the","top","ball."],
"answerVoice":"male",
"notes":"Key word 'top' (adjective) is used in the answer ('the top ball'). The man in red does nothing that only he does, so the third target is the bottle. The man in the cap clutches his head from 6.5 s only. From 6.5 s the raised right arm of the man in orange crosses in front of the man in the cap: boxes split by a vertical line, so the orange man's right fist falls outside his box at 8.0-10.0 s. Question in the present simple (one completed event)."}
json.dump(c,open("content/4031.json","w"),indent=1)
