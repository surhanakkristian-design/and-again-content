import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
cas={0.0:(0,.12,1,.92),0.5:(0,.12,1,.92),1.0:(0,.17,1,.86),1.5:(.03,.30,1,.78),2.0:(.02,.34,1,.71),2.5:(.03,.32,1,.68)}
tent={3.0:(0,.18,1,.88),3.5:(0,.24,1,.86),4.0:(0,.33,1,.82)}
arch={4.5:(.04,.22,.97,.69),5.0:(.01,.25,.95,.69),5.5:(.03,.35,.97,.69),6.0:(.03,.42,.95,.66)}
c={"mediaId":4906,"level":"B","keyWord":"tent","defaultVoice":"female",
 "taps":[{"phrase":"to carry a warning label","target":"the small bouncy castle","voice":"female","keys":keys(cas)},
  {"phrase":"to be weighted down","target":"the tent","voice":"female","keys":keys(tent)},
  {"phrase":"to buckle in the middle","target":"the inflatable arch","voice":"female","keys":keys(arch)}],
 "stillS":3.0,
 "nouns":[{"word":"a tent","x":.55,"y":.28,"voice":"female"},{"word":"a window","x":.20,"y":.55,"voice":"female"},
  {"word":"a pole","x":.47,"y":.66,"voice":"female"},{"word":"a lawn","x":.78,"y":.88,"voice":"female"}],
 "question":"What is happening to the tent?","answer":["The","tent","is","collapsing","onto","the","lawn."],"answerVoice":"female",
 "notes":"Every inflatable in the clip deflates, so phrases use distinguishing features instead of 'collapse'. The warning label is visible only 0-1.0 s. The tent's roof also sags at 3.5 s; 'buckle in the middle' is meant for the arch folding into an M (5.5 s). The large castle with a slide (6.5-9.0 s) is no target. A woman and a boy stand far right at 4.5-6.0 s."}
json.dump(c,open('content/4906.json','w'),indent=1)
