import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,0,0.88,0.50),0.5:(0,0,0.90,0.50),1.0:(0,0,0.45,0.50),1.5:(0,0,0.30,0.58),2.0:(0,0,0.60,0.55),2.5:(0,0,0.62,0.60),
3.0:(0,0,0.58,0.70),3.5:(0,0,0.55,0.68),4.0:(0,0,0.72,0.68),4.5:(0,0,0.72,0.65),5.0:(0,0,0.70,0.65),5.5:(0,0,0.46,0.72),
6.0:(0,0,0.38,0.62),6.5:(0,0.17,0.22,0.60),7.0:(0,0.22,0.24,0.50),7.5:(0,0.22,0.18,0.40),8.0:(0,0.07,0.25,0.68),8.5:(0,0,0.50,0.45),
9.5:(0,0,0.48,0.16),10.0:(0.03,0.11,0.50,0.66)}
woman={3.0:(0.72,0.48,0.28,0.20),3.5:(0.72,0.50,0.28,0.18),5.5:(0.50,0.40,0.50,0.42),6.0:(0.42,0.36,0.58,0.30),6.5:(0.24,0.10,0.76,0.72),
7.0:(0.25,0.18,0.75,0.72),7.5:(0.20,0.18,0.80,0.72),8.0:(0.44,0,0.56,0.78),10.0:(0.60,0.13,0.40,0.64)}
c={"mediaId":683,"level":"A","keyWord":"sink","defaultVoice":"male",
"taps":[
{"phrase":"to turn on the water","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to hold a yellow sponge","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to hold a clean plate","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":10.0,
"nouns":[{"word":"a man","x":0.25,"y":0.30,"voice":"male"},{"word":"a woman","x":0.76,"y":0.36,"voice":"female"},
{"word":"a sink","x":0.47,"y":0.60,"voice":"male"},{"word":"plates","x":0.60,"y":0.84,"voice":"male"}],
"question":"What are they washing in the sink?",
"answer":["They","are","washing","plates","in","the","sink."],
"answerVoice":"male",
"notes":"Many cuts and close-ups; often only the man's arms/hands are visible (boxes cover them). Woman is only hands at 3.0, 3.5, 5.5, 6.0. At 4.0-5.0 the man also holds a plate while scrubbing it (dirty, not clean) - 'to hold a clean plate' is meant for the woman holding up the clean plate at 6.0-8.0. At 7.0 the man's fingertips reach slightly into the woman's box. Noun 'plates' is on the big foreground plates at 10.0; a second small stack stands by the lemons."}
json.dump(c,open("content/683.json","w"),indent=1)
