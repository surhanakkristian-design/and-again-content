import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=v; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
N={0.0:(.22,.33,.68,.66),0.5:(.10,.27,.62,.74),1.0:(.36,.30,.70,.84),1.5:(.32,.33,.62,.66),2.0:(.46,.36,.64,.62),2.5:(.42,.41,.60,.61),
   3.0:(.40,.41,.60,.60),3.5:(.43,.45,.61,.66),4.0:(.42,.47,.60,.69),4.5:(.43,.49,.61,.71),5.0:(.45,.51,.63,.76),5.5:(.44,.50,.62,.75),
   6.0:(.50,.27,.68,.54),6.5:(.50,.28,.68,.56),7.0:(.48,.27,.66,.59),7.5:(.44,.29,.62,.60),8.0:(.44,.25,.66,.61),8.5:(.42,.24,.60,.61),9.0:(.42,.31,.60,.60)}
S={0.5:(.63,.64,1,.74),2.0:(0,.22,.20,.36),2.5:(0,.22,.20,.36),3.0:(0,.21,.18,.35),3.5:(0,.18,.20,.32),4.0:(0,.12,.20,.26),4.5:(0,.12,.20,.25),
   5.0:(0,.13,.22,.27),5.5:(0,.10,.20,.24),6.0:(0,0,1,.11),6.5:(.35,0,1,.10),7.0:(.38,0,1,.10),7.5:(.35,0,1,.11),8.0:(0,0,1,.10),8.5:(.38,0,1,.10),9.0:(0,0,1,.13)}
c={"mediaId":4988,"level":"A","keyWord":"attack","defaultVoice":"male",
 "taps":[
  {"phrase":"to carry a big flag","target":"the man in armour","voice":"male","keys":K(N)},
  {"phrase":"to lead the attack","target":"the man in armour","voice":"male","keys":K(N)},
  {"phrase":"to watch the fighters","target":"the people at the top","voice":"male","keys":K(S)}],
 "stillS":4.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.05,"voice":"male"},
          {"word":"flags","x":0.50,"y":0.14,"voice":"male"},
          {"word":"grass","x":0.13,"y":0.45,"voice":"male"},
          {"word":"tents","x":0.45,"y":0.84,"voice":"male"}],
 "question":"What is the man in armour carrying?",
 "answer":["He","is","carrying","a","big","flag."],
 "answerVoice":"male",
 "notes":"The armoured flag carrier is small in the wide crowd shots (2.0-9.0); boxes follow his banner and plate armour, verify. One or two other small banners in the crowd (e.g. left at 4.0-5.5). Spectators: box only the clear cluster (left at 2.0-5.5, top row behind the fence 6.0-9.0); off at 0.0 (none) and 1.0-1.5 (mixed with fighters). Spectators at 2.0-5.5 also at the right edge, not boxed."}
json.dump(c,open('content/4988.json','w'),indent=1)
