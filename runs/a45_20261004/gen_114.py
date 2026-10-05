import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
M={2.5:(.33,0,1,.55),3.0:(.48,0,1,.63),3.5:(.50,0,1,.64),4.0:(.53,0,1,.57),4.5:(.58,0,1,.57),5.0:(.22,0,1,.72),5.5:(.20,0,1,.76),
   6.0:(.42,0,1,.70),6.5:(.45,0,1,.70),7.0:(.30,0,1,.74),7.5:(.38,0,1,.77),8.0:(.38,0,1,.70),8.5:(.34,0,1,.70),9.0:(.42,0,1,.86),
   9.5:(.38,0,1,.80),10.0:(.36,0,1,.74)}
F={0.0:(.12,.22,.45,.46),0.5:(.15,.22,.48,.44),1.0:(0,.25,.25,.50)}
B={2.5:(.07,.47,.25,.61),8.0:(.16,.56,.36,.70),8.5:(.15,.57,.34,.71),9.0:(.21,.58,.41,.72),9.5:(.17,.58,.37,.72),10.0:(.15,.60,.35,.74)}
c={"mediaId":114,"level":"A","keyWord":"bread","defaultVoice":"female",
 "taps":[{"phrase":"to knock on the bread","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to burn in the oven","target":"the fire","voice":"female","keys":keys(F)},
         {"phrase":"to stand on the floor","target":"the bird","voice":"female","keys":keys(B)}],
 "stillS":3.5,
 "nouns":[{"word":"bread","x":.50,"y":.65,"voice":"female"},{"word":"a man","x":.80,"y":.22,"voice":"male"},
          {"word":"a woman","x":.15,"y":.20,"voice":"female"},{"word":"a table","x":.50,"y":.90,"voice":"female"}],
 "question":"What is the man doing?","answer":["He","is","knocking","on","the","bread."],"answerVoice":"male",
 "notes":"The man knocks on the loaf at 2.5-3.0 s only. The fire is visible only 0-1.0 s. The bird is small (doorway behind the table, 2.5 s and 8.0-10.0 s) - weakest target; woman not used as a target because everything she does (tear, eat, smile) the man does too. At 5.0-6.5 s the hands of both people are on the bread; the man's box may include a hand of the woman. Hand on the peel at 0.0 s is not attributed to anyone."}
json.dump(c,open("content/114.json","w"),indent=1)
