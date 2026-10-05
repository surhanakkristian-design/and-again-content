import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
P={0.2:(.17,.35,.45,.32,.33),0.7:(.16,.35,.45,.30,.33),1.2:(.15,.35,.43,.31,.33),1.7:(.13,.34,.44,.31,.33),
   2.2:(.12,.34,.44,.30,.32),2.7:(.12,.35,.44,.31,.33),3.2:(.14,.34,.43,.31,.33),3.7:(.08,.29,.40,.29,.30)}
r=lambda v:round(v,2)
man=[{"t":t,"x":P[t][2],"y":P[t][1],"w":r(1-P[t][2]),"h":r(1-P[t][1])} for t in T]
yel=[{"t":t,"x":P[t][4],"y":P[t][0],"w":r(.85-P[t][4]),"h":r(P[t][1]-P[t][0])} for t in T]
red=[{"t":t,"x":0.0,"y":0.12,"w":P[t][3],"h":0.86} for t in T]
c={"mediaId":5675,"level":"B","keyWord":"bound","defaultVoice":"male",
 "taps":[{"phrase":"to sit bound to a chair","target":"the man","voice":"male","keys":man},
  {"phrase":"to tie a big pink bow","target":"the woman in yellow","voice":"female","keys":yel},
  {"phrase":"to pull the ribbon tight","target":"the woman in red","voice":"female","keys":red}],
 "stillS":0.2,
 "nouns":[{"word":"a mast","x":0.52,"y":0.09,"voice":"male"},{"word":"a bow","x":0.66,"y":0.33,"voice":"male"},
  {"word":"a folding chair","x":0.56,"y":0.82,"voice":"male"}],
 "question":"What is the woman in yellow doing?",
 "answer":["She","is","tying","a","bow","on","his","head."],"answerVoice":"female",
 "notes":"Yellow woman stands behind the man: her box covers only her head, arms and the bow above the man's head (her dress below is behind his box); she also handles ribbon but only she ties the bow. Red woman box split at her reaching hands (x ~.30), fingertips cut a little. Key word 'bound' is an adjective, used in phrase 1, not a noun."}
json.dump(c,open('content/5675.json','w'),indent=1)
