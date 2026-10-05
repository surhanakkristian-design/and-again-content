import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
host={0.5:(0.25,0.27,0.75,0.73),1.0:(0.0,0.22,1.0,0.78),1.5:(0.0,0.24,0.37,0.76),2.0:(0.36,0.24,0.2,0.6),
 2.5:(0.0,0.2,1.0,0.8),3.0:(0.15,0.24,0.62,0.76),3.5:(0.12,0.18,0.88,0.82),4.0:(0.0,0.45,0.55,0.5),
 4.5:(0.2,0.19,0.78,0.46),5.0:(0.18,0.16,0.8,0.6),5.5:(0.08,0.2,0.92,0.62),6.0:(0.2,0.2,0.4,0.42),
 6.5:(0.38,0.23,0.28,0.28),7.0:(0.38,0.24,0.38,0.25),7.5:(0.3,0.08,0.46,0.44),8.0:(0.25,0.08,0.52,0.52),
 8.5:(0.23,0.1,0.52,0.48),9.0:(0.32,0.24,0.31,0.32)}
glasses={1.5:(0.38,0.27,0.37,0.73),2.0:(0.56,0.26,0.18,0.2),6.5:(0.7,0.11,0.3,0.5),7.0:(0.78,0.22,0.22,0.42),
 7.5:(0.82,0.31,0.18,0.3),8.0:(0.8,0.39,0.2,0.32),8.5:(0.79,0.4,0.21,0.26),9.0:(0.65,0.4,0.35,0.3)}
woman={2.0:(0.0,0.3,0.36,0.7),6.5:(0.0,0.16,0.3,0.4),7.0:(0.0,0.28,0.32,0.3),7.5:(0.0,0.32,0.3,0.3),
 8.0:(0.0,0.4,0.24,0.32),8.5:(0.0,0.4,0.22,0.28),9.0:(0.0,0.4,0.3,0.25)}
c={"mediaId":4922,"level":"A","keyWord":"host","defaultVoice":"male",
 "taps":[{"phrase":"to carry the coats","target":"the host","voice":"male","keys":K(host)},
  {"phrase":"to wear glasses","target":"the man in glasses","voice":"male","keys":K(glasses)},
  {"phrase":"to wear a warm sweater","target":"the woman","voice":"female","keys":K(woman)}],
 "stillS":7.0,
 "nouns":[{"word":"a host","x":0.58,"y":0.38,"voice":"male"},{"word":"pasta","x":0.35,"y":0.64,"voice":"male"},
  {"word":"a salad","x":0.8,"y":0.65,"voice":"male"},{"word":"bread","x":0.55,"y":0.86,"voice":"male"}],
 "question":"What is the host carrying?",
 "answer":["He","is","carrying","the","coats."],"answerVoice":"male",
 "notes":"Host = young man in waistcoat. Cuts: door (0.0, no one), hug (1.5-2.0), coats (2.5-4.0; at 4.0 only his arm hanging a coat), kitchen glasses (4.5-6.0, blurry behind glass at 5.5-6.0), dinner table (6.5-9.0). Curly-haired woman (light shirt) only at 1.5-2.0, not a target; 'the woman' = the one in the patterned sweater (2.0 hug left, table left). Tight boxes in the 2.0 hug; man in glasses small there. Two of the three phrases are states (no action fits only the guests: everyone laughs and toasts)."}
json.dump(c,open('content/4922.json','w'),indent=1)
