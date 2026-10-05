import json
T=[i*0.5 for i in range(17)]
def keys(f):
    return [dict(zip("txywh",(t,)+f(t))) for t in T]
def hog(t): return (0.03,0.39,0.65,0.43) if t<=3.5 else (0.05,0.38,0.52,0.44)
def cat(t): return (0.18,0.08,0.82,0.31) if t<=3.5 else (0.57,0.10,0.43,0.75)
d={"mediaId":4134,"level":"A","keyWord":"fat","defaultVoice":"female",
"taps":[
 {"phrase":"to have a fat belly","target":"the hedgehog","voice":"female","keys":keys(hog)},
 {"phrase":"to sit on a black chair","target":"the hedgehog","voice":"female","keys":keys(hog)},
 {"phrase":"to cover its mouth","target":"the cat","voice":"female","keys":keys(cat)}],
"stillS":4.0,
"nouns":[{"word":"a cat","x":0.70,"y":0.24,"voice":"female"},
 {"word":"a mirror","x":0.13,"y":0.20,"voice":"female"},
 {"word":"a chair","x":0.40,"y":0.86,"voice":"female"},
 {"word":"bottles","x":0.85,"y":0.07,"voice":"female"}],
"question":"Where is the fat animal sitting?",
"answer":["It","is","sitting","on","a","black","chair."],
"answerVoice":"female",
"notes":"Cat and hedgehog overlap in the picture all the time (the cat leans over it), so the cat's box is only a part of the cat: 0-3.5 s the band above the hedgehog (head, bow tie, shoulders, y < 0.39), from 4.0 s the column right of x 0.57 (most of the head, the paw at the mouth, the coat). 'to have a fat belly' is a state (key word 'fat'); the word 'hedgehog' is not A level, so it is only the target name and the question says 'the fat animal'. The cat covers its mouth with a paw from 4.5 s. The cat stands on a wooden stool, only the hedgehog sits on the black chair. 'bottles' = the group on the top right shelf (a few small dark bottles also stand far left near the mirror)."}
json.dump(d,open("content/4134.json","w"),indent=1,ensure_ascii=False)
