import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
man=K([(0.18,0.19,0.42,0.74),(0.21,0.18,0.42,0.79),(0.14,0.15,0.59,0.84),(0.13,0.15,0.51,0.85),
       (0.13,0.17,0.48,0.82),(0.12,0.18,0.53,0.81),(0.12,0.18,0.54,0.82),(0.11,0.18,0.55,0.82)])
woman=K([(0.61,0.33,0.18,0.26),(0.64,0.33,0.18,0.22),None,(0.65,0.33,0.18,0.22),
         (0.62,0.33,0.18,0.26),(0.66,0.34,0.18,0.26),(0.67,0.34,0.18,0.24),(0.67,0.34,0.18,0.24)])
d={"mediaId":6906,"level":"B","keyWord":"browser","defaultVoice":"male",
 "taps":[{"phrase":"to slouch against a bookshelf","target":"the man","voice":"male","keys":man},
         {"phrase":"to point idly at a shelf","target":"the man","voice":"male","keys":man},
         {"phrase":"to scribble in a notebook","target":"the woman","voice":"female","keys":woman}],
 "stillS":2.2,
 "nouns":[{"word":"a browser","x":0.32,"y":0.55,"voice":"male"},
          {"word":"a window","x":0.60,"y":0.20,"voice":"male"},
          {"word":"a desk lamp","x":0.86,"y":0.42,"voice":"male"},
          {"word":"a cardboard box","x":0.29,"y":0.88,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","slouching","against","a","bookshelf."],
 "answerVoice":"male",
 "notes":"'slouch' chosen over 'lean' because a ladder also leans against the shelves on the left. The woman at the desk sits right behind the man's shoulder: boxes split at his coat edge; she is hidden at 1.2 s (off). Pointing happens 1.2-1.7 s only. 'a browser' pill sits on the man (key word as person noun); check it reads as natural."}
json.dump(d,open("content/6906.json","w"),indent=1)
