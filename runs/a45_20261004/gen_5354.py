import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
A={0.0:(0.21,0.0,0.56,1.0),0.5:(0.17,0.03,0.64,0.97),1.0:(0.10,0.11,0.72,0.89),1.5:(0.04,0.18,0.76,0.82),
   5.0:(0.0,0.34,0.32,0.50),5.5:(0.0,0.37,0.36,0.44),6.0:(0.11,0.40,0.26,0.36),6.5:(0.16,0.42,0.23,0.32),
   7.0:(0.17,0.44,0.22,0.28),7.5:(0.18,0.44,0.24,0.28),8.0:(0.20,0.46,0.26,0.24),8.5:(0.20,0.47,0.26,0.23),9.0:(0.20,0.48,0.26,0.23)}
M={3.0:(0.15,0.24,0.85,0.76),3.5:(0.14,0.23,0.86,0.77),6.0:(0.0,0.40,0.11,0.30),6.5:(0.0,0.40,0.16,0.28),
   7.0:(0.0,0.42,0.17,0.27),7.5:(0.0,0.43,0.18,0.27),8.0:(0.0,0.45,0.20,0.23),8.5:(0.0,0.46,0.20,0.22),9.0:(0.0,0.47,0.20,0.21)}
c={"mediaId":5354,"level":"A","keyWord":"class","defaultVoice":"female",
 "taps":[
  {"phrase":"to laugh with her eyes closed","target":"the woman at the front","voice":"female","keys":keys(A)},
  {"phrase":"to lean to one side","target":"the woman at the front","voice":"female","keys":keys(A)},
  {"phrase":"to kneel on the grass","target":"the man in the blue vest","voice":"male","keys":keys(M)}],
 "stillS":6.5,
 "nouns":[{"word":"the sky","x":0.5,"y":0.06,"voice":"female"},{"word":"trees","x":0.5,"y":0.25,"voice":"female"},
          {"word":"a class","x":0.5,"y":0.55,"voice":"female"},{"word":"grass","x":0.5,"y":0.85,"voice":"female"}],
 "question":"What is the class doing?",
 "answer":["The","class","is","exercising","on","the","grass."],
 "answerVoice":"female",
 "notes":"Clip has cuts and a crowd. Woman at 4.0 s (grey top, BLUE leggings, eyes closed) treated as a different woman (the centre woman of the group shots), so the leader is off at 4.0-4.5; if she is the leader, 'laugh with her eyes closed' still fits only the leader (4.0 woman is not laughing). Leader followed in group shots as the front-left woman in grey top + black leggings; man in blue vest followed as the far-left man; boxes split at the line between them. 'kneel on the grass': partial figures at the right edge at 3.0-3.5 also lunge."}
json.dump(c,open('content/5354.json','w'),indent=1)
