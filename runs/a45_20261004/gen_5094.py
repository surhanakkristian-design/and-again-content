import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0,1,1),2.0:(0,0,0.5,1)}
woman={2.0:(0.52,0.24,0.48,0.76),2.5:(0,0.12,1,0.88),3.0:(0,0.07,1,0.93),3.5:(0,0.08,1,0.92),4.0:(0,0.08,1,0.92),4.5:(0,0.1,1,0.9)}
bb={5.5:(0.5,0.2,0.5,0.5)}
for t in T:
    if t>=6.0: bb[t]=(0,0.02,1,0.98)
c={"mediaId":5094,"level":"B","keyWord":"skinny","defaultVoice":"male",
"taps":[
 {"phrase":"to grimace with effort","target":"the red-haired man","voice":"male","keys":K(man)},
 {"phrase":"to beam at the camera","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to flex both biceps","target":"the bodybuilder","voice":"male","keys":K(bb)}],
"stillS":7.0,
"nouns":[{"word":"a wristwatch","x":0.74,"y":0.25,"voice":"male"},
 {"word":"a black vest","x":0.55,"y":0.62,"voice":"male"},
 {"word":"a weight bench","x":0.12,"y":0.79,"voice":"male"}],
"question":"What is the bodybuilder doing?",
"answer":["He","is","flexing","both","biceps."],"answerVoice":"male",
"notes":"Three shots: red-haired man 0-2.0, woman in blue top 2.0-4.5 (the second woman behind her is her mirror reflection, not boxed), whip pan 5.0 (all off), bodybuilder from 5.5 (5.5 = blurry dark torso at the right, weak). At 2.0 man and woman are split at x 0.5 though her arm crosses in front of him. The red-haired man's arm looks fairly muscular in the AI frames, so 'skinny' is not used in a phrase. Two friends in the background at 6-9 shout, they do not beam into the camera."}
json.dump(c,open('content/5094.json','w'),indent=1)
