import json
T=[i*0.5 for i in range(25)]
def mk(d):
    ks=[]
    for t in T:
        b=d.get(t)
        if b: ks.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
        else: ks.append({"t":t,"off":True})
    return ks
C={1.5:(0,.24,.24,.38),2.0:(0,.21,.25,.37),2.5:(0,.19,.20,.38),3.0:(0,.19,.18,.35),3.5:(0,.17,.18,.34),4.0:(0,.17,.20,.41),
   5.5:(0,.06,.62,1),6.0:(0,.03,.70,1),9.0:(.79,.05,.99,.20),9.5:(.79,.14,1,.32),10.0:(.73,.21,.93,.34),10.5:(.66,.28,.84,.40),
   11.0:(.60,.28,.78,.41),11.5:(.58,.29,.76,.43),12.0:(.56,.32,.74,.45)}
A={1.5:(.08,.38,.48,1),2.0:(0,.37,.46,1),2.5:(0,.38,.80,1),3.0:(0,.35,.82,1),3.5:(0,.34,.86,1),4.0:(0,.41,.42,1),
   9.5:(.60,.28,.78,.41),10.0:(.59,.35,.77,.49),10.5:(.53,.40,.71,.53),11.0:(.52,.41,.70,.55),11.5:(.51,.435,.69,.57),12.0:(.50,.455,.68,.59)}
B={6.5:(0,.17,.78,1),7.0:(0,.15,.85,1),7.5:(0,.15,.92,1),9.0:(.36,.09,.57,.22),9.5:(.42,.22,.60,.39),10.0:(.41,.30,.58,.44),
   10.5:(.35,.34,.53,.49),11.0:(.35,.37,.52,.51),11.5:(.33,.38,.51,.52),12.0:(.32,.41,.50,.55)}
c={"mediaId":5099,"level":"A","keyWord":"photo","defaultVoice":"male",
 "taps":[
  {"phrase":"to hold a cup of coffee","target":"the man with the cup","voice":"male","keys":mk(C)},
  {"phrase":"to carry a camera","target":"the woman with the camera","voice":"female","keys":mk(A)},
  {"phrase":"to add a German flag","target":"the blonde woman","voice":"female","keys":mk(B)}],
 "stillS":7.5,
 "nouns":[{"word":"a woman","x":0.20,"y":0.38,"voice":"female"},{"word":"a photo","x":0.75,"y":0.52,"voice":"male"},
          {"word":"a map","x":0.60,"y":0.88,"voice":"male"}],
 "question":"What is the blonde woman doing?",
 "answer":["She","is","adding","a","German","flag","to","the","map."],
 "answerVoice":"female",
 "notes":"Group selfie 9.0-12.0 has ~15 people: the cup man is boxed as the lower-right bearded man in the striped shirt (best match of face/shirt, not certain; the other bearded man stands just above him). Camera woman = the only Asian woman (camera not visible in the selfie); blonde woman = the one with plaits, centre of the selfie. 0-1.0 and 8.0-8.5 (map close-ups) all off. Camera woman not visible at 9.0."}
json.dump(c,open('content/5099.json','w'),indent=1)
