import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
# boxes as x0,y0,x1,y1
man={0.0:(.10,0,.98,.57),0.5:(.14,0,1,.58),1.0:(.12,0,.97,.58),1.5:(.12,0,1,.57),2.0:(.10,0,.96,.57),2.5:(.12,0,1,.57),
 3.0:(.15,0,1,.57),3.5:(.14,0,1,.51),4.0:(.08,0,1,.52),4.5:(.73,0,1,.90),5.0:(.73,.05,1,.90),5.5:(.74,.05,1,.90),
 6.0:(.75,0,1,.90),6.5:(.76,0,1,.90),7.0:(.75,0,1,.90),7.5:(.76,0,1,.90),8.0:(.75,0,1,.90),
 8.5:(.54,0,1,.49),9.0:(.54,0,1,.49),9.5:(.54,0,1,.49),10.0:(.54,0,1,.49),10.5:(.57,0,1,.49),
 11.0:(.21,0,1,.49),11.5:(.21,.02,.40,.90),12.0:(.19,.02,.45,.80)}
bl={0.0:(.24,.58,.72,.96),0.5:(.26,.59,.74,.96),1.0:(.24,.59,.72,.96),1.5:(.26,.58,.74,.96),2.0:(.24,.58,.72,.96),2.5:(.26,.58,.74,.96),
 3.0:(.24,.58,.72,.96),3.5:(.26,.52,.76,.96),4.0:(.24,.53,.72,.96),4.5:(.12,.12,.72,.98),5.0:(.10,.08,.72,1),5.5:(.08,.08,.73,1),
 6.0:(.08,.08,.74,1),6.5:(.08,.05,.75,1),7.0:(.05,.06,.74,1),7.5:(.06,.05,.75,1),8.0:(.03,.04,.74,1),
 8.5:(0,.06,.52,.49),9.0:(0,.06,.52,.49),9.5:(0,.06,.52,.49),10.0:(0,.04,.52,.49),10.5:(0,.08,.56,.49),
 11.0:(0,.34,.20,.92),11.5:(0,.36,.20,.92),12.0:(0,.34,.18,.76)}
gl={8.5:(.32,.50,.72,.99),9.0:(.32,.50,.72,.99),9.5:(.32,.50,.72,.99),10.0:(.32,.50,.72,.99),10.5:(.32,.50,.72,.99),
 11.0:(.31,.50,.74,1),11.5:(.41,.19,.75,.78),12.0:(.46,.03,.78,.47)}
c={"mediaId":4407,"level":"A","keyWord":"healthy","defaultVoice":"male",
 "taps":[
  {"phrase":"to make a healthy drink","target":"the man","voice":"male","keys":K(man)},
  {"phrase":"to mix the fruit","target":"the blender","voice":"male","keys":K(bl)},
  {"phrase":"to fill up with juice","target":"the glass","voice":"male","keys":K(gl)}],
 "stillS":0.0,
 "nouns":[{"word":"a man","x":.55,"y":.22,"voice":"male"},{"word":"a blender","x":.50,"y":.70,"voice":"male"},
          {"word":"bananas","x":.86,"y":.78,"voice":"male"},{"word":"spinach","x":.76,"y":.90,"voice":"male"}],
 "question":"What is the man making?",
 "answer":["He","is","making","a","healthy","drink."],
 "answerVoice":"male",
 "notes":"Man and blender overlap in the picture: split along the top edge of the jug (0-4 s) and along the jug's right edge in the close-ups (4.5-8 s); at 11-12 s the man's box is only the part of him not covered by the jug/glass. From 8.5 s 'the blender' is only its jug (base out of frame). Glass appears at 8.5 s. 'bananas' = the peeled bananas on the counter at 0.0 s, close above the spinach."}
json.dump(c,open('content/4407.json','w'),indent=1)
