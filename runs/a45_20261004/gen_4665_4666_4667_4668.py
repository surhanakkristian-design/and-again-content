import json
def keys(times, d):
    out=[]
    for t in times:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4665
t=T(21)
girl={2.5:(0,0.38,0.78,0.62),3.0:(0,0.36,0.65,0.64),3.5:(0,0,0.76,1),4.0:(0,0,0.76,1)}
man={6.0:(0.25,0,0.5,0.5),6.5:(0.22,0,0.56,0.5),7.0:(0.25,0,0.57,0.48),7.5:(0.2,0,0.58,0.48)}
mel={8.0:(0.24,0,0.46,0.24),8.5:(0.33,0.42,0.44,0.3),9.0:(0.15,0.47,0.85,0.3),9.5:(0.17,0.48,0.83,0.29),10.0:(0.15,0.47,0.85,0.28)}
save({"mediaId":4665,"level":"A","keyWord":"accident","defaultVoice":"male",
 "taps":[{"phrase":"to hold an ice cream","target":"the girl","voice":"female","keys":keys(t,girl)},
  {"phrase":"to hold a bag of fruit","target":"the man with the bag","voice":"male","keys":keys(t,man)},
  {"phrase":"to break into pieces","target":"the watermelon","voice":"male","keys":keys(t,mel)}],
 "stillS":7.5,
 "nouns":[{"word":"a bag","x":0.45,"y":0.13,"voice":"male"},{"word":"fruit","x":0.27,"y":0.46,"voice":"male"},
  {"word":"a can","x":0.72,"y":0.54,"voice":"male"},{"word":"the floor","x":0.5,"y":0.8,"voice":"male"}],
 "question":"What happens to the watermelon?",
 "answer":["The","watermelon","breaks","into","pieces."],"answerVoice":"male",
 "notes":"Five short shots (phone, ice cream, papers, bag of fruit, watermelon); each target has boxes only in its own shot. Key word 'accident' is abstract, not used as a noun. Question in present simple (a completed event, not an ongoing action). 'fruit' pill sits on the apples/orange left of the can; more fruit lies right of the can."})

# 4666
t=T(19)
man={0.0:(0,0.27,0.62,0.48),0.5:(0,0.05,0.28,0.48),2.0:(0,0.13,0.45,0.7),2.5:(0,0.16,0.46,0.58),3.0:(0,0.34,0.18,0.14),
 4.0:(0,0,0.26,0.46),4.5:(0,0.17,0.45,0.45),5.0:(0,0.27,0.55,0.16),5.5:(0,0.13,0.62,0.3),6.5:(0,0.15,0.22,0.72),
 7.0:(0,0.17,0.27,0.6),7.5:(0,0.14,0.24,0.34),8.0:(0,0.15,0.26,0.3),8.5:(0,0.22,0.37,0.28),9.0:(0,0.31,0.46,0.3)}
pum={5.0:(0.19,0.43,0.5,0.29),5.5:(0.38,0.44,0.36,0.24),6.0:(0.47,0.58,0.18,0.15),6.5:(0.22,0.19,0.48,0.42),
 7.0:(0.27,0.26,0.47,0.36),7.5:(0.42,0.55,0.33,0.2),8.0:(0.5,0.62,0.3,0.16),8.5:(0.62,0.66,0.27,0.17),9.0:(0.68,0.75,0.28,0.2)}
save({"mediaId":4666,"level":"B","keyWord":"smash","defaultVoice":"male",
 "taps":[{"phrase":"to lean over the edge","target":"the man","voice":"male","keys":keys(t,man)},
  {"phrase":"to shove a huge pumpkin","target":"the man","voice":"male","keys":keys(t,man)},
  {"phrase":"to raise a cloud of dust","target":"the pumpkin","voice":"male","keys":keys(t,pum)}],
 "stillS":5.0,
 "nouns":[{"word":"a pumpkin","x":0.42,"y":0.58,"voice":"male"},{"word":"the sky","x":0.6,"y":0.12,"voice":"male"},
  {"word":"skyscrapers","x":0.74,"y":0.4,"voice":"male"},{"word":"a ledge","x":0.33,"y":0.86,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","smashing","a","pumpkin","on","the","concrete."],"answerVoice":"male",
 "notes":"Man holds/pushes the pumpkin at 5.0, 6.5, 7.0: boxes split along the contact line (man = head/left side, pumpkin = the fruit). Man off where only fingertips show (1.0, 1.5, 3.5, 6.0); at 3.0 only his hand is visible. Two pumpkins (normal 5.0-6.0, giant 6.5-9.0) share the target 'the pumpkin'. 'a ledge' = the concrete parapet top; skyscrapers are small at 5.0."})

# 4667
t=T(21)
pl={0.0:(0.01,0.11,0.5,0.17),0.5:(0,0.1,0.74,0.29),1.0:(0.02,0,0.98,0.36),2.5:(0.24,0.25,0.28,0.17),3.0:(0.04,0.03,0.3,0.24),
 3.5:(0,0,0.36,0.22),4.0:(0.16,0.19,0.61,0.18),4.5:(0.31,0.11,0.58,0.39),5.0:(0.05,0.22,0.58,0.3),5.5:(0.2,0.3,0.48,0.21),
 6.0:(0.31,0.3,0.4,0.15),6.5:(0.34,0.31,0.36,0.14),7.0:(0.33,0.33,0.3,0.14),7.5:(0.27,0.34,0.26,0.14),8.0:(0.28,0.34,0.2,0.14),
 8.5:(0.31,0.34,0.2,0.14),9.0:(0.33,0.34,0.2,0.14),9.5:(0.35,0.34,0.2,0.14),10.0:(0.37,0.33,0.2,0.14)}
wo={0.0:(0.19,0.44,0.59,0.56),0.5:(0.16,0.78,0.5,0.22),2.5:(0,0.55,0.24,0.45),3.0:(0,0.41,0.48,0.59),3.5:(0.15,0.49,0.45,0.51),
 4.0:(0.46,0.76,0.48,0.24),7.5:(0.68,0.67,0.32,0.33),8.0:(0.53,0.61,0.28,0.28),8.5:(0.5,0.57,0.24,0.25),9.0:(0.45,0.57,0.3,0.22),
 9.5:(0.45,0.57,0.26,0.18),10.0:(0.43,0.59,0.26,0.19)}
save({"mediaId":4667,"level":"A","keyWord":"plane","defaultVoice":"female",
 "taps":[{"phrase":"to fly over the tents","target":"the plane","voice":"female","keys":keys(t,pl)},
  {"phrase":"to drop a wooden box","target":"the plane","voice":"female","keys":keys(t,pl)},
  {"phrase":"to open her arms wide","target":"the woman","voice":"female","keys":keys(t,wo)}],
 "stillS":0.0,
 "nouns":[{"word":"a plane","x":0.25,"y":0.19,"voice":"female"},{"word":"a tent","x":0.17,"y":0.57,"voice":"female"},
  {"word":"horses","x":0.8,"y":0.6,"voice":"female"},{"word":"a woman","x":0.45,"y":0.8,"voice":"female"}],
 "question":"What is the plane doing?",
 "answer":["It","is","dropping","boxes","from","the","sky."],"answerVoice":"female",
 "notes":"The woman is the one in the striped robe; tiny villagers at 5.5-7.5 are not boxed. Plane is very small from 7.5 on (minimum-size boxes). Woman opens her arms at 8.5-10.0."})

# 4668
t=T(9)
wo={0.0:(0.42,0.17,0.56,0.83),0.5:(0.46,0.24,0.54,0.76),1.0:(0.46,0.2,0.54,0.8),1.5:(0.44,0.25,0.56,0.75),2.0:(0.37,0.26,0.63,0.74),
 2.5:(0.27,0.2,0.73,0.8),3.0:(0.33,0.2,0.67,0.8),3.5:(0.36,0.25,0.62,0.75),4.0:(0.3,0.21,0.68,0.79)}
k=keys(t,wo)
save({"mediaId":4668,"level":"B","keyWord":"to smell","defaultVoice":"female",
 "taps":[{"phrase":"to hang out the laundry","target":"the woman","voice":"female","keys":k},
  {"phrase":"to straighten a white shirt","target":"the woman","voice":"female","keys":k},
  {"phrase":"to sniff the fresh laundry","target":"the woman","voice":"female","keys":k}],
 "stillS":2.0,
 "nouns":[{"word":"a shirt","x":0.2,"y":0.42,"voice":"female"},{"word":"a clothesline","x":0.62,"y":0.27,"voice":"female"},
  {"word":"an apron","x":0.68,"y":0.72,"voice":"female"},{"word":"roof tiles","x":0.22,"y":0.87,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","smelling","a","clean","shirt."],"answerVoice":"female",
 "notes":"Only one possible target (the woman), used for all three phrases. She smells the cloth only at 3.5 s; the cloth looks like a white shirt (cuff visible)."})
