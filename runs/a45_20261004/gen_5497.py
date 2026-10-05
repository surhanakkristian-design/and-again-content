import json
O=None
C={0.0:(0.21,0.36,0.56,0.64),0.5:(0.21,0.36,0.56,0.64),1.0:(0.21,0.36,0.56,0.64),1.5:(0.21,0.36,0.56,0.64),2.0:(0.21,0.36,0.56,0.64),
 2.5:(0.04,0.02,0.96,0.98),3.0:(0.02,0.02,0.98,0.98),3.5:(0.04,0.02,0.96,0.98),4.0:(0.0,0.02,1.0,0.98),4.5:(0.0,0.24,1.0,0.76),
 5.0:(0.06,0.38,0.88,0.62),5.5:(0.18,0.41,0.62,0.53),6.0:(0.25,0.42,0.34,0.38),6.5:(0.29,0.42,0.40,0.26),7.0:(0.30,0.41,0.38,0.24),
 7.5:(0.20,0.15,0.66,0.55),8.0:(0.12,0.12,0.86,0.60),8.5:(0.04,0.12,0.96,0.66),9.0:(0.0,0.17,1.0,0.83)}
S={0.0:(0.06,0.05,0.88,0.31),0.5:(0.06,0.05,0.88,0.31),1.0:(0.06,0.05,0.88,0.31),1.5:(0.06,0.05,0.88,0.31),2.0:(0.05,0.05,0.86,0.31),
 2.5:O,3.0:O,3.5:O,4.0:O,4.5:(0.10,0.07,0.74,0.16),5.0:(0.18,0.14,0.70,0.23),5.5:(0.18,0.17,0.64,0.23),6.0:(0.21,0.19,0.57,0.21),
 6.5:(0.23,0.19,0.55,0.21),7.0:(0.23,0.21,0.53,0.19),7.5:O,8.0:O,8.5:O,9.0:O}
def keys(D):
    return [{"t":t,"off":True} if D[t] is None else {"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} for t in sorted(D)]
c={"mediaId":5497,"level":"B","keyWord":"candidate","defaultVoice":"female",
 "taps":[{"phrase":"to clasp her hands nervously","target":"the candidate","voice":"female","keys":keys(C)},
  {"phrase":"to be lifted high","target":"the candidate","voice":"female","keys":keys(C)},
  {"phrase":"to show a rising bar chart","target":"the screen","voice":"female","keys":keys(S)}],
 "stillS":1.0,
 "nouns":[{"word":"a bar chart","x":0.38,"y":0.22,"voice":"female"},
  {"word":"a candidate","x":0.50,"y":0.47,"voice":"female"},{"word":"a rosette","x":0.60,"y":0.66,"voice":"female"}],
 "question":"What is happening to the candidate?","answer":["Her","supporters","are","lifting","her","into","the","air."],"answerVoice":"female",
 "notes":"Target 'the candidate' (the woman in the cream blazer; only she wears it). Screen marked off in the face close-ups (2.5-4.0, blurred behind her head) and at 7.5-9.0 where she is lifted in front of it. 'a candidate' (face) and 'a rosette' (chest) are on one large figure 0.19 apart - check. answerVoice female by default (subject = mixed supporters)."}
json.dump(c,open('content/5497.json','w'),indent=1)
