import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
white={0.0:(.17,.25,.57,.75),0.5:(0,.18,1,.82),1.0:(0,.18,1,.82),1.5:(0,.18,1,.82),2.0:(.02,.2,.97,.8),2.5:(0,.45,.14,.55),
 5.0:(.40,.36,.235,.55),5.5:(.37,.35,.23,.46),6.0:(.39,.33,.21,.35),6.5:(.39,.34,.21,.35),7.0:(.41,.40,.21,.44),7.5:(.36,.34,.25,.56),
 8.0:(0,.25,.36,.75),8.5:(0,.1,1,.9),9.0:(0,0,1,1)}
black={2.5:(.36,.33,.56,.67),5.0:(.64,.38,.19,.41),5.5:(.60,.37,.19,.36),6.0:(.60,.35,.19,.30),6.5:(.60,.35,.19,.30),7.0:(.62,.40,.20,.30),
 7.5:(.615,.48,.35,.23),8.0:(.37,.58,.55,.30)}
woman={3.0:(0,.1,1,.86),5.0:(.835,.41,.165,.36),5.5:(.83,.39,.17,.36),6.0:(.83,.39,.17,.31),6.5:(.83,.39,.17,.31),7.0:(.84,.38,.16,.26)}
c={"mediaId":5133,"level":"B","keyWord":"scream","defaultVoice":"male",
"taps":[
 {"phrase":"to film himself laughing","target":"the man in white","voice":"male","keys":K(white)},
 {"phrase":"to collapse onto the grass","target":"the man in the printed T-shirt","voice":"male","keys":K(black)},
 {"phrase":"to do a star jump","target":"the woman in black shorts","voice":"female","keys":K(woman)}],
"stillS":7.5,
"nouns":[{"word":"a pine tree","x":0.80,"y":0.20,"voice":"male"},{"word":"a lamp post","x":0.74,"y":0.34,"voice":"male"},
 {"word":"a bench","x":0.36,"y":0.43,"voice":"male"},{"word":"grass","x":0.50,"y":0.90,"voice":"male"}],
"question":"What is the man in white doing?",
"answer":["He","is","laughing","into","the","camera."],"answerVoice":"male",
"notes":"Key word scream is a verb (no noun slot). Woman in black crop top + black shorts does the star jump at 3.0 s and is identified as the right-edge woman in the group shots 5.0-7.0 (same outfit, partly cut off); the brunette at 4.0 s is a different woman and not a target. Man in printed T-shirt (glasses at 2.5 s) lies on the grass at 7.5/8.0 s; marked off at 3.0 s where only his hand shows at the left edge."}
json.dump(c,open('content/5133.json','w'),indent=1)
