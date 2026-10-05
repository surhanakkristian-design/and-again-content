import json
times=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in times:
        if t in d:
            x1,y1,x2,y2=d[t]; out.append({"t":t,"x":round(x1,2),"y":round(y1,2),"w":round(x2-x1,2),"h":round(y2-y1,2)})
        else: out.append({"t":t,"off":True})
    return out
M={0.0:(.40,.28,.61,.56),0.5:(.40,.27,.60,.57),1.0:(.39,.27,.63,.58),1.5:(.38,.26,.64,.59),2.0:(.39,.24,.61,.59),2.5:(.31,.23,.75,.61),
3.0:(.40,.17,.76,.66),3.5:(.16,.22,.94,.63),4.0:(.05,.38,.97,.57),4.5:(.28,.30,.98,.59),5.0:(.20,.40,.97,.57),5.5:(.29,.42,.94,.62),
6.0:(.27,.42,.93,.63),6.5:(.29,.41,.78,.63),7.0:(.28,.44,.74,.66),7.5:(.26,.41,.80,.67),8.0:(.21,.34,.74,.67),8.5:(.31,.33,.74,.68),
9.0:(.31,.35,.90,.83),9.5:(.28,.37,.81,.85),10.0:(.24,.37,.84,.76)}
P={0.0:(.62,.34,.80,.48),0.5:(.61,.34,.79,.48),2.0:(.20,.33,.38,.47),2.5:(.12,.33,.30,.47),3.0:(.16,.31,.36,.45),
4.0:(.67,.19,.85,.34),4.5:(.80,.15,.99,.29),5.0:(.81,.17,1.0,.31),5.5:(.80,.19,.99,.34),6.0:(.80,.19,.99,.35),6.5:(.79,.19,.99,.35),
7.0:(.76,.20,.96,.35),7.5:(.72,.20,.92,.36),8.0:(.65,.20,.83,.33),8.5:(.56,.20,.74,.32),9.0:(.45,.22,.63,.34),9.5:(.31,.22,.51,.36),10.0:(.21,.22,.40,.36)}
F={0.0:(.0,.58,1.0,1.0),0.5:(.0,.58,1.0,1.0),1.0:(.0,.60,.70,1.0),1.5:(.0,.60,.50,1.0),2.0:(.0,.60,.40,.95),2.5:(.0,.62,.34,.98),
3.0:(.0,.61,.37,.98),3.5:(.0,.64,.56,.96),4.0:(.0,.58,.82,1.0),4.5:(.0,.60,.84,1.0),5.0:(.0,.66,.60,1.0),7.0:(.58,.80,.80,.95),7.5:(.40,.86,.62,1.0)}
def inter(a,b): return min(a[2],b[2])-max(a[0],b[0])>0.001 and min(a[3],b[3])-max(a[1],b[1])>0.001
for t in times:
    for n1,n2,a,b in (("M","P",M,P),("M","F",M,F),("P","F",P,F)):
        if t in a and t in b and inter(a[t],b[t]): print("OVERLAP",t,n1,n2,a[t],b[t])
c={"mediaId":4030,"level":"A","keyWord":"park","defaultVoice":"male",
"taps":[
 {"phrase":"to fall into the water","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to swim in the pond","target":"the fish","voice":"male","keys":keys(F)},
 {"phrase":"to walk together","target":"the two people","voice":"male","keys":keys(P)}],
"stillS":0.0,
"nouns":[{"word":"trees","x":0.35,"y":0.20,"voice":"male"},
 {"word":"a man","x":0.52,"y":0.35,"voice":"male"},
 {"word":"a bench","x":0.18,"y":0.44,"voice":"male"},
 {"word":"fish","x":0.28,"y":0.76,"voice":"male"}],
"question":"Where is the man walking?",
"answer":["He","is","walking","in","the","park."],
"answerVoice":"male",
"notes":"Key word 'park' is the whole place, not one spot, so it is not a noun slot; it is in the answer instead. The pair in the background is small and far away (gender not certain, so 'the two people'); hidden behind the man at 1.0-1.5 s and out of frame at 3.5 s (off). A third, single walker is visible far left at times; 'to walk together' does not fit him. Fish box = the whole group of fish under the surface; off from 5.5 s when the water is churned, except single fish at 7.0 and 7.5 s. At 8.0-9.0 s the pair is just above the man's head: split with a horizontal line. Camera pans/cuts at 4.0 s."}
json.dump(c,open("content/4030.json","w"),indent=1)
