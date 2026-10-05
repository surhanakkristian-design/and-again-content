import json
O = None
G = [(0.06,0.0,0.76,0.54),(0.0,0.0,1.0,0.78),(0.0,0.0,1.0,0.90),O,O,O,O,O,O,O,
     (0.0,0.0,0.48,0.72),(0.0,0.0,0.49,0.72),(0.0,0.0,0.47,0.70),(0.0,0.0,0.40,0.70),(0.0,0.0,0.46,0.72),
     (0.0,0.03,0.52,0.65),(0.0,0.08,0.43,0.55),(0.17,0.10,0.35,0.44),(0.16,0.18,0.44,0.40),(0.13,0.19,0.41,0.38),
     (0.15,0.18,0.33,0.28),(0.24,0.18,0.20,0.23),(0.25,0.20,0.18,0.22),(0.31,0.22,0.19,0.14),(0.30,0.23,0.18,0.14)]
S = [O,O,O,(0.38,0.10,0.25,0.36),(0.38,0.10,0.26,0.36),(0.38,0.10,0.26,0.36),(0.37,0.12,0.27,0.35),(0.38,0.12,0.26,0.34),
     (0.37,0.11,0.27,0.34),(0.37,0.11,0.26,0.34),
     (0.48,0.0,0.52,0.74),(0.49,0.0,0.51,0.74),(0.47,0.0,0.53,0.75),(0.42,0.0,0.58,0.75),(0.46,0.04,0.54,0.72),
     (0.52,0.0,0.46,0.68),(0.43,0.05,0.42,0.54),(0.52,0.10,0.33,0.42),(0.60,0.18,0.27,0.37),(0.54,0.18,0.23,0.37),
     (0.48,0.18,0.22,0.35),(0.44,0.20,0.21,0.32),(0.43,0.22,0.18,0.28),(0.50,0.26,0.18,0.26),(0.48,0.27,0.18,0.28)]
def keys(L): return [dict(t=i*0.5,off=True) if b is None else dict(t=i*0.5,x=b[0],y=b[1],w=b[2],h=b[3]) for i,b in enumerate(L)]
c = {"mediaId":5231,"level":"B","keyWord":"hospitality","defaultVoice":"female",
 "taps":[
  {"phrase":"to serve steaming dumplings","target":"the elderly woman","voice":"female","keys":keys(G)},
  {"phrase":"to pour a glass of tea","target":"the elderly woman","voice":"female","keys":keys(G)},
  {"phrase":"to give off steam","target":"the samovar","voice":"female","keys":keys(S)}],
 "stillS":4.0,
 "nouns":[{"word":"a samovar","x":0.52,"y":0.30,"voice":"female"},
          {"word":"dumplings","x":0.42,"y":0.55,"voice":"female"},
          {"word":"pickles","x":0.80,"y":0.68,"voice":"female"},
          {"word":"pancakes","x":0.53,"y":0.80,"voice":"female"}],
 "question":"What is the elderly woman serving?",
 "answer":["She","is","serving","steaming","dumplings."],
 "answerVoice":"female",
 "notes":"Elderly woman only identifiable at 0.0-1.0 (carrying the dumpling platter, which is inside her box) and 5.0-12.0; hands placing bread/pickles at 2.0-3.5 are not clearly hers, so off. Samovar steams from its chimney at 1.5-4.5 and 9.0-11.0; the dumplings also steam faintly at 0.0-1.0 (samovar off then). Key word 'hospitality' is abstract, no noun slot. In the last frames (11.5-12.0) arms and glasses hide most of both targets; boxes split around her face / the samovar body."}
json.dump(c, open('content/5231.json','w'), indent=1)
