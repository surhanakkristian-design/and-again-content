import json
T=[i*0.5 for i in range(19)]
W={0.0:(.33,.50,.45,.50),0.5:(.33,.12,.55,.88),1.0:(.20,.03,.68,.97),1.5:(.15,.08,.85,.92),2.0:(.22,.10,.78,.90),
 2.5:(.03,.12,.97,.88),3.0:(.10,.17,.90,.83),3.5:(.12,.17,.88,.83),4.0:(.20,.15,.80,.85),4.5:(.22,.15,.78,.85),
 5.0:(0,0,1,.60),5.5:(0,0,1,.60),6.0:(0,0,1,.72),6.5:(.10,0,.82,.65),7.0:(.12,.08,.74,.68),7.5:(.10,.33,.83,.62),
 8.0:(0,.27,1,.65),8.5:(0,.27,1,.65),9.0:(0,.27,1,.66)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
wk=keys(W)
c={"mediaId":5181,"level":"B","keyWord":"signature","defaultVoice":"female",
 "taps":[{"phrase":"to step out of a limousine","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to sign an official document","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to raise her arms in triumph","target":"the woman","voice":"female","keys":wk}],
 "stillS":6.5,
 "nouns":[{"word":"a signature","x":.58,"y":.65,"voice":"female"},{"word":"a fountain pen","x":.15,"y":.71,"voice":"female"},
          {"word":"a flag","x":.86,"y":.18,"voice":"female"},{"word":"a desk","x":.50,"y":.88,"voice":"female"}],
 "question":"What is the woman signing?","answer":["She","is","signing","an","official","document."],"answerVoice":"female",
 "notes":"Only the grey-haired woman does all the actions; men only shake hands and stand in the background, so all three phrases use her. At t=0.0 only her legs are visible below the car door. Several cuts (palace steps, hall, desk close-up, balcony)."}
json.dump(c,open('content/5181.json','w'),indent=1)
