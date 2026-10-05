import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
# boxes as x0,y0,x1,y1
W={0.0:(.20,.19,.84,1.0),0.5:(.18,.16,.80,1.0),1.0:(.14,.16,.88,1.0),1.5:(.30,.12,.86,1.0),2.0:(.26,.12,.82,1.0),
   2.5:(.44,.13,.87,.97),3.0:(.32,.19,.84,1.0),3.5:(.30,.31,.84,1.0),4.0:(.33,.36,.80,.93),4.5:(.17,.34,.88,.73),
   5.0:(.10,.39,.95,.74),5.5:(.10,.40,1.0,.74),6.0:(.08,.40,1.0,.75),6.5:(.08,.40,.68,.76),7.0:(.08,.40,.47,.77),
   7.5:(.08,.40,.40,.78),8.0:(.08,.40,.36,.79),8.5:(.08,.40,.36,.80),9.0:(.08,.41,.36,.81),9.5:(.08,.41,.36,.82),10.0:(.06,.40,.36,.82)}
C={6.5:(.68,.57,1.0,.92),7.0:(.47,.44,.90,.72),7.5:(.40,.45,.83,.73),8.0:(.36,.47,.78,.73),8.5:(.36,.55,.83,.73),
   9.0:(.36,.56,.85,.73),9.5:(.36,.58,.88,.74),10.0:(.36,.60,.88,.74)}
M={2.5:(.24,.39,.44,.53),3.0:(.14,.53,.32,.67),3.5:(.12,.68,.30,.82),4.0:(.13,.69,.33,.83),4.5:(.18,.73,.40,.87),
   5.0:(.18,.74,.40,.88),5.5:(.19,.74,.41,.88),6.0:(.19,.75,.41,.89),6.5:(.20,.76,.42,.90),7.0:(.20,.78,.42,.92),
   7.5:(.19,.79,.41,.93),8.0:(.20,.80,.42,.94),8.5:(.20,.81,.42,.95),9.0:(.20,.82,.42,.96),9.5:(.20,.83,.42,.97),10.0:(.20,.83,.42,.97)}
c={"mediaId":536,"level":"B","keyWord":"peace","defaultVoice":"female",
 "taps":[{"phrase":"to settle into a hammock","target":"the woman","voice":"female","keys":keys(W)},
         {"phrase":"to climb onto her lap","target":"the cat","voice":"female","keys":keys(C)},
         {"phrase":"to rest on a wooden stool","target":"the mug","voice":"female","keys":keys(M)}],
 "stillS":10.0,
 "nouns":[{"word":"a hammock","x":.68,"y":.52,"voice":"female"},{"word":"a ginger cat","x":.55,"y":.68,"voice":"female"},
          {"word":"a mug","x":.30,"y":.88,"voice":"female"},{"word":"a palm leaf","x":.45,"y":.10,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","relaxing","in","a","hammock."],"answerVoice":"female",
 "notes":"Woman, cat and mug overlap in the picture, so the boxes are split: from 6.5 s the woman's box is her head and upper body left of the cat (her legs under/right of the cat are outside it); from 4.5 s her box ends above the mug, so her lower legs/feet are cut. While she carries the mug (2.5-4.0 s) the mug box is split from her box at the mug's right edge. Cat at 6.0 s is only an orange tip at the frame edge: off. Key word 'peace' is abstract, so it is not a noun slot and not in the answer."}
json.dump(c,open('content/536.json','w'),indent=1)
