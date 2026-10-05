import json
T=[i*0.5 for i in range(19)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(d): return [k(t,d.get(t)) for t in T]
wo={5.0:(0.0,0.06,0.47,0.9),5.5:(0.0,0.07,0.5,0.88),6.0:(0.0,0.07,0.48,0.88),6.5:(0.0,0.03,0.44,0.92),7.0:(0.0,0.02,0.3,0.73)}
man={5.0:(0.6,0.13,0.33,0.5),5.5:(0.63,0.13,0.34,0.5),6.0:(0.68,0.18,0.31,0.45),6.5:(0.69,0.17,0.31,0.45),7.0:(0.66,0.12,0.33,0.48)}
gr={7.5:(0.18,0.5,0.7,0.3),8.0:(0.21,0.49,0.66,0.33),8.5:(0.17,0.5,0.73,0.36),9.0:(0.17,0.51,0.69,0.35)}
c={"mediaId":4899,"level":"A","keyWord":"enormous","defaultVoice":"male",
 "taps":[
  {"phrase":"to wear her hair in braids","target":"the woman with braids","voice":"female","keys":keys(wo)},
  {"phrase":"to close his eyes","target":"the man in the dark hat","voice":"male","keys":keys(man)},
  {"phrase":"to lift a whole tree","target":"the gardeners","voice":"male","keys":keys(gr)}],
 "stillS":6.0,
 "nouns":[{"word":"a straw hat","x":0.25,"y":0.14,"voice":"male"},
          {"word":"a radish","x":0.5,"y":0.38,"voice":"male"},
          {"word":"roots","x":0.6,"y":0.82,"voice":"male"}],
 "question":"What are the gardeners doing?",
 "answer":["They","are","lifting","an","enormous","tree."],
 "answerVoice":"male",
 "notes":"Four shots: carrot (0-2.0), radish with one man (2.5-4.5), radish with woman + man in dark hat (5.0-7.0), tree with group (7.5-9.0). Carrot/radish shots have no unique target phrase (both vegetables come out of the ground, man at 2.5-4.5 wears the same light-blue shirt as the dark-hat man), so they carry no boxes. 'to close his eyes': eyes shut 5.0-6.5, open and shouting at 7.0 (still boxed). Woman and dark-hat man may be among the group at 7.5+ (too small to tell) - off there. 'radish' maybe A2+."}
json.dump(c,open("content/4899.json","w"),indent=1)
