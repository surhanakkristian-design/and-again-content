import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
T=[i*0.5 for i in range(21)]
M={0.0:(0,.20,1,.80),0.5:(0,.20,1,.80),1.0:(0,.20,1,.80),1.5:(0,.20,1,.80),2.0:(0,.22,1,.37),2.5:(0,.22,1,.39),3.0:(0,.24,1,.43),3.5:(0,.24,1,.44),
4.0:(0,.22,1,.62),4.5:(0,.16,1,.84),5.0:(0,.26,1,.74),5.5:(0,.26,1,.74),6.0:None,6.5:(0,.40,.76,.46),7.0:(0,.52,.95,.45),7.5:(0,.52,.95,.45)}
for t in (8.0,8.5,9.0,9.5,10.0): M[t]=(0,.53,.95,.36)
Co={t:None for t in T}
Co.update({2.0:(.40,.60,.20,.15),2.5:(.37,.62,.20,.15),3.0:(.38,.68,.20,.14),3.5:(.36,.69,.18,.14),4.0:(.38,.86,.20,.14)})
Ck={t:None for t in T}
Ck[6.0]=(.18,.10,.65,.40)
for t in (6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0): Ck[t]=(.62,.16,.20,.15)
c={"mediaId":103,"level":"B","keyWord":"laundromat","defaultVoice":"male",
"taps":[tap("to sprawl across the chairs","the man","male",M),tap("to spin on the counter","the coin","male",Co),tap("to hang above a whiteboard","the clock","male",Ck)],
"stillS":8.0,
"nouns":[noun("a clock",.71,.24,"male"),noun("a whiteboard",.76,.34,"male"),noun("washing machines",.30,.53,"male"),noun("sandals",.13,.79,"male")],
"question":"Where is the man lying?","answer":["He","is","lying","across","the","laundromat","chairs."],"answerVoice":"male",
"notes":"The key word 'laundromat' is the whole room, not one thing, so it is in the answer, not a noun. The coin is small and only in 2.0-4.0 (on its edge spinning at 2.0-2.5, lying at 3.0-3.5, falling and blurred at 4.0); its box touches the man's hand, the man's box there is his head/arms above the coin so his right hand is partly cut. The man sprawls across the chairs only from 7.0 (0.0-5.5 he is slumped on the counter). 4.5: a paper cup stands on his head (inside his box). Clock: close-up at 6.0, small on the wall from 6.5. The machines may be dryers rather than washing machines; they stand in a row, so bare plural."}
json.dump(c,open('content/103.json','w'),indent=1)
