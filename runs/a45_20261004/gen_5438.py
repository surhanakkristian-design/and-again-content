import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(.24,0,.76,.74),0.5:(.24,0,.76,.74),1.0:(.24,0,.76,.74),1.5:(.43,0,.57,.70),2.0:(.30,0,.70,.64),
2.5:(.40,0,.60,.62),3.0:(.16,0,.84,.62),3.5:(.30,0,.70,.60),4.0:(.18,0,.82,.58),
4.5:(.14,.06,.45,.57),5.0:(.09,.06,.53,.57),5.5:(.08,.05,.49,.59),6.0:(0,0,.52,.66),6.5:(0,0,.50,.66),
7.0:(0,0,1,.56),7.5:(0,0,1,.57),8.0:(0,.02,1,.54),8.5:(0,.02,1,.55),9.0:(0,.02,1,.55),9.5:(0,.02,1,.55),
10.0:(0,.03,1,.55),10.5:(0,.03,1,.55),11.0:(0,.03,.63,.60),11.5:(0,.04,.57,.58),12.0:(0,.05,.43,.57)}
boy={4.5:(.59,.26,.27,.30),5.0:(.62,.27,.26,.30),5.5:(.57,.26,.28,.28),6.0:(.52,.25,.22,.24),6.5:(.51,.25,.31,.22),
11.0:(.63,.24,.37,.38),11.5:(.57,.26,.43,.38),12.0:(.43,.24,.52,.38)}
pot={4.5:(.06,.63,.92,.34),5.0:(.02,.63,.94,.35),5.5:(.04,.65,.94,.33),6.0:(0,.67,.95,.30),6.5:(.06,.67,.94,.30),
7.0:(0,.57,1,.43),7.5:(0,.58,1,.42),8.0:(0,.56,1,.44),8.5:(0,.57,1,.43),9.0:(0,.57,1,.43),9.5:(0,.57,1,.43),
10.0:(0,.58,1,.42),10.5:(0,.58,1,.42)}
c={"mediaId":5438,"level":"B","keyWord":"filling","defaultVoice":"female",
"taps":[{"phrase":"to taste a steaming dumpling","target":"the woman","voice":"female","keys":K(woman)},
{"phrase":"to wear an embroidered waistcoat","target":"the boy","voice":"male","keys":K(boy)},
{"phrase":"to bubble on the stove","target":"the big pot","voice":"female","keys":K(pot)}],
"stillS":12.0,
"nouns":[{"word":"filling","x":0.13,"y":0.59,"voice":"female"},{"word":"dumplings","x":0.55,"y":0.66,"voice":"female"},
{"word":"an apron","x":0.22,"y":0.40,"voice":"female"},{"word":"a waistcoat","x":0.70,"y":0.43,"voice":"female"}],
"question":"What is the woman tasting?","answer":["She","is","tasting","a","steaming","dumpling."],"answerVoice":"female",
"notes":"Boy is only visible 4.5-6.5 s and 11-12 s; his phrase is a state (embroidered waistcoat) because his only action is watching/smiling, which the woman also does. The big pot is on the stove from 4.5-10.5 s, off in the end shot (wooden bowl there instead). Woman and pot overlap 7-10.5 s (she leans over it): split along the pot rim. 'filling' = the white bowl of red filling at the left of the end shot."}
json.dump(c,open('content/5438.json','w'),indent=1)
