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
W={0.0:(.20,.22,.72,.65),0.5:(.20,.22,.72,.65),1.0:(0,.22,.30,.82),1.5:(.25,.24,.57,.54),2.0:(.32,.24,.66,.53),2.5:(.33,.24,.65,.52),
   3.0:(.36,.26,.62,.54),3.5:(.33,.26,.62,.54),4.0:(.35,.26,.62,.57),4.5:(.30,.24,.62,.56),5.0:(.31,.26,.68,.59),5.5:(.30,.22,.70,.63),
   6.0:(.30,.19,.74,.65),6.5:(.29,.18,.79,.68),7.0:(.24,.19,.80,.73),7.5:(.13,.19,.73,.73),8.0:(.04,.18,.63,.74),8.5:(.04,.16,.64,.74),
   9.0:(.03,.17,.64,.74),9.5:(.05,.42,.66,.77),10.0:(.02,.43,.62,.78)}
M={6.0:(.75,.26,.95,.44),6.5:(.80,.25,1,.63),7.0:(.82,.26,1,.56),7.5:(.76,.22,1,.56),8.0:(.64,.21,.93,.62),8.5:(.65,.18,1,.70),
   9.0:(.65,.18,1,.70),9.5:(.67,.18,1,.66),10.0:(.63,.17,1,.67)}
c={"mediaId":4987,"level":"B","keyWord":"present","defaultVoice":"female",
 "taps":[
  {"phrase":"to present her ideas","target":"the woman in the black suit","voice":"female","keys":K(W)},
  {"phrase":"to carry a tray of coffees","target":"the man in the dark shirt","voice":"male","keys":K(M)},
  {"phrase":"to slump over the table","target":"the woman in the black suit","voice":"female","keys":K(W)}],
 "stillS":10.0,
 "nouns":[{"word":"sticky notes","x":0.25,"y":0.32,"voice":"female"},
          {"word":"takeaway cups","x":0.76,"y":0.40,"voice":"female"},
          {"word":"braids","x":0.30,"y":0.62,"voice":"female"},
          {"word":"a laptop","x":0.83,"y":0.76,"voice":"female"}],
 "question":"What is the man carrying?",
 "answer":["He","is","carrying","a","tray","of","takeaway","coffees."],
 "answerVoice":"male",
 "notes":"Third target would have been the man raising a finger (1.0-4.5), but a man at the right seems to raise a hand at 5.0, so two phrases share the presenter. Slump only at 9.5-10.0. Coffee man first appears faintly behind the glass at 6.0. Question: only he carries anything."}
json.dump(c,open('content/4987.json','w'),indent=1)
