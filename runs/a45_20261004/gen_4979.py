import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
man={1.0:(0.0,0.74,0.18,0.92),1.5:(0.0,0.0,0.33,0.88),2.0:(0.0,0.02,0.72,1.0),2.5:(0.02,0.12,0.98,1.0),
 3.0:(0.02,0.18,1.0,1.0),3.5:(0.58,0.38,1.0,0.72),4.0:(0.62,0.0,1.0,0.7)}
blonde={3.5:(0.0,0.38,0.5,1.0),4.0:(0.25,0.25,0.61,0.82),4.5:(0.2,0.26,0.84,0.93),5.0:(0.0,0.32,0.7,1.0)}
stand={5.5:(0.34,0.17,1.0,0.68)}
c={"mediaId":4979,"level":"A","keyWord":"office","defaultVoice":"male",
 "taps":[
  {"phrase":"to give her a pen","target":"the man in the dark jumper","voice":"male","keys":keys(man)},
  {"phrase":"to take a pen","target":"the blonde woman in white","voice":"female","keys":keys(blonde)},
  {"phrase":"to hand him some papers","target":"the standing woman","voice":"female","keys":keys(stand)}],
 "stillS":0.0,
 "nouns":[{"word":"a man","x":0.42,"y":0.52,"voice":"male"},
          {"word":"a window","x":0.62,"y":0.14,"voice":"male"},
          {"word":"a keyboard","x":0.86,"y":0.79,"voice":"male"},
          {"word":"a phone","x":0.86,"y":0.95,"voice":"male"}],
 "question":"What are the office workers doing?",
 "answer":["They","are","blowing","their","noses."],
 "answerVoice":"male",
 "notes":"Many quick shots. Coughing/handshake avoided as phrases (two men do both). The man in the dark jumper hands the pen at 3.5-4.0; at 4.0 his hand is in front of the woman, boxes split at x 0.61/0.62 (his hand on the pen left out). Key word 'office' is the whole scene, not placed as a noun. Standing woman with papers only at 5.5. Answer: several people blow their noses (5.0, 7.0-9.0); the coughing men are not covered by it."}
json.dump(c,open('content/4979.json','w'),indent=1)
