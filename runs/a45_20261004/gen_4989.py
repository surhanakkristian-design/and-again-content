import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=v; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
N={0.0:(.38,.26,.56,.41),0.5:(.37,.25,.55,.42),1.0:(.37,.24,.55,.44),1.5:(.37,.23,.56,.44),2.0:(.38,.26,.56,.48),2.5:(.38,.30,.56,.52),
   3.0:(.39,.43,.57,.57),3.5:(.40,.45,.58,.59),4.0:(.42,.48,.60,.62),4.5:(.44,.50,.62,.63),5.0:(.44,.51,.59,.65),5.5:(.40,.51,.56,.66),
   6.0:(.38,.50,.55,.66),6.5:(.33,.49,.51,.64),7.0:(.30,.48,.50,.67),7.5:(.28,.35,.48,.69),8.0:(.26,.25,.56,.71),8.5:(.27,.08,.75,.79)}
P={t:(0,.30,.18,.70) for t in (0.0,0.5)}
P.update({1.0:(0,.33,.18,.75),1.5:(0,.33,.18,.75),2.0:(0,.37,.18,.75),2.5:(0,.40,.18,.75),3.0:(0,.43,.18,.80),3.5:(0,.43,.18,.80),
   4.0:(0,.38,.18,.88),4.5:(0,.38,.18,1),5.0:(0,.48,.18,1),5.5:(0,.45,.18,1),6.0:(0,.45,.18,1),6.5:(0,.45,.17,1),7.0:(0,.45,.17,1),
   7.5:(0,.45,.16,1),8.0:(0,.43,.18,1),8.5:(0,.45,.18,1)})
TE={0.0:(.82,.53,1,.85),0.5:(.82,.54,1,.86),1.0:(.82,.55,1,.88),1.5:(.82,.56,1,.90),2.0:(.78,.54,1,.88),2.5:(.74,.55,1,.87),3.0:(.70,.55,1,.84),
   3.5:(.64,.54,1,.81),4.0:(.62,.41,1,.77),4.5:(.63,.41,1,.73),5.0:(.60,.43,1,.73),5.5:(.57,.39,1,.70),6.0:(.56,.39,1,.68),6.5:(.54,.39,1,.70),
   7.0:(.57,.40,1,.66),7.5:(.58,.39,1,.66),8.0:(.57,.38,1,.68),8.5:(.76,.38,1,.68),9.0:(.48,.40,.95,.56),9.5:(.45,.41,.98,.56)}
c={"mediaId":4989,"level":"A","keyWord":"hill","defaultVoice":"male",
 "taps":[
  {"phrase":"to run ahead of the others","target":"the man in armour","voice":"male","keys":K(N)},
  {"phrase":"to film with a phone","target":"the people on the left","voice":"male","keys":K(P)},
  {"phrase":"to stand below the hill","target":"the white tent","voice":"male","keys":K(TE)}],
 "stillS":4.0,
 "nouns":[{"word":"flags","x":0.35,"y":0.36,"voice":"male"},
          {"word":"a hill","x":0.25,"y":0.56,"voice":"male"},
          {"word":"a tent","x":0.80,"y":0.60,"voice":"male"},
          {"word":"a rope","x":0.40,"y":0.71,"voice":"male"}],
 "question":"Where are the men running?",
 "answer":["They","are","running","down","the","hill."],
 "answerVoice":"male",
 "notes":"At 0.0-1.5 the knight stands on the crest (alone at 0.0, line forming behind him); 'run ahead of the others' is true from about 2.0 to 8.5. Knight off from 9.0 (passed the camera). Phone-filming spectators are only partly visible at the left edge; phones clearly seen 5.0-8.0; off 9.0-10.0. Tent phrase is a state (tents cannot act); from 4.5 the tent is a double tent and is boxed as one. Tent at 9.0-9.5 boxed on its visible upper part only, off at 10.0 (hidden behind fighters)."}
json.dump(c,open('content/4989.json','w'),indent=1)
