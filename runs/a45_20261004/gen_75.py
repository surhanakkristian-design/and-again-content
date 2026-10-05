import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def write(mid,level,kw,dv,taps,still,nouns,q,a,av,notes):
    json.dump({"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
      "taps":[{"phrase":p,"target":t,"voice":v,"keys":keys(k)} for p,t,v,k in taps],
      "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
      "question":q,"answer":a,"answerVoice":av,"notes":notes},open(f"content/{mid}.json","w"),indent=1)

# ---- 75
bat={0.0:(.26,.12,.44,.57),0.5:(.22,.12,.50,.60),1.0:(.08,.12,.80,.58),1.5:(0,.12,.86,.62),2.0:(0,.10,1,.64),
 2.5:(.33,.08,.40,.62),3.0:(.33,.06,.38,.64),3.5:(.18,0,.72,.66),4.0:(.35,.78,.50,.22),4.5:(.36,.53,.36,.24),
 5.0:(.12,.31,.52,.24),5.5:(0,.47,.57,.21),6.0:(.22,.53,.31,.14),6.5:(.40,.53,.32,.15),7.0:(.47,.45,.28,.14),
 7.5:(.46,.46,.33,.14),8.0:(.42,.39,.26,.14),8.5:(.45,.42,.20,.14),9.0:(.43,.41,.22,.14),9.5:(.48,.40,.20,.14),
 10.0:(.47,.34,.20,.14)}
swarm={5.5:(.40,.19,.60,.14),6.0:(.30,.28,.70,.14),6.5:(.20,.33,.80,.14),7.0:(.04,.30,.78,.14),7.5:(0,.31,.85,.14),
 8.0:(0,.39,.41,.14),8.5:(0,.41,.44,.14),9.0:(0,.44,.42,.14),9.5:(0,.47,.47,.14),10.0:(0,.49,.60,.14)}
lake={4.0:(0,.22,1,.27),4.5:(0,.17,1,.29),5.0:(.65,.33,.35,.25),5.5:(0,.70,1,.30),6.0:(0,.68,1,.32),6.5:(0,.70,1,.30),
 7.0:(0,.60,1,.40),7.5:(0,.62,1,.38),8.0:(0,.65,1,.35),8.5:(0,.67,1,.33),9.0:(0,.70,1,.30),9.5:(0,.71,1,.29),10.0:(0,.72,1,.28)}
write(75,"B","flap","male",
 [("to flap its leathery wings","the big bat","male",bat),
  ("to swarm across the sky","the flock of bats","male",swarm),
  ("to reflect the sunset","the lake","male",lake)],
 10.0,[("a bat",.57,.44,"male"),("the sky",.50,.14,"male"),("trees",.60,.63,"male"),("a lake",.50,.85,"male")],
 "What is the big bat doing?",["It","is","flapping","its","wings","over","the","lake."],"male",
 "Hanging bat (0-3.5 s) and flying bat (4-10 s) treated as the same big bat. The distant flock is tiny dots; from 8.0 s it lies behind the big bat, boxes split at the bat's left edge. The lake box at 5.0-6.5 s is only the part of the water not covered by the bat's box; at 4.0 s the pink area in the cave mouth is taken as water.")
