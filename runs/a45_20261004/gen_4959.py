import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
old={0.0:(0.04,0.44,0.58,0.56),0.5:(0.16,0.45,0.50,0.55),1.0:(0.15,0.43,0.65,0.57),1.5:(0.16,0.43,0.55,0.57),
     2.0:(0.16,0.44,0.46,0.56),2.5:(0.15,0.44,0.62,0.56)}
man={3.0:(0.12,0.39,0.45,0.61),3.5:(0.25,0.42,0.33,0.58),4.0:(0.07,0.45,0.41,0.55),4.5:(0.0,0.47,0.33,0.53)}
suit={6.0:(0.40,0.43,0.18,0.16),6.5:(0.41,0.43,0.18,0.17),7.0:(0.39,0.43,0.23,0.18),7.5:(0.38,0.44,0.24,0.19),
      8.0:(0.37,0.51,0.25,0.19),8.5:(0.37,0.62,0.25,0.20),9.0:(0.37,0.76,0.26,0.24),9.5:(0.41,0.86,0.18,0.14)}
c={"mediaId":4959,"level":"B","keyWord":"cottage","defaultVoice":"male",
 "taps":[
  {"phrase":"to lean out of a doorway","target":"the old man","voice":"male","keys":keys(old)},
  {"phrase":"to give a thumbs-up","target":"the bearded man","voice":"male","keys":keys(man)},
  {"phrase":"to pose by a reflecting pool","target":"the woman in white","voice":"female","keys":keys(suit)}],
 "stillS":3.5,
 "nouns":[{"word":"a cottage","x":0.44,"y":0.22,"voice":"male"},
          {"word":"a red door","x":0.76,"y":0.44,"voice":"male"},
          {"word":"a hedge","x":0.12,"y":0.58,"voice":"male"},
          {"word":"a gate","x":0.10,"y":0.85,"voice":"male"}],
 "question":"What is the old man doing?",
 "answer":["He","is","leaning","out","of","a","doorway."],
 "answerVoice":"male",
 "notes":"Three shots: old man at a tin-roofed hut, couple at a white weatherboard cottage, woman in white suit at a glass mansion. Thumbs-up by the bearded man is clear only at 4.0 s. Woman in white is tiny (min-size boxes). No single main person, evenId false -> defaultVoice male."}
json.dump(c,open('content/4959.json','w'),indent=1)
