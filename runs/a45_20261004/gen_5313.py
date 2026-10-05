import json
def keys(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
T=[i/2 for i in range(25)]
d0={0.0:(0,.48,.78,.52),0.5:(0,.48,.92,.52),1.0:(0,.45,.80,.55),1.5:(.01,.43,.92,.57),2.0:(0,.45,.82,.55),
 2.5:(0,.45,.95,.55),3.0:(.04,.52,.74,.48),3.5:(0,.13,1,.87),4.0:(0,.13,1,.87),4.5:(0,.13,1,.87),5.0:(0,.14,1,.86),
 5.5:(0,.15,1,.85),6.0:(0,.16,1,.84),6.5:(0,.16,1,.84),7.0:(0,.18,1,.82),7.5:(0,.18,1,.82),8.0:(0,.20,1,.80),
 8.5:(0,.21,1,.79),9.0:(.01,.38,.98,.62),9.5:(.07,.38,.92,.62),10.0:(.25,.39,.53,.61),10.5:(.27,.41,.52,.59),
 11.0:(.25,.38,.53,.62),11.5:(.26,.40,.55,.60),12.0:(.20,.40,.60,.60)}
w=keys([(t,)+d0[t] for t in T])
d={"mediaId":5313,"level":"B","keyWord":"neon","defaultVoice":"female",
"taps":[{"phrase":"to twirl in a flowing dress","target":"the woman","voice":"female","keys":w},
{"phrase":"to slurp a rice cake","target":"the woman","voice":"female","keys":w},
{"phrase":"to make a finger heart","target":"the woman","voice":"female","keys":w}],
"stillS":10.0,
"nouns":[{"word":"neon signs","x":0.85,"y":0.18,"voice":"female"},{"word":"a zebra crossing","x":0.14,"y":0.61,"voice":"female"},
{"word":"a denim jacket","x":0.52,"y":0.75,"voice":"female"},{"word":"a bollard","x":0.10,"y":0.86,"voice":"female"}],
"question":"What is the woman eating?","answer":["She","is","slurping","a","chewy","rice","cake."],"answerVoice":"female",
"notes":"Only one real target (the woman); passing cars and the bus (11.0 only) are blurred, brief and overlap her, so all three phrases use her: twirl 0.0-3.0, slurp 3.5-5.0, hand/finger heart 10.0-12.0. Answer uses 'slurping' for a question with 'eating' - verifier may prefer 'eating'. Key word 'neon' (adjective) used in the noun 'neon signs' (right-hand buildings)."}
json.dump(d,open("content/5313.json","w"),indent=1)
