import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
old={0.0:(0.02,0.26,0.68,0.74),0.5:(0.0,0.27,0.64,0.73),1.0:(0.0,0.29,0.62,0.71),1.5:(0.02,0.30,0.68,0.70),
     2.0:(0.0,0.31,0.62,0.69),2.5:(0.0,0.32,0.58,0.68),3.0:(0.0,0.32,0.58,0.68),3.5:(0.0,0.32,0.58,0.68)}
young={4.0:(0.0,0.20,0.52,0.80),4.5:(0.0,0.24,0.50,0.76),5.0:(0.0,0.28,0.48,0.72),5.5:(0.0,0.31,0.60,0.69),
       6.0:(0.0,0.36,0.44,0.62),6.5:(0.0,0.38,0.43,0.62),7.0:(0.0,0.50,0.18,0.50),7.5:(0.0,0.50,0.18,0.50)}
suit={8.0:(0.40,0.24,0.30,0.76),8.5:(0.28,0.25,0.47,0.75),9.0:(0.12,0.24,0.72,0.76),9.5:(0.48,0.24,0.50,0.76),
      10.0:(0.66,0.26,0.34,0.74),10.5:(0.69,0.26,0.31,0.74),11.0:(0.70,0.26,0.30,0.74),11.5:(0.70,0.27,0.30,0.73),12.0:(0.69,0.27,0.31,0.73)}
c={"mediaId":4958,"level":"B","keyWord":"villa","defaultVoice":"female",
 "taps":[
  {"phrase":"to point at a run-down hut","target":"the old man","voice":"male","keys":keys(old)},
  {"phrase":"to spread his arms wide","target":"the young man","voice":"male","keys":keys(young)},
  {"phrase":"to present a luxury villa","target":"the woman in the suit","voice":"female","keys":keys(suit)}],
 "stillS":9.5,
 "nouns":[{"word":"a villa","x":0.35,"y":0.30,"voice":"female"},
          {"word":"a fountain","x":0.52,"y":0.56,"voice":"female"},
          {"word":"a pool","x":0.25,"y":0.68,"voice":"female"},
          {"word":"pebbles","x":0.30,"y":0.84,"voice":"female"}],
 "question":"What is the woman in cream doing?",
 "answer":["She","is","presenting","a","luxury","villa."],
 "answerVoice":"female",
 "notes":"Three-shot clip (hut / suburban house / villa). Young man's arm spread at 6.0-6.5; the young woman also opens her hands slightly at 6.5-7.5 but not wide. defaultVoice female (no single main person, evenId true)."}
json.dump(c,open('content/4958.json','w'),indent=1)
