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
rh={0.0:(0,.04,.62,.73),0.5:(0,.04,.66,.72),1.0:(0,.05,.60,.79),1.5:(0,.08,.62,.77),2.0:(0,.09,.58,.79),
 2.5:(0,.10,.56,.79),3.0:(0,.08,.45,.80),3.5:(0,.03,.42,.79),4.0:(0,0,.42,.78),4.5:(0,0,.45,.78),5.0:(0,0,.48,.76),
 5.5:(0,0,.55,.73),6.0:(0,0,.55,.69),6.5:(0,0,.58,.69),7.0:(0,0,.60,.70),7.5:(0,0,.60,.71),8.0:(0,0,.62,.76),
 8.5:(0,0,.62,.79),9.0:(0,0,.65,.81),9.5:(0,0,.66,.78),10.0:(0,.05,.66,.84)}
dh={0.0:(.62,.10,1,1),0.5:(.66,.06,1,1),1.0:(.60,.06,1,1),1.5:(.62,.12,1,1),2.0:(.58,.10,1,1),2.5:(.56,.11,1,1),
 3.0:(.45,.12,1,1),3.5:(.42,.13,1,1),4.0:(.42,.03,1,1),4.5:(.45,0,1,1),5.0:(.48,.05,1,1),5.5:(.55,0,1,1),
 6.0:(.55,0,1,1),6.5:(.58,0,1,1),7.0:(.60,0,1,1),7.5:(.60,0,1,1),8.0:(.62,.06,1,1),8.5:(.62,0,1,1),
 9.0:(.65,.13,1,1),9.5:(.66,.08,1,1),10.0:(.66,.07,1,1)}
gl={0.0:(.18,.73,.54,.99),0.5:(.18,.72,.56,.99),1.0:(.18,.79,.53,1),1.5:(.18,.77,.48,1),2.0:(.16,.79,.50,.99),
 2.5:(.13,.79,.44,.99),3.0:(.07,.80,.41,.99),3.5:(.07,.80,.40,1),4.0:(.01,.79,.40,1),4.5:(.01,.79,.43,1),
 5.0:(.01,.77,.44,1),5.5:(.01,.74,.44,1),6.0:(0,.69,.42,.97),6.5:(0,.70,.43,.97),7.0:(0,.71,.43,.99),
 7.5:(0,.72,.44,1),8.0:(.01,.77,.47,1),8.5:(.07,.80,.48,1),9.0:(.10,.82,.50,1),9.5:(.14,.79,.44,1),10.0:(.17,.85,.55,1)}
c={"mediaId":5193,"level":"B","keyWord":"rash","defaultVoice":"female",
 "taps":[
  {"phrase":"to scratch her itchy arm","target":"the red-haired woman","voice":"female","keys":K(rh,times)},
  {"phrase":"to squeeze a tube of cream","target":"the dark-haired woman","voice":"female","keys":K(dh,times)},
  {"phrase":"to rest on her lap","target":"the gardening gloves","voice":"female","keys":K(gl,times)}],
 "stillS":2.5,
 "nouns":[{"word":"a rash","x":0.48,"y":0.63,"voice":"female"},{"word":"a tube","x":0.88,"y":0.57,"voice":"female"},
  {"word":"gardening gloves","x":0.28,"y":0.89,"voice":"female"},{"word":"bushes","x":0.55,"y":0.10,"voice":"female"}],
 "question":"What is the dark-haired woman doing?",
 "answer":["She","is","applying","cream","to","the","rash."],
 "answerVoice":"female",
 "notes":"The red-haired woman's forearm and hand reach across the dark-haired woman, so the split line between their boxes runs near the rash; the red-haired box stops above the gloves on her lap. The gloves are a still object; 'to rest on her lap' is a state."}
json.dump(c,open('content/5193.json','w'),indent=1)
