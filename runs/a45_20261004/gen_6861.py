import json
def keys(times, boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(times,boxes)]
T=[0.2,0.7,1.2]
man=[(0.0,0.10,0.63,0.76),(0.0,0.10,0.64,0.79),(0.0,0.09,0.64,0.84)]
maid=[(0.69,0.15,0.31,0.70),(0.71,0.16,0.29,0.72),(0.73,0.16,0.27,0.50)]
c={"mediaId":6861,"level":"B","keyWord":"baron","defaultVoice":"male",
 "taps":[
  {"phrase":"to reach for a silver tray","target":"the young man","voice":"male","keys":keys(T,man)},
  {"phrase":"to lean forward from the waist","target":"the young man","voice":"male","keys":keys(T,man)},
  {"phrase":"to hold up a champagne glass","target":"the maid","voice":"female","keys":keys(T,maid)}],
 "stillS":0.2,
 "nouns":[{"word":"a chandelier","x":0.12,"y":0.06,"voice":"male"},
          {"word":"a silver tray","x":0.70,"y":0.37,"voice":"male"},
          {"word":"guests","x":0.42,"y":0.64,"voice":"male"},
          {"word":"a red carpet","x":0.62,"y":0.87,"voice":"male"}],
 "question":"What is the young man reaching for?",
 "answer":["He","is","reaching","for","a","silver","tray."],
 "answerVoice":"male",
 "notes":"Short clip (1.75 s), single shot. Guests below are not a tap target because their group overlaps the young man's legs. Key word 'baron' is not a visible noun. 'guests' pill sits on the group in gowns behind his legs; the man's legs are near x 0.1-0.3, pill centre at 0.42 is on the guests."}
json.dump(c,open('content/6861.json','w'),indent=1)
