import json
def K(d, times):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=[max(0,min(1,v)) for v in b]
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
times=[i*0.5 for i in range(21)]
flag={1.0:(.44,.00,.62,.38),1.5:(.44,.00,.62,.30),2.0:(.46,.00,.66,.47),2.5:(.44,.00,.60,.57),3.0:(.40,.02,.62,.62),
 3.5:(.44,.03,.71,.55),4.0:(.44,.05,.67,.53),4.5:(.40,.05,.60,.46),5.0:(.40,.05,.58,.41),5.5:(.46,.04,.69,.33),
 6.0:(.45,.01,.64,.29),6.5:(.41,.04,.58,.30),7.0:(.30,.03,.55,.26),7.5:(.37,.03,.56,.26),8.0:(.35,.01,.56,.26),
 8.5:(.34,.01,.55,.25),9.0:(.37,.01,.55,.26),9.5:(.37,.01,.55,.25),10.0:(.30,.01,.56,.25)}
woman={0.0:(.18,.00,1.0,1.0),1.0:(.62,.00,1.0,1.0),1.5:(.45,.30,1.0,1.0),2.0:(.45,.47,.92,1.0),2.5:(.38,.57,.80,1.0),
 3.0:(.38,.63,.76,1.0),3.5:(.44,.70,.79,1.0),4.0:(.49,.76,.69,1.0),4.5:(.50,.80,.70,1.0),5.0:(.51,.86,.70,1.0),
 5.5:(.50,.86,.70,1.0),6.0:(.46,.80,.64,1.0),6.5:(.49,.77,.68,1.0),7.0:(.51,.76,.70,1.0),7.5:(.52,.75,.72,1.0),
 8.0:(.48,.74,.75,1.0),8.5:(.62,.74,.84,1.0),9.0:(.69,.74,.89,1.0),9.5:(.70,.74,.89,1.0),10.0:(.69,.74,.89,1.0)}
hut={2.5:(.80,.55,1.0,.69),3.0:(.80,.60,1.0,.74),3.5:(.80,.66,1.0,.80),4.0:(.72,.70,.97,.83),4.5:(.72,.73,.96,.87),
 5.0:(.72,.77,.93,.91),5.5:(.72,.78,.92,.92),6.0:(.67,.79,.90,.93),6.5:(.69,.78,.91,.93),7.0:(.71,.79,.92,.94),
 7.5:(.73,.79,.92,.94),8.0:(.76,.78,.94,.93)}
c={"mediaId":5192,"level":"B","keyWord":"horizon","defaultVoice":"female",
 "taps":[
  {"phrase":"to flutter in the wind","target":"the red flag","voice":"female","keys":K(flag,times)},
  {"phrase":"to wear her hair loose","target":"the blonde woman","voice":"female","keys":K(woman,times)},
  {"phrase":"to sit on the horizon","target":"the hut","voice":"female","keys":K(hut,times)}],
 "stillS":6.0,
 "nouns":[{"word":"a flag","x":0.56,"y":0.15,"voice":"female"},{"word":"a flagpole","x":0.48,"y":0.50,"voice":"female"},
  {"word":"a hut","x":0.80,"y":0.86,"voice":"female"},{"word":"the horizon","x":0.18,"y":0.90,"voice":"female"}],
 "question":"What are the people doing?",
 "answer":["They","are","hoisting","a","red","flag."],
 "answerVoice":"female",
 "notes":"The blonde woman is the only one without a dark beanie; at 0.5 s only an arm and glove fill the frame, so she is off there; at 1.0 s her box excludes the gloved hands to stay clear of the flag. The hut is off where it is a tiny sliver (2.0 s, 8.5-10.0 s) or not in shot (0-1.5 s)."}
json.dump(c,open('content/5192.json','w'),indent=1)
