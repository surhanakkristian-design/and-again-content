import json,os
H=os.path.dirname(os.path.abspath(__file__))
def keys(times,d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
T=[i*0.5 for i in range(21)]
girl={}
for t in [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5]: girl[t]=(0.01,0.26,0.28,0.19)
girl.update({4.0:(0.0,0.24,0.25,0.19),4.5:(0.0,0.24,0.22,0.18),5.0:(0.0,0.23,0.22,0.19),5.5:(0.0,0.23,0.22,0.19),6.0:(0.0,0.24,0.22,0.19),6.5:(0.0,0.24,0.20,0.18),7.0:(0.0,0.24,0.25,0.19),7.5:(0.0,0.25,0.21,0.18)})
man={}
for t in [0.0,0.5,1.0,1.5]: man[t]=(0.30,0.19,0.68,0.53)
for t in [2.0,2.5]: man[t]=(0.30,0.18,0.67,0.54)
for t in [3.0,3.5]: man[t]=(0.30,0.18,0.66,0.54)
man.update({4.0:(0.26,0.14,0.72,0.56),4.5:(0.23,0.12,0.75,0.58),5.0:(0.23,0.12,0.76,0.58),5.5:(0.23,0.12,0.76,0.58),6.0:(0.23,0.12,0.77,0.58),6.5:(0.21,0.13,0.79,0.57),7.0:(0.26,0.09,0.74,0.62),7.5:(0.22,0.10,0.78,0.60),
 8.0:(0.0,0.02,1.0,0.80),8.5:(0.12,0.03,0.88,0.94),9.0:(0.0,0.05,1.0,0.95),9.5:(0.04,0.06,0.96,0.94),10.0:(0.02,0.04,0.98,0.96)})
mk=keys(T,man)
c={"mediaId":5077,"level":"B","keyWord":"recall","defaultVoice":"male",
"taps":[
 {"phrase":"to recall the answers","target":"the student","voice":"male","keys":mk},
 {"phrase":"to take notes","target":"the girl on the left","voice":"female","keys":keys(T,girl)},
 {"phrase":"to punch the air","target":"the student","voice":"male","keys":mk}],
"stillS":6.0,
"nouns":[{"word":"a pillar","x":0.17,"y":0.10,"voice":"male"},{"word":"glasses","x":0.55,"y":0.33,"voice":"male"},
 {"word":"headphones","x":0.50,"y":0.45,"voice":"male"},{"word":"flashcards","x":0.55,"y":0.80,"voice":"male"}],
"question":"What is the student doing?","answer":["He","is","trying","to","recall","the","answers."],"answerVoice":"male",
"notes":"One shot. The girl on the left is blurred in the background, writing with a pen (pen clearest at 0.0-1.0); she is hidden once he stands up (8.0+). Her box sits right behind the student's left shoulder, so the student's box is split vertically next to it and his left arm/elbow (x 0.03-0.29) lies outside his box at 0.0-7.5. A second blurred woman appears behind his right shoulder at 7.0-7.5 (not a target). 'to punch the air' happens at 9.5-10.0 (fist pump); 'to recall the answers' = card to forehead with eyes closed, tapping his temple at 8.5-9.0."}
json.dump(c,open(f"{H}/content/5077.json","w"),indent=1)
