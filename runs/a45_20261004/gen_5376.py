import json
T=[i*0.5 for i in range(25)]
B={0.0:(.20,.28,.70,.72),0.5:(.13,.24,.85,.76),1.0:(.13,.23,.87,.77),1.5:(.13,.23,.87,.77),2.0:(.08,.22,.92,.78),
2.5:(.10,.20,.90,.80),3.0:(.08,.20,.92,.80),3.5:(.02,.20,.98,.80),4.0:(0,.05,1,.95),4.5:(0,.05,1,.95),5.0:(0,.05,1,.95),
5.5:(.12,.23,.86,.77),6.0:(.08,.12,.88,.88),6.5:(.10,.48,.90,.47),7.0:(.05,.48,.95,.48),7.5:(.48,.50,.52,.48),
8.0:(.46,.50,.54,.45),8.5:(.13,.50,.87,.38),9.0:None,9.5:(.82,.62,.18,.38),10.0:(.60,.13,.40,.87),10.5:(.58,.13,.42,.87),
11.0:(.28,.17,.72,.83),11.5:(.18,.18,.82,.82),12.0:(.12,.19,.84,.81)}
def keys():
    out=[]
    for t in T:
        b=B[t]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
ph=["to flip a light switch","to grin into the camera","to gaze around the living room"]
c={"mediaId":5376,"level":"B","keyWord":"switch","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys()} for p in ph],
"stillS":2.5,
"nouns":[{"word":"a light switch","x":0.15,"y":0.50,"voice":"male"},{"word":"a doorway","x":0.40,"y":0.30,"voice":"male"},
{"word":"a denim shirt","x":0.80,"y":0.72,"voice":"male"}],
"question":"What is the man doing first?",
"answer":["He","is","flipping","a","light","switch."],"answerVoice":"male",
"notes":"Only one person; all three phrases target the man (hand-only close-up 6.5-8.5 s counts as him; off at 9.0 s, edge of frame at 9.5 s). Flips the switch 0.5-3 s and 6.5-8.5 s, grins into the lens 4-6 s, gazes around the lit room 10-12 s. 'a doorway' = dark glass door/opening behind him at 2.5 s."}
json.dump(c,open('content/5376.json','w'),indent=1)
