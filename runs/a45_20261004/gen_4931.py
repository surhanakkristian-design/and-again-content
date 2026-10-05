import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
W={0.5:(0.06,0.0,0.97,0.92),1.0:(0.23,0.08,0.90,1.0),1.5:(0.18,0.31,0.72,1.0),2.0:(0.0,0.45,0.77,1.0),2.5:(0.0,0.47,1.0,1.0),
   3.0:(0.25,0.47,1.0,1.0),3.5:(0.44,0.65,1.0,1.0),4.0:(0.02,0.28,0.85,1.0),4.5:(0.05,0.27,0.90,1.0),
   6.0:(0.42,0.34,1.0,0.97),6.5:(0.62,0.38,1.0,0.68),7.0:(0.78,0.44,1.0,0.64),
   7.5:(0.0,0.21,1.0,1.0),8.0:(0.0,0.21,1.0,1.0),8.5:(0.0,0.23,1.0,1.0),9.0:(0.0,0.22,1.0,1.0)}
S={0.0:(0.34,0.46,1.0,0.62),1.5:(0.73,0.48,1.0,0.64),2.0:(0.0,0.30,1.0,0.45),2.5:(0.0,0.30,1.0,0.46),
   5.0:(0.0,0.10,1.0,0.86),5.5:(0.0,0.10,1.0,0.86)}
c={"mediaId":4931,"level":"B","keyWord":"diagram","defaultVoice":"female",
 "taps":[
  {"phrase":"to stride into the lecture hall","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to point at the diagram","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to stare in amazement","target":"the students","voice":"female","keys":keys(S)}],
 "stillS":8.0,
 "nouns":[{"word":"a diagram","x":0.30,"y":0.19,"voice":"female"},
          {"word":"glasses","x":0.60,"y":0.30,"voice":"female"},
          {"word":"a blazer","x":0.72,"y":0.76,"voice":"female"},
          {"word":"wooden panels","x":0.16,"y":0.86,"voice":"female"}],
 "question":"What is the woman pointing at?",
 "answer":["She","is","pointing","at","the","chalk","diagram."],
 "answerVoice":"female",
 "notes":"Students box at 2.0/2.5 covers only the rows above the woman's head (split to avoid overlap); students off at 0.5/1.0 (hidden behind her legs/bag). 'the students' voice = defaultVoice (mixed group). Phrase 1 fits 0.5-1.5 only; she points at the diagram 4.0-4.5."}
json.dump(c,open('content/4931.json','w'),indent=1)
