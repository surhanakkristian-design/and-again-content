import json
T=[i*0.5 for i in range(19)]
w={0.0:(0.0,0.17,0.97,0.83),0.5:(0.0,0.0,0.97,1.0),1.0:(0.0,0.0,0.88,1.0),1.5:(0.0,0.0,0.95,1.0),2.0:(0.03,0.0,0.92,1.0),
2.5:(0.15,0.02,0.85,0.98),3.0:(0.15,0.18,0.75,0.82),3.5:(0.28,0.16,0.52,0.84),4.0:(0.17,0.36,0.6,0.64),4.5:(0.15,0.38,0.52,0.62)}
cy={5.0:0.28,5.5:0.29,6.0:0.29,6.5:0.30,7.0:0.32,7.5:0.33,8.0:0.32,8.5:0.32,9.0:0.36}
def k(d,t):
    if t in d: x,y,ww,h=d[t]; return {"t":t,"x":x,"y":y,"w":ww,"h":h}
    return {"t":t,"off":True}
wk=[k(w,t) for t in T]
ck=[k({t:(0.0,v,1.0,round(1-v,2)) for t,v in cy.items()},t) for t in T]
c={"mediaId":4884,"level":"A","keyWord":"point","defaultVoice":"female",
"taps":[{"phrase":"to point at the sky first","target":"the young woman","voice":"female","keys":wk},
{"phrase":"to open her mouth wide","target":"the young woman","voice":"female","keys":wk},
{"phrase":"to fill the old square","target":"the crowd","voice":"female","keys":ck}],
"stillS":7.0,
"nouns":[{"word":"the sky","x":0.5,"y":0.07,"voice":"female"},{"word":"a building","x":0.75,"y":0.22,"voice":"female"},
{"word":"umbrellas","x":0.2,"y":0.31,"voice":"female"},{"word":"a crowd","x":0.5,"y":0.65,"voice":"female"}],
"question":"What are the people doing?","answer":["They","are","pointing","at","the","sky."],"answerVoice":"female",
"notes":"Everyone points later, so the woman's phrase says 'first' (0-1.5 s only she points). 'Open her mouth wide': others gape a little, hers is clearly widest. The crowd is OFF 0-4.5 s while the close-up woman fills the frame (crowd behind her would overlap her box); crowd boxed 5.0-9.0 below the buildings. Woman OFF from 5.0 (not identifiable in the wide shot)."}
json.dump(c,open('content/4884.json','w'),indent=1)
