import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
T=[i*0.5 for i in range(21)]
Wm={t:(.08,.31,.86,.69) for t in T}
for t in (4.0,4.5): Wm[t]=(.04,.31,.90,.69)
Wm[7.5]=(.06,.33,.90,.67)
Wm[8.0]=(0,.37,.97,.63)
for t in (8.5,9.0,9.5,10.0): Wm[t]=(0,.39,1,.61)
Ck={t:(.40,.16,.22,.14) for t in T}
c={"mediaId":101,"level":"A","keyWord":"bored","defaultVoice":"female",
"taps":[tap("to play with her keys","the woman","female",Wm),tap("to look very bored","the woman","female",Wm),tap("to show the time","the clock","female",Ck)],
"stillS":0.0,
"nouns":[noun("a clock",.51,.25,"female"),noun("keys",.70,.56,"female"),noun("a book",.33,.72,"female"),noun("a chair",.22,.85,"female")],
"question":"How does the woman look?","answer":["She","looks","very","bored."],"answerVoice":"female",
"notes":"Only two real targets (woman, clock); the book on the next seat does nothing. The keys are in her hand only at 0.0-3.5. Clock box is kept tight at the bottom (ends at y 0.30) because her head starts at about 0.32. Answer is short (4 chips) on purpose: key word 'bored'. Chair pill sits on the grey chair base/leg under the seat."}
json.dump(c,open('content/101.json','w'),indent=1)
