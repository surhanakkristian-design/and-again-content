import json
def K(d, times):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=[max(0,min(1,v)) for v in b]
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
times=[i*0.5 for i in range(19)]
flag={0.0:(.39,.13,.70,.41),0.5:(.34,.10,.62,.37),1.0:(.40,.00,.66,.27),1.5:(.44,.07,.67,.33),2.0:(.60,.00,.78,.15),
 2.5:(.63,.12,.91,.28),3.0:(.44,.23,.62,.97),3.5:(.47,.20,.60,.97),4.0:(.43,.08,.58,.95),4.5:(.44,.03,.58,.92),
 5.0:(.44,.00,.55,.91),5.5:(.37,.07,.58,.62),6.0:(.36,.02,.57,.51),6.5:(.38,.00,.57,.38),7.0:(.30,.00,.57,.33),
 7.5:(.22,.00,.57,.28),8.0:(.00,.02,.58,.28),8.5:(.00,.00,.61,.32),9.0:(.00,.07,.62,.41)}
man={3.0:(.15,.38,.44,1.0),3.5:(.16,.38,.47,1.0),4.0:(.15,.40,.43,1.0),4.5:(.13,.43,.44,1.0),5.0:(.10,.47,.44,1.0),
 5.5:(.22,.74,.58,1.0),6.0:(.22,.79,.54,1.0),6.5:(.23,.79,.56,1.0),7.0:(.21,.81,.55,1.0),7.5:(.21,.81,.55,1.0),
 8.0:(.28,.80,.56,1.0),8.5:(.28,.75,.57,1.0),9.0:(.30,.68,.65,1.0)}
c={"mediaId":5191,"level":"A","keyWord":"snowy","defaultVoice":"female",
 "taps":[
  {"phrase":"to go up the pole","target":"the flag","voice":"female","keys":K(flag,times)},
  {"phrase":"to blow in the wind","target":"the flag","voice":"female","keys":K(flag,times)},
  {"phrase":"to raise his fist","target":"the man at the pole","voice":"male","keys":K(man,times)}],
 "stillS":1.5,
 "nouns":[{"word":"a flag","x":0.58,"y":0.20,"voice":"female"},{"word":"the sky","x":0.22,"y":0.38,"voice":"female"},
  {"word":"a coat","x":0.30,"y":0.85,"voice":"female"},{"word":"snow","x":0.88,"y":0.87,"voice":"female"}],
 "question":"What are the people doing?",
 "answer":["They","are","raising","a","flag","in","the","snow."],
 "answerVoice":"female",
 "notes":"Only the flag and the bearded man at the pole have unique actions; the woman with braids pulls the rope like the others, so the flag takes two phrases. The man raises his fist only at 8.5-9.0 s. Flag box split from the people at 3.0-5.0 s where it hangs between them."}
json.dump(c,open('content/5191.json','w'),indent=1)
